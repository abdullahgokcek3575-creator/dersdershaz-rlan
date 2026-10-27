// 5. Sınıf Akıllı Çalışma Portalı - Universal Interaction Engine
// Fully compatible with Mobile, Tablet, Desktop, Smart TV / TV Box (D-Pad & Remote)

class StudyPortal {
  constructor(lessonKey = 'general', lang = 'tr-TR') {
    this.lessonKey = lessonKey;
    this.lang = lang;
    this.scores = {};
    this.maxScore = 100;
    this.currentAudio = null;
    this.isPaused = false;

    this.init();
  }

  init() {
    this.loadScores();
    this.setupTabs();
    this.updateScoreDisplay();
    this.setupKeyboardNavigation();
  }

  // --- TAB NAVIGATION ---
  setupTabs() {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');

    tabBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const targetId = btn.getAttribute('data-tab');

        tabBtns.forEach(b => b.classList.remove('active'));
        tabPanes.forEach(p => p.classList.remove('active'));

        btn.classList.add('active');
        const targetPane = document.getElementById(targetId);
        if (targetPane) targetPane.classList.add('active');
      });
    });
  }

  // --- TV BOX & SMART TV REMOTE CONTROL / D-PAD NAVIGATION ---
  setupKeyboardNavigation() {
    window.addEventListener('keydown', (e) => {
      // Space or Enter on focused element works naturally
      // Allow number keys 1, 2, 3 to switch tabs quickly on TV Remotes
      if (['1', '2', '3'].includes(e.key) && document.activeElement.tagName !== 'TEXTAREA') {
        const tabs = document.querySelectorAll('.tab-btn');
        const idx = parseInt(e.key) - 1;
        if (tabs[idx]) tabs[idx].click();
      }
    });
  }

  // --- STUDIO NEURAL AUDIO ENGINE ---
  playAudio(audioFile, highlightElId = null) {
    this.stopAudio();

    const audioPath = `assets/audio/${audioFile}`;
    const audio = new Audio(audioPath);
    this.currentAudio = audio;

    const audioBar = document.querySelector('.audio-bar');
    const statusText = document.getElementById('audioStatusText');

    if (highlightElId) {
      document.querySelectorAll('.active-reading').forEach(c => c.classList.remove('active-reading'));
      const el = document.getElementById(highlightElId);
      if (el) el.classList.add('active-reading');
    }

    audio.onplay = () => {
      this.isPaused = false;
      if (audioBar) audioBar.classList.add('speaking');
      if (statusText) statusText.textContent = '🔊 Doğal Stüdyo Seslendirmesi Çalıyor...';
    };

    audio.onended = () => {
      this.isPaused = false;
      if (audioBar) audioBar.classList.remove('speaking');
      if (statusText) statusText.textContent = 'Hazır (Dinlemek için ses butonlarına dokunun)';
      document.querySelectorAll('.active-reading').forEach(c => c.classList.remove('active-reading'));
    };

    audio.onerror = () => {
      if (statusText) statusText.textContent = 'ℹ️ Ses dosyası çalınamadı.';
    };

    audio.play().catch(err => {
      console.log('Audio autoplay prevented or stopped:', err);
    });
  }

  pauseSpeech() {
    const statusText = document.getElementById('audioStatusText');
    if (this.currentAudio) {
      if (this.currentAudio.paused) {
        this.currentAudio.play();
        this.isPaused = false;
        if (statusText) statusText.textContent = '🔊 Seslendirme Devam Ediyor...';
      } else {
        this.currentAudio.pause();
        this.isPaused = true;
        if (statusText) statusText.textContent = '⏸️ Seslendirme Duraklatıldı';
      }
    }
  }

  stopAudio() {
    if (this.currentAudio) {
      this.currentAudio.pause();
      this.currentAudio.currentTime = 0;
      this.currentAudio = null;
    }
    const audioBar = document.querySelector('.audio-bar');
    const statusText = document.getElementById('audioStatusText');
    if (audioBar) audioBar.classList.remove('speaking');
    if (statusText) statusText.textContent = 'Hazır (Dinlemek için ses butonlarına dokunun)';
    document.querySelectorAll('.active-reading').forEach(c => c.classList.remove('active-reading'));
  }

  stopSpeech() {
    this.stopAudio();
  }

  // --- INTERACTIVE ACTIONS ON DIRECT PDF OR CARD ---
  toggleSolution(solId) {
    const el = document.getElementById(solId);
    if (!el) return;
    el.classList.toggle('show');
    if (el.classList.contains('show')) {
      el.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  }

  toggleHint(hintId) {
    const el = document.getElementById(hintId);
    if (!el) return;
    el.classList.toggle('show');
  }

  gradeQuestion(qId, maxPts, awardedPts, btnEl) {
    this.scores[qId] = awardedPts;
    localStorage.setItem(`scores_${this.lessonKey}`, JSON.stringify(this.scores));
    this.updateScoreDisplay();

    // Highlight button in parent container
    if (btnEl && btnEl.parentElement) {
      btnEl.parentElement.querySelectorAll('.grade-btn').forEach(b => {
        b.classList.remove('active-full', 'active-half', 'active-zero');
      });
      if (awardedPts === maxPts) btnEl.classList.add('active-full');
      else if (awardedPts > 0) btnEl.classList.add('active-half');
      else btnEl.classList.add('active-zero');
    }
  }

  updateScoreDisplay() {
    const total = Object.values(this.scores).reduce((a, b) => a + b, 0);
    const scoreValEl = document.getElementById('currentScoreVal');
    if (scoreValEl) scoreValEl.textContent = total;
  }

  loadScores() {
    const saved = localStorage.getItem(`scores_${this.lessonKey}`);
    if (saved) {
      try {
        this.scores = JSON.parse(saved);
      } catch (e) {
        this.scores = {};
      }
    }
  }

  finishExam() {
    const total = Object.values(this.scores).reduce((a, b) => a + b, 0);
    const modal = document.getElementById('scoreModal');
    const scoreVal = document.getElementById('finalScoreVal');
    const feedback = document.getElementById('scoreFeedback');

    if (scoreVal) scoreVal.textContent = total;

    if (feedback) {
      if (total >= 85) {
        feedback.innerHTML = '🌟 <strong>Tebrikler, Mükemmel Başarı!</strong><br>Konuları çok iyi kavramışsın. Yazılı sınavında yüksek not almaya hazırsın!';
      } else if (total >= 70) {
        feedback.innerHTML = '👍 <strong>Çok Güzel Bir Çalışma!</strong><br>Başarın oldukça iyi. Birkaç eksik olduğun sorunun çözümünü tekrar dinleyerek 100 tam puana ulaşabilirsin.';
      } else {
        feedback.innerHTML = '💪 <strong>Gayretin Çok Değerli!</strong><br>Önemli hap bilgileri ve öğretmen çözümlerini bir kez daha dinleyip tekrar dene, başaracaksın!';
      }
    }

    if (modal) modal.classList.add('show');
  }

  closeModal() {
    const modal = document.getElementById('scoreModal');
    if (modal) modal.classList.remove('show');
  }
}

let portalApp;
function initLesson(lessonKey, lang = 'tr-TR') {
  portalApp = new StudyPortal(lessonKey, lang);
}
