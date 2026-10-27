# -*- coding: utf-8 -*-
"""
Generate ultra-modern, interactive direct-PDF-study subject pages for 5th Grade Study Portal.
Directly studies on original PDF pages with audio, hints, official answers, and scoring.
"""

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

# ----------------- TÜRKÇE -----------------
def generate_turkce():
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
      <button class="tab-btn active" data-tab="pdf-pane">📄 Orijinal PDF Üzerinde Çalış</button>
      <button class="tab-btn" data-tab="questions-pane">📝 Soru Soru Detaylı Çözümler</button>
      <button class="tab-btn" data-tab="summary-pane">💡 Sınavda Çıkacak Hap Bilgiler</button>
    </div>

    <!-- TAB 1: DIRECT PDF WORKBENCH -->
    <div id="pdf-pane" class="tab-pane active">
      <div class="interactive-pdf-container">
        
        <!-- PAGE 1: Soru 1, 2, 3 -->
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

        <!-- PAGE 2: Soru 4, 5 -->
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
              <strong>✅ Örnek Cevap:</strong> 1. "Rüzgâr gece boyunca pencerelere kızgın kızgın vurdu." • 2. "Güneş sabah yüzünü gösterdiğinde çiçekler sevinçle gülümsedi." İnsana ait duygular doğaya aktarılmıştır.
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
            <textarea class="student-input-box" placeholder="I. Tarih kuralı cümlesi, II. Yer adı kuralı cümlesi, III. Cadde/Sokak cümlesi..."></textarea>
            <div id="pdf_sol_tr_5" class="q-solution-reveal">
              <strong>✅ Örnek Cümleler:</strong><br>
              I: "Kardeşim <strong>12 Mayıs 2018 Cumartesi</strong> günü doğdu." (Belirli gün ve ay adı büyük)<br>
              II: "Tatilimizi <strong>Van Gölü</strong> çevresinde geçirdik." (Coğrafi tür adı büyük)<br>
              III: "Teyzem <strong>Atatürk Bulvarı, Menekşe Sokak</strong>ta oturuyor." (Bulvar ve sokak büyük)
              <div class="self-grading">
                <span>Puan Ver:</span>
                <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_tr_5', 30, 30, this)">30 Puan (Tam)</button>
                <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_tr_5', 30, 15, this)">15 Puan</button>
                <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_tr_5', 30, 0, this)">0 Puan</button>
              </div>
            </div>
          </div>
        </div>

        <!-- PAGE 3 & 4: OFFICIAL ANSWER KEY PAGES -->
        <div class="pdf-interactive-page">
          <div class="page-banner" style="background:#047857;">
            <span>📄 Orijinal Öğretmen Cevap Anahtarı - Sayfa 3 & 4</span>
            <span style="font-size:0.85rem; opacity:0.85;">Resmi Çözümler</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/img/turkce_p3.png" alt="Türkçe Cevap Anahtarı Sayfa 3" loading="lazy">
          </div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
            <img src="assets/img/turkce_p4.png" alt="Türkçe Cevap Anahtarı Sayfa 4" loading="lazy">
          </div>
        </div>

      </div>

      <div style="text-align: center; margin: 32px 0;">
        <button class="btn-start" style="padding: 16px 36px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 Türkçe Sınav Notumu Hesapla
        </button>
      </div>
    </div>

    <!-- TAB 2: DETAILED QUESTION CARDS -->
    <div id="questions-pane" class="tab-pane">
      <div class="question-card" id="q_tr_c1">
        <div class="q-header"><span class="q-badge">Soru 1 • Sözcükte Anlam</span><span class="q-points">15 Puan</span></div>
        <div class="q-text">
          Pusula metnindeki tanımdan hareketle şu sözcükleri tespit ediniz: 1. Buluş (İcat), 2. Tallı su/kaya bitkisi (Yosun), 3. Demiri çeken oksit (Mıknatıs).
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('turkce_q1.mp3')">🔊 Soruyu Dinle</button>
          <button class="btn-q" onclick="portalApp.playAudio('turkce_sol1.mp3')">🎙️ Çözüm Sesini Dinle</button>
          <button class="btn-q" onclick="portalApp.toggleSolution('sol_card_1')">✅ Çözüm Metnini Gör</button>
        </div>
        <div id="sol_card_1" class="solution-box">
          <strong>Resmi Çözüm:</strong> 1: İcat, 2: Yosun, 3: Mıknatıs.
        </div>
      </div>

      <div class="question-card" id="q_tr_c2">
        <div class="q-header"><span class="q-badge">Soru 2 • Ana Fikir & Konu</span><span class="q-points">20 Puan</span></div>
        <div class="q-text">
          Yapay zeka sistemlerinin enerji ve yüksek su tüketimini ele alan metnin konusunu ve ana fikrini yazınız.
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('turkce_q2.mp3')">🔊 Soruyu Dinle</button>
          <button class="btn-q" onclick="portalApp.playAudio('turkce_sol2.mp3')">🎙️ Çözüm Sesini Dinle</button>
          <button class="btn-q" onclick="portalApp.toggleSolution('sol_card_2')">✅ Çözüm Metnini Gör</button>
        </div>
        <div id="sol_card_2" class="solution-box">
          <strong>Resmi Çözüm:</strong> Konu: Yapay zekanın elektrik ve su sarfiyatı. Ana Fikir: Teknoloji geliştirilirken çevre dengesi korunmalıdır.
        </div>
      </div>
    </div>

    <!-- TAB 3: SUMMARY HAP BİLGİLER -->
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

# Let's write the generator runner
with open(r'd:\gpt\5_sinif_calisma_portali\generate_modern_pages.py', 'w', encoding='utf-8') as f:
    f.write('''# -*- coding: utf-8 -*-
import os

from build_portal import build_fen, build_mat, build_sosyal, build_din, build_ingilizce
''')
print("Base helper created!")
