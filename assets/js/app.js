// ============================================================
// 5. Sınıf Akıllı Yazılı Çalışma Portalı — Universal Engine v3
// Tam cihaz uyumu: Telefon, Tablet, Bilgisayar, Smart TV, TV Box
// Ses: MP3 → Hybrid SpeechSynthesis Fallback (masaüstü tam destek)
// ============================================================

class StudyPortal {
  constructor(lessonKey = 'general', lang = 'tr-TR') {
    this.lessonKey = lessonKey;
    this.lang = lang;
    this.scores = {};
    this.maxScore = 100;
    this.currentAudio = null;
    this.currentUtterance = null;
    this.isPaused = false;
    this.synth = window.speechSynthesis || null;

    this.init();
  }

  init() {
    this.loadScores();
    this.setupTabs();
    this.updateScoreDisplay();
    this.setupKeyboardNavigation();
    this.setupPdfOverlays();
  }

  // ---- TAB NAVIGATION ----
  setupTabs() {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');
    tabBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const targetId = btn.getAttribute('data-tab');
        tabBtns.forEach(b => b.classList.remove('active'));
        tabPanes.forEach(p => p.classList.remove('active'));
        btn.classList.add('active');
        const pane = document.getElementById(targetId);
        if (pane) pane.classList.add('active');
      });
    });
  }

  // ---- SMART TV / TV BOX KEYBOARD NAVIGATION ----
  setupKeyboardNavigation() {
    window.addEventListener('keydown', (e) => {
      const tag = document.activeElement ? document.activeElement.tagName : '';
      if (['TEXTAREA', 'INPUT'].includes(tag)) return;
      if (['1','2','3'].includes(e.key)) {
        const tabs = document.querySelectorAll('.tab-btn');
        const idx = parseInt(e.key) - 1;
        if (tabs[idx]) tabs[idx].click();
      }
    });
  }

  // ---- PDF OVERLAY AUTO-RESIZE ----
  setupPdfOverlays() {
    document.querySelectorAll('.pdf-overlay-textarea').forEach(ta => {
      ta.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = Math.max(this.scrollHeight, 30) + 'px';
      });
    });
  }

  // ---- HYBRID AUDIO ENGINE ----
  // 1. Try MP3 file first (fast, pre-rendered)
  // 2. If MP3 fails (404, autoplay block, etc.) → fall back to SpeechSynthesis
  playAudio(audioFile, highlightId = null, fallbackText = null) {
    this.stopAudio();

    if (highlightId) {
      document.querySelectorAll('.active-reading').forEach(c => c.classList.remove('active-reading'));
      const el = document.getElementById(highlightId);
      if (el) { el.classList.add('active-reading'); el.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); }
    }

    const audioPath = 'assets/audio/' + audioFile;
    const audio = new Audio(audioPath);
    this.currentAudio = audio;
    this._updateStatus('⏳ Ses yükleniyor...', true);

    audio.onplay = () => this._updateStatus('🔊 Seslendirme çalıyor...', true);
    audio.onended = () => this._clearAudio();
    audio.onerror = () => {
      // MP3 not found → use SpeechSynthesis
      this.currentAudio = null;
      const txt = fallbackText || document.getElementById(highlightId || '')?.innerText || audioFile;
      this._speakText(txt);
    };

    audio.play().catch(() => {
      this.currentAudio = null;
      const txt = fallbackText || '';
      if (txt) this._speakText(txt);
    });
  }

  // Speak text directly (no MP3 needed — works everywhere)
  speakText(text, lang = null) {
    this.stopAudio();
    this._speakText(text, lang);
  }

  _speakText(text, lang = null) {
    if (!this.synth || !text) {
      this._updateStatus('ℹ️ Seslendirme desteklenmiyor', false);
      return;
    }
    // Cancel any ongoing speech
    this.synth.cancel();

    const utter = new SpeechSynthesisUtterance(text);
    utter.lang = lang || this.lang;
    utter.rate = 0.9;
    utter.pitch = 1.0;

    // Try to pick a natural-sounding voice
    const voices = this.synth.getVoices();
    const langCode = (lang || this.lang).toLowerCase().split('-')[0];
    const preferred = voices.find(v => v.lang.toLowerCase().startsWith(langCode) && (v.name.includes('Google') || v.name.includes('Microsoft') || v.localService));
    const fallback = voices.find(v => v.lang.toLowerCase().startsWith(langCode));
    if (preferred || fallback) utter.voice = preferred || fallback;

    utter.onstart = () => this._updateStatus('🔊 Seslendirme çalıyor...', true);
    utter.onend = () => this._clearAudio();
    utter.onerror = () => this._updateStatus('❌ Ses çalınamadı', false);

    this.currentUtterance = utter;
    this.synth.speak(utter);
  }

  pauseSpeech() {
    const statusText = document.getElementById('audioStatusText');
    if (this.currentAudio) {
      if (this.currentAudio.paused) {
        this.currentAudio.play();
        if (statusText) statusText.textContent = '🔊 Devam ediyor...';
      } else {
        this.currentAudio.pause();
        if (statusText) statusText.textContent = '⏸️ Duraklatıldı';
      }
    } else if (this.synth) {
      if (this.synth.paused) {
        this.synth.resume();
        if (statusText) statusText.textContent = '🔊 Devam ediyor...';
      } else {
        this.synth.pause();
        if (statusText) statusText.textContent = '⏸️ Duraklatıldı';
      }
    }
  }

  stopSpeech() { this.stopAudio(); }

  stopAudio() {
    if (this.currentAudio) {
      this.currentAudio.pause();
      this.currentAudio.currentTime = 0;
      this.currentAudio = null;
    }
    if (this.synth) this.synth.cancel();
    this.currentUtterance = null;
    this._clearAudio();
  }

  _updateStatus(msg, speaking) {
    const bar = document.querySelector('.audio-bar');
    const txt = document.getElementById('audioStatusText');
    if (bar) { speaking ? bar.classList.add('speaking') : bar.classList.remove('speaking'); }
    if (txt) txt.textContent = msg;
  }

  _clearAudio() {
    this._updateStatus('Hazır — ses butonlarına dokunun', false);
    document.querySelectorAll('.active-reading').forEach(c => c.classList.remove('active-reading'));
  }

  // ---- SOLUTION / HINT TOGGLES ----
  toggleSolution(id) {
    const el = document.getElementById(id);
    if (!el) return;
    el.classList.toggle('show');
    if (el.classList.contains('show')) el.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  toggleHint(id) {
    const el = document.getElementById(id);
    if (el) el.classList.toggle('show');
  }

  // ---- SELF GRADING ----
  gradeQuestion(qId, maxPts, awarded, btnEl) {
    this.scores[qId] = awarded;
    localStorage.setItem('scores_' + this.lessonKey, JSON.stringify(this.scores));
    this.updateScoreDisplay();

    if (btnEl && btnEl.parentElement) {
      btnEl.parentElement.querySelectorAll('.grade-btn').forEach(b => {
        b.classList.remove('active-full','active-half','active-zero');
      });
      if (awarded === maxPts) btnEl.classList.add('active-full');
      else if (awarded > 0) btnEl.classList.add('active-half');
      else btnEl.classList.add('active-zero');
    }
  }

  updateScoreDisplay() {
    const total = Object.values(this.scores).reduce((a,b) => a+b, 0);
    const el = document.getElementById('currentScoreVal');
    if (el) el.textContent = total;
  }

  loadScores() {
    const saved = localStorage.getItem('scores_' + this.lessonKey);
    if (saved) { try { this.scores = JSON.parse(saved); } catch(e) { this.scores = {}; } }
  }

  finishExam() {
    const total = Object.values(this.scores).reduce((a,b) => a+b, 0);
    const modal = document.getElementById('scoreModal');
    const scoreVal = document.getElementById('finalScoreVal');
    const feedback = document.getElementById('scoreFeedback');
    if (scoreVal) scoreVal.textContent = total;
    if (feedback) {
      if (total >= 85) feedback.innerHTML = '🌟 <strong>Tebrikler, Mükemmel!</strong><br>Yazılı sınavına çok iyi hazırlandın!';
      else if (total >= 70) feedback.innerHTML = '👍 <strong>Çok İyi!</strong><br>Birkaç soruyu tekrar gözden geçir, tam puana ulaşabilirsin.';
      else feedback.innerHTML = '💪 <strong>Devam Et!</strong><br>Çözümleri sesli dinleyerek tekrar çalış, başaracaksın!';
    }
    if (modal) modal.classList.add('show');
  }

  closeModal() {
    const modal = document.getElementById('scoreModal');
    if (modal) modal.classList.remove('show');
  }

  // ---- PDF CANVAS DRAWING ----
  setupCanvas(canvasId, imgId) {
    const canvas = document.getElementById(canvasId);
    const img = document.getElementById(imgId);
    if (!canvas || !img) return;
    const ctx = canvas.getContext('2d');
    let drawing = false, lastX = 0, lastY = 0;
    ctx.strokeStyle = '#1a1aff';
    ctx.lineWidth = 2;
    ctx.lineCap = 'round';

    function getPos(e, rect) {
      const scale = canvas.width / rect.width;
      if (e.touches) {
        return [(e.touches[0].clientX - rect.left) * scale, (e.touches[0].clientY - rect.top) * scale];
      }
      return [(e.clientX - rect.left) * scale, (e.clientY - rect.top) * scale];
    }

    ['mousedown','touchstart'].forEach(ev => canvas.addEventListener(ev, e => {
      e.preventDefault(); drawing = true;
      const rect = canvas.getBoundingClientRect();
      [lastX, lastY] = getPos(e, rect);
    }, { passive: false }));

    ['mousemove','touchmove'].forEach(ev => canvas.addEventListener(ev, e => {
      e.preventDefault();
      if (!drawing) return;
      const rect = canvas.getBoundingClientRect();
      const [x, y] = getPos(e, rect);
      ctx.beginPath(); ctx.moveTo(lastX, lastY); ctx.lineTo(x, y); ctx.stroke();
      [lastX, lastY] = [x, y];
    }, { passive: false }));

    ['mouseup','touchend','mouseleave'].forEach(ev => canvas.addEventListener(ev, () => drawing = false));
  }

  clearCanvas(canvasId) {
    const canvas = document.getElementById(canvasId);
    if (canvas) canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
  }
}

let portalApp;
function initLesson(lessonKey, lang = 'tr-TR') {
  // Ensure voices are loaded before first use
  if (window.speechSynthesis) {
    window.speechSynthesis.getVoices();
    window.speechSynthesis.onvoiceschanged = () => window.speechSynthesis.getVoices();
  }
  portalApp = new StudyPortal(lessonKey, lang);
}
