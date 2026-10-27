# -*- coding: utf-8 -*-
import os, sys

def get_header(current_page="home"):
    links = [
        ("index.html", "🏠 Ana Sayfa", "home"),
        ("turkce.html", "📚 Türkçe", "turkce"),
        ("matematik.html", "📐 Matematik", "mat"),
        ("fen-bilimleri.html", "🔬 Fen Bilimleri", "fen"),
        ("sosyal-bilgiler.html", "🌍 Sosyal Bilgiler", "sosyal"),
        ("din-kulturu.html", "🕌 Din Kültürü", "din"),
        ("ingilizce.html", "🇬🇧 İngilizce", "ingilizce"),
        ("qr_giris.html", "📱 Ağ / TV Giriş", "qr"),
    ]
    nav_html = ""
    for href, title, key in links:
        active_cls = " active" if key == current_page else ""
        nav_html += f'<a href="{href}" class="nav-link{active_cls}">{title}</a>\n'
    return f"""
    <header class="site-header">
      <div class="nav-bar">
        <a href="index.html" class="brand-link">
          <span class="brand-badge">5. SINIF</span>
          <span>Akıllı Yazılı Çalışma Portalı</span>
        </a>
        <nav class="nav-links">
          {nav_html}
        </nav>
      </div>
    </header>
    """

def get_footer():
    return """
    <footer class="site-footer">
      <div class="container">
        <p style="font-weight: 700; color: #1e293b; font-size: 1rem;">5. Sınıf 1. Dönem 1. Yazılı Akıllı Hazırlık Portalı</p>
        <p style="margin-top: 4px;">Milli Eğitim Bakanlığı Müfredatı ile Tam Uyumlu Etkileşimli Çalışma & Sesli Çözüm Materyali</p>
        <p style="margin-top: 8px; font-size: 0.82rem; color: #94a3b8;">Her Hakkı Saklıdır • Telefon, Tablet, Akıllı TV ve Bilgisayar Uyumlu</p>
      </div>
    </footer>
    """

def get_score_modal():
    return """
    <div id="scoreModal" class="modal-overlay">
      <div class="modal-content">
        <h2>🎉 Sınav Çalışması Tamamlandı!</h2>
        <div class="modal-score" id="finalScoreVal">100</div>
        <p style="font-weight: 700; color: #64748b; margin-bottom: 12px;">Toplam Başarı Puanı / 100</p>
        <p id="scoreFeedback" style="font-size: 1.05rem; line-height: 1.5; color: #334155;">Harika bir çalışma gerçekleştirdin!</p>
        <button class="btn-modal" onclick="portalApp.closeModal()">Kapat ve İncelemeye Devam Et</button>
      </div>
    </div>
    """

# 1. TÜRKÇE
def get_turkce_html():
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>5. Sınıf Türkçe 1. Dönem 1. Yazılı - Orijinal PDF Üzerinde Çalışma</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>body {{ font-family: 'Plus Jakarta Sans', system-ui, sans-serif; }}</style>
</head>
<body class="theme-turkce">
  {get_header('turkce')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>📚</span> Türkçe 1. Dönem 1. Yazılı</h1>
        <p>Orijinal Sınav Kağıdı Üzerinde Soru Soru Sesli Çözüm • Metinde Anlam • Söz Sanatları • Yazım Kuralları</p>
      </div>
      <div class="score-box">
        <div class="score-val" id="currentScoreVal">0</div>
        <div class="score-lbl">Mevcut Puan / 100</div>
      </div>
    </div>

    <!-- Master Audio Bar -->
    <div class="audio-bar">
      <div class="audio-bar-info">
        <div class="audio-icon-pulse">🔊</div>
        <div>
          <strong style="display:block; font-size:0.95rem;">Türkçe Doğal Sesli Öğretmen Anlatımı</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır (Dinlemek için ses butonlarına dokunun)</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.playAudio('turkce_summary.mp3')">📢 Sınav Konu Özetini Dinle</button>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="pdf-pane">📄 Orijinal PDF Üzerinde Çalış & Dinle</button>
      <button class="tab-btn" data-tab="summary-pane">💡 Sınavda Çıkacak Hap Bilgiler</button>
    </div>

    <!-- TAB 1: DIRECT PDF WORKBENCH -->
    <div id="pdf-pane" class="tab-pane active">
      <div class="interactive-pdf-container">
        
        <!-- PAGE 1 -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Orijinal Sınav Kağıdı - Sayfa 1 (Soru 1, Soru 2, Soru 3)</span>
            <span style="font-size:0.85rem; opacity:0.85;">1. Dönem 1. Yazılı</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/img/turkce_p1.png" alt="Türkçe Sayfa 1" loading="eager">
          </div>
          <div class="pdf-question-controls">
            <!-- Q1 Controls -->
            <div class="q-strip-header">
              <div class="q-strip-title"><span>📌 Soru 1:</span> Metinden Sözcük Bulma (15 Puan)</div>
              <div class="q-strip-actions">
                <button class="btn-q-action audio-play" onclick="portalApp.playAudio('turkce_q1.mp3')">🔊 Soruyu Dinle</button>
                <button class="btn-q-action" onclick="portalApp.playAudio('turkce_sol1.mp3')">🎙️ Çözümü Dinle</button>
                <button class="btn-q-action solution-btn" onclick="portalApp.toggleSolution('pdf_sol_tr_1')">✅ Çözümü Aç / Kapat</button>
              </div>
            </div>
            <textarea class="student-input-box" placeholder="Cevabını buraya yazabilirsin (1: İcat, 2: Yosun, 3: Mıknatıs)..."></textarea>
            <div id="pdf_sol_tr_1" class="q-solution-reveal">
              <strong>✅ Resmi Cevap:</strong> 1. İcat (Buluş) • 2. Yosun • 3. Mıknatıs (Demirkapan). Metindeki bağlamdan hareketle doğru kelimeler tespit edilir.
              <div class="self-grading">
                <span>Puan Ver:</span>
                <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_tr_1', 15, 15, this)">15 Puan (Tam)</button>
                <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_tr_1', 15, 8, this)">8 Puan</button>
                <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_tr_1', 15, 0, this)">0 Puan</button>
              </div>
            </div>

            <hr style="border:none; border-top:1px solid #e2e8f0; margin:10px 0;">

            <!-- Q2 Controls -->
            <div class="q-strip-header">
              <div class="q-strip-title"><span>📌 Soru 2:</span> Metnin Konusu ve Ana Fikri (20 Puan)</div>
              <div class="q-strip-actions">
                <button class="btn-q-action audio-play" onclick="portalApp.playAudio('turkce_q2.mp3')">🔊 Soruyu Dinle</button>
                <button class="btn-q-action" onclick="portalApp.playAudio('turkce_sol2.mp3')">🎙️ Çözümü Dinle</button>
                <button class="btn-q-action solution-btn" onclick="portalApp.toggleSolution('pdf_sol_tr_2')">✅ Çözümü Aç / Kapat</button>
              </div>
            </div>
            <textarea class="student-input-box" placeholder="Metnin ana fikrini ve konusunu buraya yazınız..."></textarea>
            <div id="pdf_sol_tr_2" class="q-solution-reveal">
              <strong>✅ Resmi Cevap:</strong> Konu: Yapay zekâ veri merkezlerinin aşırı elektrik ve su tüketimiyle çevreye olan etkileri.<br>
              Ana Fikir: Teknolojik gelişmeler insanlığa kolaylık sağlarken doğal kaynaklarımızın tükenmemesi için enerji ve su verimliliği gözetilmelidir.
              <div class="self-grading">
                <span>Puan Ver:</span>
                <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_tr_2', 20, 20, this)">20 Puan (Tam)</button>
                <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_tr_2', 20, 10, this)">10 Puan</button>
                <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_tr_2', 20, 0, this)">0 Puan</button>
              </div>
            </div>
          </div>
        </div>

        <!-- PAGE 2 -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Orijinal Sınav Kağıdı - Sayfa 2 (Soru 4, Soru 5)</span>
            <span style="font-size:0.85rem; opacity:0.85;">1. Dönem 1. Yazılı</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/img/turkce_p2.png" alt="Türkçe Sayfa 2" loading="lazy">
          </div>
          <div class="pdf-question-controls">
            <!-- Q4 Controls -->
            <div class="q-strip-header">
              <div class="q-strip-title"><span>📌 Soru 4:</span> Kişileştirme Sanatına Örnekler (15 Puan)</div>
              <div class="q-strip-actions">
                <button class="btn-q-action audio-play" onclick="portalApp.playAudio('turkce_q4.mp3')">🔊 Soruyu Dinle</button>
                <button class="btn-q-action" onclick="portalApp.playAudio('turkce_sol4.mp3')">🎙️ Çözümü Dinle</button>
                <button class="btn-q-action solution-btn" onclick="portalApp.toggleSolution('pdf_sol_tr_4')">✅ Çözümü Aç / Kapat</button>
              </div>
            </div>
            <textarea class="student-input-box" placeholder="İki adet kişileştirme cümlesi yazınız..."></textarea>
            <div id="pdf_sol_tr_4" class="q-solution-reveal">
              <strong>✅ Örnek Cevap:</strong> 1. "Rüzgâr gece boyunca pencerelere kızgın kızgın vurdu." • 2. "Güneş sabah yüzünü gösterdiğinde çiçekler sevinçle gülümsedi."
              <div class="self-grading">
                <span>Puan Ver:</span>
                <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_tr_4', 15, 15, this)">15 Puan (Tam)</button>
                <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_tr_4', 15, 8, this)">8 Puan</button>
                <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_tr_4', 15, 0, this)">0 Puan</button>
              </div>
            </div>

            <hr style="border:none; border-top:1px solid #e2e8f0; margin:10px 0;">

            <!-- Q5 Controls -->
            <div class="q-strip-header">
              <div class="q-strip-title"><span>📌 Soru 5:</span> Yazım Kurallarını Örneklendirme (30 Puan)</div>
              <div class="q-strip-actions">
                <button class="btn-q-action audio-play" onclick="portalApp.playAudio('turkce_q5.mp3')">🔊 Soruyu Dinle</button>
                <button class="btn-q-action" onclick="portalApp.playAudio('turkce_sol5.mp3')">🎙️ Çözümü Dinle</button>
                <button class="btn-q-action solution-btn" onclick="portalApp.toggleSolution('pdf_sol_tr_5')">✅ Çözümü Aç / Kapat</button>
              </div>
            </div>
            <textarea class="student-input-box" placeholder="I. Tarih cümlesi, II. Coğrafi tür adı cümlesi, III. Cadde/Sokak cümlesi..."></textarea>
            <div id="pdf_sol_tr_5" class="q-solution-reveal">
              <strong>✅ Örnek Cümleler:</strong><br>
              I: "Kardeşim <strong>12 Mayıs 2018 Cumartesi</strong> günü doğdu."<br>
              II: "Tatilimizi <strong>Van Gölü</strong> kıyısında geçirdik."<br>
              III: "Teyzem <strong>Atatürk Bulvarı, Menekşe Sokak</strong>ta oturuyor."
              <div class="self-grading">
                <span>Puan Ver:</span>
                <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_tr_5', 30, 30, this)">30 Puan (Tam)</button>
                <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_tr_5', 30, 15, this)">15 Puan</button>
                <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_tr_5', 30, 0, this)">0 Puan</button>
              </div>
            </div>
          </div>
        </div>

        <!-- PAGE 3 & 4 -->
        <div class="pdf-interactive-page">
          <div class="page-banner" style="background:#047857;">
            <span>📄 Orijinal Öğretmen Çözüm Anahtarı - Sayfa 3 & 4</span>
            <span style="font-size:0.85rem; opacity:0.85;">Resmi Çözümler</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/img/turkce_p3.png" alt="Türkçe Cevap Sayfa 3" loading="lazy">
          </div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
            <img src="assets/img/turkce_p4.png" alt="Türkçe Cevap Sayfa 4" loading="lazy">
          </div>
        </div>

      </div>

      <div style="text-align: center; margin: 32px 0;">
        <button class="btn-start" style="padding: 16px 36px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 Türkçe Sınav Notumu Hesapla
        </button>
      </div>
    </div>

    <!-- TAB 2: SUMMARY HAP BİLGİLER -->
    <div id="summary-pane" class="tab-pane">
      <div class="summary-cards">
        <div class="summary-card">
          <h4>📖 1. Sözcükte Anlam ve Bağlam</h4>
          <ul>
            <li><strong>Gerçek Anlam:</strong> Kelimenin akla gelen ilk temel anlamıdır.</li>
            <li><strong>Mecaz Anlam:</strong> Gerçek anlamdan tamamen uzaklaşan soyut anlamdır.</li>
            <li><strong>Terim Anlam:</strong> Bilim, sanat ve spora özgü kavramlardır.</li>
          </ul>
        </div>
        <div class="summary-card">
          <h4>🎭 2. Söz Sanatları: Kişileştirme (Teşhis)</h4>
          <ul>
            <li>İnsana ait özelliklerin hayvanlara veya cansız varlıklara verilmesidir.</li>
            <li>Örnek: "Güneş bize sıcacık tebessüm ediyordu."</li>
          </ul>
        </div>
        <div class="summary-card">
          <h4>✍️ 3. Kritik Yazım Kuralları</h4>
          <ul>
            <li>Belirli tarih bildiren gün ve aylar büyük harfle başlar: <em>29 Ekim 1923, 14 Haziran Pazartesi</em>.</li>
            <li>Özel isimden sonra gelen dağ, göl, nehir isimleri büyük başlar: <em>Van Gölü, Ağrı Dağı</em>.</li>
            <li>Cadde, sokak, meydan, bulvar kelimeleri büyük harfle yazılır: <em>İstiklal Caddesi</em>.</li>
          </ul>
        </div>
      </div>
    </div>

  </main>

  {get_score_modal()}
  {get_footer()}

  <script src="assets/js/app.js"></script>
  <script>
    initLesson('turkce', 'tr-TR');
  </script>
</body>
</html>
"""

# 2. MATEMATİK
def get_matematik_html():
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>5. Sınıf Matematik 1. Dönem 1. Yazılı - Orijinal PDF Üzerinde Çalışma</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>body {{ font-family: 'Plus Jakarta Sans', system-ui, sans-serif; }}</style>
</head>
<body class="theme-mat">
  {get_header('mat')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>📐</span> Matematik 1. Dönem 1. Yazılı</h1>
        <p>Orijinal Sınav Kağıdı Üzerinde Soru Soru Sesli Çözüm • Geometrik Çizimler • Doğru Parçası • Açılar</p>
      </div>
      <div class="score-box">
        <div class="score-val" id="currentScoreVal">0</div>
        <div class="score-lbl">Mevcut Puan / 100</div>
      </div>
    </div>

    <!-- Master Audio Bar -->
    <div class="audio-bar">
      <div class="audio-bar-info">
        <div class="audio-icon-pulse">🔊</div>
        <div>
          <strong style="display:block; font-size:0.95rem;">Matematik Doğal Sesli Öğretmen Anlatımı</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır (Dinlemek için ses butonlarına dokunun)</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.playAudio('mat_summary.mp3')">📢 Sınav Konu Özetini Dinle</button>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="pdf-pane">📄 Orijinal PDF Üzerinde Çalış & Dinle</button>
      <button class="tab-btn" data-tab="summary-pane">💡 Sınavda Çıkacak Hap Bilgiler</button>
    </div>

    <!-- TAB 1: DIRECT PDF WORKBENCH -->
    <div id="pdf-pane" class="tab-pane active">
      <div class="interactive-pdf-container">
        
        <!-- PAGE 1 -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Orijinal Sınav Kağıdı - Sayfa 1 (Soru 1, Soru 2, Soru 3)</span>
            <span style="font-size:0.85rem; opacity:0.85;">1. Dönem 1. Yazılı</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/img/matematik_p1.png" alt="Matematik Sayfa 1" loading="eager">
          </div>
          <div class="pdf-question-controls">
            <!-- Q1 Controls -->
            <div class="q-strip-header">
              <div class="q-strip-title"><span>📌 Soru 1:</span> Geometrik Çizim Araçları (10 Puan)</div>
              <div class="q-strip-actions">
                <button class="btn-q-action audio-play" onclick="portalApp.playAudio('mat_q1.mp3')">🔊 Soruyu Dinle</button>
                <button class="btn-q-action" onclick="portalApp.playAudio('mat_sol1.mp3')">🎙️ Çözümü Dinle</button>
                <button class="btn-q-action solution-btn" onclick="portalApp.toggleSolution('pdf_sol_mat_1')">✅ Çözümü Aç / Kapat</button>
              </div>
            </div>
            <textarea class="student-input-box" placeholder="Pergel, gönye, iletki (açıölçer) araçlarının isimlerini ve kullanım alanlarını yazınız..."></textarea>
            <div id="pdf_sol_mat_1" class="q-solution-reveal">
              <strong>✅ Resmi Çözüm:</strong> 1. İletki (Açıölçer): Açıları ölçmeye ve çizmeye yarar. • 2. Pergel: Çember ve yay çizmek, eşit mesafeleri taşımak için kullanılır. • 3. Gönye: Dik açıları (90°) ve dik üçgenleri çizmek için kullanılır.
              <div class="self-grading">
                <span>Puan Ver:</span>
                <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_mat_1', 10, 10, this)">10 Puan (Tam)</button>
                <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_mat_1', 10, 5, this)">5 Puan</button>
                <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_mat_1', 10, 0, this)">0 Puan</button>
              </div>
            </div>

            <hr style="border:none; border-top:1px solid #e2e8f0; margin:10px 0;">

            <!-- Q2 Controls -->
            <div class="q-strip-header">
              <div class="q-strip-title"><span>📌 Soru 2:</span> Doğru, Işın ve Doğru Parçası Sembolleri (10 Puan)</div>
              <div class="q-strip-actions">
                <button class="btn-q-action audio-play" onclick="portalApp.playAudio('mat_q2.mp3')">🔊 Soruyu Dinle</button>
                <button class="btn-q-action" onclick="portalApp.playAudio('mat_sol2.mp3')">🎙️ Çözümü Dinle</button>
                <button class="btn-q-action solution-btn" onclick="portalApp.toggleSolution('pdf_sol_mat_2')">✅ Çözümü Aç / Kapat</button>
              </div>
            </div>
            <textarea class="student-input-box" placeholder="Doğru, ışın ve doğru parçası sembolik gösterimlerini yazınız..."></textarea>
            <div id="pdf_sol_mat_2" class="q-solution-reveal">
              <strong>✅ Resmi Çözüm:</strong> Doğru: Her iki yöne sonsuz [AB doğrusu], Işın: Başlangıcı sabit bir ucu sonsuz [AB ışını veya [AB), Doğru Parçası: İki ucu da kapalı [AB] veya |AB|.
              <div class="self-grading">
                <span>Puan Ver:</span>
                <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_mat_2', 10, 10, this)">10 Puan (Tam)</button>
                <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_mat_2', 10, 5, this)">5 Puan</button>
                <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_mat_2', 10, 0, this)">0 Puan</button>
              </div>
            </div>
          </div>
        </div>

        <!-- PAGE 2 -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Orijinal Sınav Kağıdı - Sayfa 2 (Soru 4 - 7)</span>
            <span style="font-size:0.85rem; opacity:0.85;">1. Dönem 1. Yazılı</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/img/matematik_p2.png" alt="Matematik Sayfa 2" loading="lazy">
          </div>
          <div class="pdf-question-controls">
            <!-- Q6 Controls -->
            <div class="q-strip-header">
              <div class="q-strip-title"><span>📌 Soru 6:</span> Tümler ve Bütünler Açılar (10 Puan)</div>
              <div class="q-strip-actions">
                <button class="btn-q-action audio-play" onclick="portalApp.playAudio('mat_q6.mp3')">🔊 Soruyu Dinle</button>
                <button class="btn-q-action" onclick="portalApp.playAudio('mat_sol6.mp3')">🎙️ Çözümü Dinle</button>
                <button class="btn-q-action solution-btn" onclick="portalApp.toggleSolution('pdf_sol_mat_6')">✅ Çözümü Aç / Kapat</button>
              </div>
            </div>
            <textarea class="student-input-box" placeholder="Tümler açı: toplamı 90 derece, Bütünler açı: toplamı 180 derece..."></textarea>
            <div id="pdf_sol_mat_6" class="q-solution-reveal">
              <strong>✅ Resmi Çözüm:</strong> Ölçüleri toplamı 90° olan iki açıya tümler açılar, ölçüleri toplamı 180° olan iki açıya bütünler açılar denir. 35 derecenin tümleri: 90 - 35 = 55°, bütünleri: 180 - 35 = 145°.
              <div class="self-grading">
                <span>Puan Ver:</span>
                <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_mat_6', 10, 10, this)">10 Puan (Tam)</button>
                <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_mat_6', 10, 5, this)">5 Puan</button>
                <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_mat_6', 10, 0, this)">0 Puan</button>
              </div>
            </div>
          </div>
        </div>

        <!-- PAGE 3 & 4 -->
        <div class="pdf-interactive-page">
          <div class="page-banner" style="background:#047857;">
            <span>📄 Orijinal Öğretmen Çözüm Anahtarı - Sayfa 3 & 4</span>
            <span style="font-size:0.85rem; opacity:0.85;">Resmi Çözümler</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/img/matematik_p3.png" alt="Matematik Cevap Sayfa 3" loading="lazy">
          </div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
            <img src="assets/img/matematik_p4.png" alt="Matematik Cevap Sayfa 4" loading="lazy">
          </div>
        </div>

      </div>

      <div style="text-align: center; margin: 32px 0;">
        <button class="btn-start" style="padding: 16px 36px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 Matematik Sınav Notumu Hesapla
        </button>
      </div>
    </div>

    <!-- TAB 2: SUMMARY HAP BİLGİLER -->
    <div id="summary-pane" class="tab-pane">
      <div class="summary-cards">
        <div class="summary-card">
          <h4>📐 1. Geometrik Çizim Araçları</h4>
          <ul>
            <li><strong>Cetvel:</strong> Düz çizgiler çizmek ve uzunluk ölçmek için kullanılır.</li>
            <li><strong>İletki (Açıölçer):</strong> Açının kaç derece olduğunu ölçmek veya belirli derecede açı çizmek için kullanılır.</li>
            <li><strong>Gönye:</strong> 90 derecelik dik açıları oluşturmak ve doğrulamak için kullanılır.</li>
            <li><strong>Pergel:</strong> Çember ve yay çizmek, uzunlukları taşımak için kullanılır.</li>
          </ul>
        </div>
        <div class="summary-card">
          <h4>📏 2. Doğru, Işın ve Doğru Parçası</h4>
          <ul>
            <li><strong>Doğru:</strong> İki ucu da sınırsız uzayan noktalar kümesi (AB doğrusu).</li>
            <li><strong>Işın:</strong> Başlangıç noktası sabit, diğer ucu sınırsız uzar [AB ışını).</li>
            <li><strong>Doğru Parçası:</strong> İki ucu da sınırlı olan çizgi [AB].</li>
          </ul>
        </div>
        <div class="summary-card">
          <h4>⚪ 3. Tümler ve Bütünler Açılar</h4>
          <ul>
            <li><strong>Tümler Açılar:</strong> Ölçüleri toplamı 90° olan iki açıdır.</li>
            <li><strong>Bütünler Açılar:</strong> Ölçüleri toplamı 180° olan iki açıdır.</li>
          </ul>
        </div>
      </div>
    </div>

  </main>

  {get_score_modal()}
  {get_footer()}

  <script src="assets/js/app.js"></script>
  <script>
    initLesson('matematik', 'tr-TR');
  </script>
</body>
</html>
"""

# 3. FEN BİLİMLERİ
def get_fen_html():
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>5. Sınıf Fen Bilimleri 1. Dönem 1. Yazılı - Orijinal PDF Üzerinde Çalışma</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>body {{ font-family: 'Plus Jakarta Sans', system-ui, sans-serif; }}</style>
</head>
<body class="theme-fen">
  {get_header('fen')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>🔬</span> Fen Bilimleri 1. Dönem 1. Yazılı</h1>
        <p>Orijinal Sınav Kağıdı Üzerinde Soru Soru Sesli Çözüm • Güneş & Ay • Ay'ın Evreleri • Dinamometre</p>
      </div>
      <div class="score-box">
        <div class="score-val" id="currentScoreVal">0</div>
        <div class="score-lbl">Mevcut Puan / 100</div>
      </div>
    </div>

    <!-- Master Audio Bar -->
    <div class="audio-bar">
      <div class="audio-bar-info">
        <div class="audio-icon-pulse">🔊</div>
        <div>
          <strong style="display:block; font-size:0.95rem;">Fen Bilimleri Doğal Sesli Öğretmen Anlatımı</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır (Dinlemek için ses butonlarına dokunun)</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.playAudio('fen_summary.mp3')">📢 Sınav Konu Özetini Dinle</button>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="pdf-pane">📄 Orijinal PDF Üzerinde Çalış & Dinle</button>
      <button class="tab-btn" data-tab="summary-pane">💡 Sınavda Çıkacak Hap Bilgiler</button>
    </div>

    <!-- TAB 1: DIRECT PDF WORKBENCH -->
    <div id="pdf-pane" class="tab-pane active">
      <div class="interactive-pdf-container">
        
        <!-- PAGE 1 -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Orijinal Sınav Kağıdı - Sayfa 1 (Soru 1, Soru 2, Soru 3)</span>
            <span style="font-size:0.85rem; opacity:0.85;">1. Dönem 1. Yazılı</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/img/fen_p1.png" alt="Fen Sayfa 1" loading="eager">
          </div>
          <div class="pdf-question-controls">
            <!-- Q1 Controls -->
            <div class="q-strip-header">
              <div class="q-strip-title"><span>📌 Soru 1:</span> Güneş'in Temel Özellikleri (10 Puan)</div>
              <div class="q-strip-actions">
                <button class="btn-q-action audio-play" onclick="portalApp.playAudio('fen_q1.mp3')">🔊 Soruyu Dinle</button>
                <button class="btn-q-action" onclick="portalApp.playAudio('fen_sol1.mp3')">🎙️ Çözümü Dinle</button>
                <button class="btn-q-action solution-btn" onclick="portalApp.toggleSolution('pdf_sol_fen_1')">✅ Çözümü Aç / Kapat</button>
              </div>
            </div>
            <textarea class="student-input-box" placeholder="Güneş'in 5 özelliğini maddeler halinde yazınız..."></textarea>
            <div id="pdf_sol_fen_1" class="q-solution-reveal">
              <strong>✅ Resmi Cevap:</strong> 1. Şekli küreseldir. 2. Sıcak gazlardan (hidrojen ve helyum) oluşur. 3. Dünyamızın ısı ve ışık kaynağıdır. 4. Dünyamıza en yakın yıldızdır. 5. Kendi ekseni etrafında saat yönünün tersine döner (yaklaşık 25 gün).
              <div class="self-grading">
                <span>Puan Ver:</span>
                <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_fen_1', 10, 10, this)">10 Puan (Tam)</button>
                <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_fen_1', 10, 5, this)">5 Puan</button>
                <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_fen_1', 10, 0, this)">0 Puan</button>
              </div>
            </div>

            <hr style="border:none; border-top:1px solid #e2e8f0; margin:10px 0;">

            <!-- Q2 Controls -->
            <div class="q-strip-header">
              <div class="q-strip-title"><span>📌 Soru 2:</span> Ay'ın Yapısı ve Yaşam Şartları (15 Puan)</div>
              <div class="q-strip-actions">
                <button class="btn-q-action audio-play" onclick="portalApp.playAudio('fen_q2.mp3')">🔊 Soruyu Dinle</button>
                <button class="btn-q-action" onclick="portalApp.playAudio('fen_sol2.mp3')">🎙️ Çözümü Dinle</button>
                <button class="btn-q-action solution-btn" onclick="portalApp.toggleSolution('pdf_sol_fen_2')">✅ Çözümü Aç / Kapat</button>
              </div>
            </div>
            <textarea class="student-input-box" placeholder="Ay'da hava olayları neden görülmez ve Ay'a giderken ne götürülmelidir?"></textarea>
            <div id="pdf_sol_fen_2" class="q-solution-reveal">
              <strong>✅ Resmi Cevap:</strong> A) Atmosfer olmadığı için rüzgâr, yağmur, kar gibi hava olayları görülmez; gece-gündüz sıcaklık farkı aşırıdır; ses iletilmez.<br>
              B) Ay'da yaşayabilmek için: Oksijen tüpü, uzay kıyafeti, su ve besin götürülmelidir.
              <div class="self-grading">
                <span>Puan Ver:</span>
                <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_fen_2', 15, 15, this)">15 Puan (Tam)</button>
                <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_fen_2', 15, 8, this)">8 Puan</button>
                <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_fen_2', 15, 0, this)">0 Puan</button>
              </div>
            </div>
          </div>
        </div>

        <!-- PAGE 2 -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Orijinal Sınav Kağıdı - Sayfa 2 (Soru 4 - 8)</span>
            <span style="font-size:0.85rem; opacity:0.85;">1. Dönem 1. Yazılı</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/img/fen_p2.png" alt="Fen Sayfa 2" loading="lazy">
          </div>
          <div class="pdf-question-controls">
            <!-- Q6 Controls -->
            <div class="q-strip-header">
              <div class="q-strip-title"><span>📌 Soru 6:</span> Dinamometre ile Kuvvet Ölçümü (15 Puan)</div>
              <div class="q-strip-actions">
                <button class="btn-q-action audio-play" onclick="portalApp.playAudio('fen_q6.mp3')">🔊 Soruyu Dinle</button>
                <button class="btn-q-action" onclick="portalApp.playAudio('fen_sol6.mp3')">🎙️ Çözümü Dinle</button>
                <button class="btn-q-action solution-btn" onclick="portalApp.toggleSolution('pdf_sol_fen_6')">✅ Çözümü Aç / Kapat</button>
              </div>
            </div>
            <textarea class="student-input-box" placeholder="Kuvvetin birimi ve dinamometredeki yay uzama ilişkisini yazınız..."></textarea>
            <div id="pdf_sol_fen_6" class="q-solution-reveal">
              <strong>✅ Resmi Cevap:</strong> Kuvvetin birimi Newton'dur (N). Dinamometre içindeki yayın uzama miktarı uygulanan kuvvetle doğru orantılıdır; kuvvet arttıkça uzama miktarı da artar.
              <div class="self-grading">
                <span>Puan Ver:</span>
                <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_fen_6', 15, 15, this)">15 Puan (Tam)</button>
                <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_fen_6', 15, 8, this)">8 Puan</button>
                <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_fen_6', 15, 0, this)">0 Puan</button>
              </div>
            </div>
          </div>
        </div>

        <!-- PAGE 3 & 4 -->
        <div class="pdf-interactive-page">
          <div class="page-banner" style="background:#047857;">
            <span>📄 Orijinal Öğretmen Çözüm Anahtarı - Sayfa 3 & 4</span>
            <span style="font-size:0.85rem; opacity:0.85;">Resmi Çözümler</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/img/fen_p3.png" alt="Fen Cevap Sayfa 3" loading="lazy">
          </div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
            <img src="assets/img/fen_p4.png" alt="Fen Cevap Sayfa 4" loading="lazy">
          </div>
        </div>

      </div>

      <div style="text-align: center; margin: 32px 0;">
        <button class="btn-start" style="padding: 16px 36px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 Fen Bilimleri Sınav Notumu Hesapla
        </button>
      </div>
    </div>

    <!-- TAB 2: SUMMARY HAP BİLGİLER -->
    <div id="summary-pane" class="tab-pane">
      <div class="summary-cards">
        <div class="summary-card">
          <h4>☀️ 1. Güneş'in Özellikleri</h4>
          <ul>
            <li>Şekli küreseldir, hidrojen ve helyum gazlarından oluşur.</li>
            <li>Dünyamızın temel ısı ve ışık kaynağıdır.</li>
            <li>Kendi ekseni etrafında saat yönünün tersine 25 günde döner.</li>
          </ul>
        </div>
        <div class="summary-card">
          <h4>🌑 2. Ay'ın Yapısı ve Evreleri</h4>
          <ul>
            <li>Ay'ın atmosferi yok denecek kadar azdır, hava olayları yaşanmaz.</li>
            <li>Dünya'dan Ay'ın hep aynı yüzü görünür çünkü kendi etrafında dönme süresi ile Dünya etrafında dolanma süresi eşittir (yaklaşık 27 gün).</li>
            <li>Ana Evreler: Yeni Ay, İlk Dördün, Dolunay, Son Dördün.</li>
          </ul>
        </div>
        <div class="summary-card">
          <h4>⚖️ 3. Dinamometre</h4>
          <ul>
            <li>Kuvvet dinamometre ile ölçülür, birimi Newton'dur (N).</li>
            <li>Hassas ölçüm için ince yaylı, büyük kuvvetler için kalın yaylı dinamometre seçilir.</li>
          </ul>
        </div>
      </div>
    </div>

  </main>

  {get_score_modal()}
  {get_footer()}

  <script src="assets/js/app.js"></script>
  <script>
    initLesson('fen', 'tr-TR');
  </script>
</body>
</html>
"""

# 4. SOSYAL BİLGİLER
def get_sosyal_html():
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>5. Sınıf Sosyal Bilgiler 1. Dönem 1. Yazılı - Orijinal PDF Üzerinde Çalışma</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>body {{ font-family: 'Plus Jakarta Sans', system-ui, sans-serif; }}</style>
</head>
<body class="theme-sosyal">
  {get_header('sosyal')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>🌍</span> Sosyal Bilgiler 1. Dönem 1. Yazılı</h1>
        <p>Orijinal Sınav Kağıdı Üzerinde Soru Soru Sesli Çözüm • Hak & Sorumluluk • Çocuk Hakları • Uygarlıklar</p>
      </div>
      <div class="score-box">
        <div class="score-val" id="currentScoreVal">0</div>
        <div class="score-lbl">Mevcut Puan / 100</div>
      </div>
    </div>

    <!-- Master Audio Bar -->
    <div class="audio-bar">
      <div class="audio-bar-info">
        <div class="audio-icon-pulse">🔊</div>
        <div>
          <strong style="display:block; font-size:0.95rem;">Sosyal Bilgiler Doğal Sesli Öğretmen Anlatımı</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır (Dinlemek için ses butonlarına dokunun)</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.playAudio('sosyal_summary.mp3')">📢 Sınav Konu Özetini Dinle</button>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="pdf-pane">📄 Orijinal PDF Üzerinde Çalış & Dinle</button>
      <button class="tab-btn" data-tab="summary-pane">💡 Sınavda Çıkacak Hap Bilgiler</button>
    </div>

    <!-- TAB 1: DIRECT PDF WORKBENCH -->
    <div id="pdf-pane" class="tab-pane active">
      <div class="interactive-pdf-container">
        
        <!-- PAGE 1 -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Orijinal Sınav Kağıdı - Sayfa 1 (Soru 1, Soru 2, Soru 3)</span>
            <span style="font-size:0.85rem; opacity:0.85;">1. Dönem 1. Yazılı</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/img/sosyal_p1.png" alt="Sosyal Bilgiler Sayfa 1" loading="eager">
          </div>
          <div class="pdf-question-controls">
            <!-- Q1 Controls -->
            <div class="q-strip-header">
              <div class="q-strip-title"><span>📌 Soru 1:</span> Hak ve Sorumluluk İlişkisi (20 Puan)</div>
              <div class="q-strip-actions">
                <button class="btn-q-action audio-play" onclick="portalApp.playAudio('sosyal_q1.mp3')">🔊 Soruyu Dinle</button>
                <button class="btn-q-action" onclick="portalApp.playAudio('sosyal_sol1.mp3')">🎙️ Çözümü Dinle</button>
                <button class="btn-q-action solution-btn" onclick="portalApp.toggleSolution('pdf_sol_sos_1')">✅ Çözümü Aç / Kapat</button>
              </div>
            </div>
            <textarea class="student-input-box" placeholder="Hak ve sorumluluk arasındaki farkı örneklerle yazınız..."></textarea>
            <div id="pdf_sol_sos_1" class="q-solution-reveal">
              <strong>✅ Resmi Cevap:</strong> Hak: Kanunların ve toplumun bireye tanıdığı yetkidir (örneğin eğitim alma, sağlık hakkı). Sorumluluk ise bireyin üzerine düşen görevleri yerine getirmesidir (ödevlerini yapmak, dersi dinlemek).
              <div class="self-grading">
                <span>Puan Ver:</span>
                <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_sos_1', 20, 20, this)">20 Puan (Tam)</button>
                <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_sos_1', 20, 10, this)">10 Puan</button>
                <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_sos_1', 20, 0, this)">0 Puan</button>
              </div>
            </div>

            <hr style="border:none; border-top:1px solid #e2e8f0; margin:10px 0;">

            <!-- Q2 Controls -->
            <div class="q-strip-header">
              <div class="q-strip-title"><span>📌 Soru 2:</span> Çocuk Hakları Sözleşmesi (20 Puan)</div>
              <div class="q-strip-actions">
                <button class="btn-q-action audio-play" onclick="portalApp.playAudio('sosyal_q2.mp3')">🔊 Soruyu Dinle</button>
                <button class="btn-q-action" onclick="portalApp.playAudio('sosyal_sol2.mp3')">🎙️ Çözümü Dinle</button>
                <button class="btn-q-action solution-btn" onclick="portalApp.toggleSolution('pdf_sol_sos_2')">✅ Çözümü Aç / Kapat</button>
              </div>
            </div>
            <textarea class="student-input-box" placeholder="18 yaşına kadar her bireyin çocuk sayılması ve temel haklarını yazınız..."></textarea>
            <div id="pdf_sol_sos_2" class="q-solution-reveal">
              <strong>✅ Resmi Cevap:</strong> 18 yaşına kadar her birey çocuk sayılır. Yaşama, sağlıklı bir çevrede büyüme, eğitim alma, oyun oynama ve fikirlerini özgürce ifade etme temel haklarındandır.
              <div class="self-grading">
                <span>Puan Ver:</span>
                <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_sos_2', 20, 20, this)">20 Puan (Tam)</button>
                <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_sos_2', 20, 10, this)">10 Puan</button>
                <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_sos_2', 20, 0, this)">0 Puan</button>
              </div>
            </div>
          </div>
        </div>

        <!-- PAGE 2 -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Orijinal Sınav Kağıdı - Sayfa 2 (Soru 4, Soru 5)</span>
            <span style="font-size:0.85rem; opacity:0.85;">1. Dönem 1. Yazılı</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/img/sosyal_p2.png" alt="Sosyal Bilgiler Sayfa 2" loading="lazy">
          </div>
          <div class="pdf-question-controls">
            <!-- Q5 Controls -->
            <div class="q-strip-header">
              <div class="q-strip-title"><span>📌 Soru 5:</span> Tarihi Eserler ve Doğal Varlıklar (20 Puan)</div>
              <div class="q-strip-actions">
                <button class="btn-q-action audio-play" onclick="portalApp.playAudio('sosyal_q5.mp3')">🔊 Soruyu Dinle</button>
                <button class="btn-q-action" onclick="portalApp.playAudio('sosyal_sol5.mp3')">🎙️ Çözümü Dinle</button>
                <button class="btn-q-action solution-btn" onclick="portalApp.toggleSolution('pdf_sol_sos_5')">✅ Çözümü Aç / Kapat</button>
              </div>
            </div>
            <textarea class="student-input-box" placeholder="Tarihi eser ve doğal varlık farkını açıklayıp örnekler veriniz..."></textarea>
            <div id="pdf_sol_sos_5" class="q-solution-reveal">
              <strong>✅ Resmi Cevap:</strong> Doğal Varlık: Doğada kendiliğinden insan eli değmeden oluşan güzelliklerdir (Pamukkale Travertenleri, Düden Şelalesi, Peri Bacaları). Tarihi Eser: Geçmiş uygarlıklar tarafından inşa edilen yapay mirastır (Topkapı Sarayı, Efes Antik Kenti, Selimiye Camii).
              <div class="self-grading">
                <span>Puan Ver:</span>
                <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_sos_5', 20, 20, this)">20 Puan (Tam)</button>
                <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_sos_5', 20, 10, this)">10 Puan</button>
                <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_sos_5', 20, 0, this)">0 Puan</button>
              </div>
            </div>
          </div>
        </div>

        <!-- PAGE 3 & 4 -->
        <div class="pdf-interactive-page">
          <div class="page-banner" style="background:#047857;">
            <span>📄 Orijinal Öğretmen Çözüm Anahtarı - Sayfa 3 & 4</span>
            <span style="font-size:0.85rem; opacity:0.85;">Resmi Çözümler</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/img/sosyal_p3.png" alt="Sosyal Bilgiler Cevap Sayfa 3" loading="lazy">
          </div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
            <img src="assets/img/sosyal_p4.png" alt="Sosyal Bilgiler Cevap Sayfa 4" loading="lazy">
          </div>
        </div>

      </div>

      <div style="text-align: center; margin: 32px 0;">
        <button class="btn-start" style="padding: 16px 36px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 Sosyal Bilgiler Sınav Notumu Hesapla
        </button>
      </div>
    </div>

    <!-- TAB 2: SUMMARY HAP BİLGİLER -->
    <div id="summary-pane" class="tab-pane">
      <div class="summary-cards">
        <div class="summary-card">
          <h4>👥 1. Roller, Haklar ve Sorumluluklar</h4>
          <ul>
            <li>Bir kişi aynı anda birden fazla gruba dahil olabilir (ailede çocuk, okulda öğrenci, takımda kaleci).</li>
            <li>Her rolün getirdiği farklı haklar ve sorumluluklar vardır.</li>
          </ul>
        </div>
        <div class="summary-card">
          <h4>🕊️ 2. Çocuk Hakları Sözleşmesi</h4>
          <ul>
            <li>UNICEF tarafından desteklenir ve 18 yaş altındaki her bireyi kapsar.</li>
            <li>Hiçbir ayrım gözetmeksizin tüm çocuklar eşit haklara sahiptir.</li>
          </ul>
        </div>
      </div>
    </div>

  </main>

  {get_score_modal()}
  {get_footer()}

  <script src="assets/js/app.js"></script>
  <script>
    initLesson('sosyal', 'tr-TR');
  </script>
</body>
</html>
"""

# 5. DİN KÜLTÜRÜ
def get_din_html():
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>5. Sınıf Din Kültürü 1. Dönem 1. Yazılı - Orijinal PDF Üzerinde Çalışma</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>body {{ font-family: 'Plus Jakarta Sans', system-ui, sans-serif; }}</style>
</head>
<body class="theme-din">
  {get_header('din')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>🕌</span> Din Kültürü ve Ahlak Bilgisi 1. Dönem 1. Yazılı</h1>
        <p>Orijinal Sınav Kağıdı Üzerinde Soru Soru Sesli Çözüm • Allah İnancı • Evrendeki Düzen • İhlas Suresi</p>
      </div>
      <div class="score-box">
        <div class="score-val" id="currentScoreVal">0</div>
        <div class="score-lbl">Mevcut Puan / 100</div>
      </div>
    </div>

    <!-- Master Audio Bar -->
    <div class="audio-bar">
      <div class="audio-bar-info">
        <div class="audio-icon-pulse">🔊</div>
        <div>
          <strong style="display:block; font-size:0.95rem;">Din Kültürü Doğal Sesli Öğretmen Anlatımı</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır (Dinlemek için ses butonlarına dokunun)</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.playAudio('din_summary.mp3')">📢 Sınav Konu Özetini Dinle</button>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="pdf-pane">📄 Orijinal PDF Üzerinde Çalış & Dinle</button>
      <button class="tab-btn" data-tab="summary-pane">💡 Sınavda Çıkacak Hap Bilgiler</button>
    </div>

    <!-- TAB 1: DIRECT PDF WORKBENCH -->
    <div id="pdf-pane" class="tab-pane active">
      <div class="interactive-pdf-container">
        
        <!-- PAGE 1 -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Orijinal Sınav Kağıdı - Sayfa 1 & 2 (Sorular & Boşluk Doldurma)</span>
            <span style="font-size:0.85rem; opacity:0.85;">1. Dönem 1. Yazılı</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/img/din_p1.png" alt="Din Kültürü Sayfa 1" loading="eager">
          </div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
            <img src="assets/img/din_p2.png" alt="Din Kültürü Sayfa 2" loading="lazy">
          </div>
          <div class="pdf-question-controls">
            <!-- Q1 Controls -->
            <div class="q-strip-header">
              <div class="q-strip-title"><span>📌 Soru 1:</span> Evrendeki Ölçü ve Düzen (20 Puan)</div>
              <div class="q-strip-actions">
                <button class="btn-q-action audio-play" onclick="portalApp.playAudio('din_q1.mp3')">🔊 Soruyu Dinle</button>
                <button class="btn-q-action" onclick="portalApp.playAudio('din_sol1.mp3')">🎙️ Çözümü Dinle</button>
                <button class="btn-q-action solution-btn" onclick="portalApp.toggleSolution('pdf_sol_din_1')">✅ Çözümü Aç / Kapat</button>
              </div>
            </div>
            <textarea class="student-input-box" placeholder="Allah'ın evreni bir ölçü ve düzen içinde yarattığına dair 3 örnek veriniz..."></textarea>
            <div id="pdf_sol_din_1" class="q-solution-reveal">
              <strong>✅ Resmi Cevap:</strong> 1. Gece ve gündüzün ardı ardına gelmesi, 2. Mevsimlerin kusursuz bir sırayla birbirini takip etmesi, 3. Güneş sistemindeki gezegenlerin birbirine çarpmadan yörüngelerinde dönmesi, 4. Canlıların solunum için oksijene olan dengesi.
              <div class="self-grading">
                <span>Puan Ver:</span>
                <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_din_1', 20, 20, this)">20 Puan (Tam)</button>
                <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_din_1', 20, 10, this)">10 Puan</button>
                <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_din_1', 20, 0, this)">0 Puan</button>
              </div>
            </div>
          </div>
        </div>

        <!-- PAGE 3 & 4 (Official Answers) -->
        <div class="pdf-interactive-page">
          <div class="page-banner" style="background:#047857;">
            <span>📄 Orijinal Öğretmen Çözüm Anahtarı - Sayfa 3, 4 & 5</span>
            <span style="font-size:0.85rem; opacity:0.85;">Resmi Çözümler</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/img/din_p3.png" alt="Din Kültürü Cevap Sayfa 3" loading="lazy">
          </div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
            <img src="assets/img/din_p4.png" alt="Din Kültürü Cevap Sayfa 4" loading="lazy">
          </div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
            <img src="assets/img/din_p5.png" alt="Din Kültürü Cevap Sayfa 5" loading="lazy">
          </div>
        </div>

      </div>

      <div style="text-align: center; margin: 32px 0;">
        <button class="btn-start" style="padding: 16px 36px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 Din Kültürü Sınav Notumu Hesapla
        </button>
      </div>
    </div>

    <!-- TAB 2: SUMMARY HAP BİLGİLER -->
    <div id="summary-pane" class="tab-pane">
      <div class="summary-cards">
        <div class="summary-card">
          <h4>🌌 1. Evrendeki Mükemmel Uyum</h4>
          <ul>
            <li>Evrendeki her şey bir ölçü, düzen ve ahenk içinde yaratılmıştır (Kamer Suresi, 49. ayet).</li>
            <li>Su döngüsü, yer çekimi kanunu ve atmosferin koruyucu kalkanı bu düzenin kanıtlarıdır.</li>
          </ul>
        </div>
        <div class="summary-card">
          <h4>📖 2. İhlas Suresi ve Tevhit</h4>
          <ul>
            <li>Tevhit: Allah'ın bir ve tek olduğuna, hiçbir denginin bulunmadığına inanmaktır.</li>
            <li>İhlas Suresi tevhidi en özlü anlatan suredir: "De ki: O Allah tektir. Samed'dir. Doğurmamış ve doğmamıştır."</li>
          </ul>
        </div>
      </div>
    </div>

  </main>

  {get_score_modal()}
  {get_footer()}

  <script src="assets/js/app.js"></script>
  <script>
    initLesson('din', 'tr-TR');
  </script>
</body>
</html>
"""

# 6. İNGİLİZCE
def get_ingilizce_html():
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>5. Sınıf İngilizce 1. Dönem 1. Yazılı - Orijinal PDF Üzerinde Çalışma</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>body {{ font-family: 'Plus Jakarta Sans', system-ui, sans-serif; }}</style>
</head>
<body class="theme-ingilizce">
  {get_header('ingilizce')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>🇬🇧</span> İngilizce 1. Dönem 1. Yazılı</h1>
        <p>Orijinal Sınav Kağıdı Üzerinde Soru Soru Sesli Çözüm • Hello! Unit • School Subjects • Nationalities</p>
      </div>
      <div class="score-box">
        <div class="score-val" id="currentScoreVal">0</div>
        <div class="score-lbl">Mevcut Puan / 100</div>
      </div>
    </div>

    <!-- Master Audio Bar -->
    <div class="audio-bar">
      <div class="audio-bar-info">
        <div class="audio-icon-pulse">🔊</div>
        <div>
          <strong style="display:block; font-size:0.95rem;">English Teacher Studio Audio (Native Pronunciation)</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Ready (Click audio buttons to listen)</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.playAudio('ing_summary.mp3')">📢 Listen Unit Summary</button>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="pdf-pane">📄 Orijinal PDF Üzerinde Çalış & Dinle</button>
      <button class="tab-btn" data-tab="summary-pane">💡 Sınavda Çıkacak Hap Bilgiler</button>
    </div>

    <!-- TAB 1: DIRECT PDF WORKBENCH -->
    <div id="pdf-pane" class="tab-pane active">
      <div class="interactive-pdf-container">
        
        <!-- PAGE 1 & 2 -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Original Exam Paper - Page 1 & 2 (Questions & Exercises)</span>
            <span style="font-size:0.85rem; opacity:0.85;">1st Term 1st Exam</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/img/ingilizce_p1.png" alt="İngilizce Sayfa 1" loading="eager">
          </div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
            <img src="assets/img/ingilizce_p2.png" alt="İngilizce Sayfa 2" loading="lazy">
          </div>
          <div class="pdf-question-controls">
            <!-- Q1 Controls -->
            <div class="q-strip-header">
              <div class="q-strip-title"><span>📌 Exercise 1:</span> School Subjects & Nationalities (20 Points)</div>
              <div class="q-strip-actions">
                <button class="btn-q-action audio-play" onclick="portalApp.playAudio('ing_q1.mp3')">🔊 Listen Question</button>
                <button class="btn-q-action" onclick="portalApp.playAudio('ing_sol1.mp3')">🎙️ Listen Solution</button>
                <button class="btn-q-action solution-btn" onclick="portalApp.toggleSolution('pdf_sol_ing_1')">✅ Open / Close Solution</button>
              </div>
            </div>
            <textarea class="student-input-box" placeholder="Write your answers here (e.g., Maths, Science, History, Turkish, English)..."></textarea>
            <div id="pdf_sol_ing_1" class="q-solution-reveal">
              <strong>✅ Official Answer Key:</strong> 1. Maths (Matematik), 2. Science (Fen Bilimleri), 3. Social Studies (Sosyal Bilgiler), 4. Art (Görsel Sanatlar), 5. P.E. (Physical Education - Beden Eğitimi). Country: Turkey -> Nationality: Turkish. Country: England -> Nationality: English.
              <div class="self-grading">
                <span>Puan Ver:</span>
                <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_ing_1', 20, 20, this)">20 Points (Full)</button>
                <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_ing_1', 20, 10, this)">10 Points</button>
                <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_ing_1', 20, 0, this)">0 Points</button>
              </div>
            </div>
          </div>
        </div>

        <!-- PAGE 3 - 7 (Answer Key & Full Booklet) -->
        <div class="pdf-interactive-page">
          <div class="page-banner" style="background:#047857;">
            <span>📄 Official Teacher Answer Key Pages (Pages 3 - 7)</span>
            <span style="font-size:0.85rem; opacity:0.85;">Official Solutions</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/img/ingilizce_p3.png" alt="İngilizce Sayfa 3" loading="lazy">
          </div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
            <img src="assets/img/ingilizce_p4.png" alt="İngilizce Sayfa 4" loading="lazy">
          </div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
            <img src="assets/img/ingilizce_p5.png" alt="İngilizce Sayfa 5" loading="lazy">
          </div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
            <img src="assets/img/ingilizce_p6.png" alt="İngilizce Sayfa 6" loading="lazy">
          </div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
            <img src="assets/img/ingilizce_p7.png" alt="İngilizce Sayfa 7" loading="lazy">
          </div>
        </div>

      </div>

      <div style="text-align: center; margin: 32px 0;">
        <button class="btn-start" style="padding: 16px 36px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 İngilizce Sınav Notumu Hesapla
        </button>
      </div>
    </div>

    <!-- TAB 2: SUMMARY HAP BİLGİLER -->
    <div id="summary-pane" class="tab-pane">
      <div class="summary-cards">
        <div class="summary-card">
          <h4>🏫 1. School Subjects</h4>
          <ul>
            <li><strong>Maths:</strong> Numbers and calculations.</li>
            <li><strong>Science:</strong> Experiments, nature and planets.</li>
            <li><strong>Social Studies:</strong> History and geography.</li>
            <li><strong>Art:</strong> Drawing and painting.</li>
            <li><strong>Physical Education (P.E.):</strong> Sports and gymnastics.</li>
          </ul>
        </div>
        <div class="summary-card">
          <h4>🌍 2. Countries & Nationalities</h4>
          <ul>
            <li>Where are you from? -> I am from Turkey. (Country)</li>
            <li>What nationality are you? -> I am Turkish. (Nationality)</li>
            <li>Germany -> German, Spain -> Spanish, France -> French.</li>
          </ul>
        </div>
      </div>
    </div>

  </main>

  {get_score_modal()}
  {get_footer()}

  <script src="assets/js/app.js"></script>
  <script>
    initLesson('ingilizce', 'en-US');
  </script>
</body>
</html>
"""

# Write all pages
pages = {
    'turkce.html': get_turkce_html(),
    'matematik.html': get_matematik_html(),
    'fen-bilimleri.html': get_fen_html(),
    'sosyal-bilgiler.html': get_sosyal_html(),
    'din-kulturu.html': get_din_html(),
    'ingilizce.html': get_ingilizce_html()
}

out_dir = r"d:\gpt\5_sinif_calisma_portali"
for name, content in pages.items():
    filepath = os.path.join(out_dir, name)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Written:", name)

print("All modern workbench pages generated successfully!")
