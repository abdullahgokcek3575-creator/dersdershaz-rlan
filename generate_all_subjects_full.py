# -*- coding: utf-8 -*-
"""
Generate complete interactive HTML subject pages where EVERY question is fully solved,
answers can be typed in responsive inputs under each question on the PDF,
and hybrid audio works on PC, Mobile, Smart TV and Tablets.
"""

import os, sys

def get_header(active_tab="home"):
    links = [
        ("index.html", "🏠 Ana Sayfa", "home"),
        ("turkce.html", "📚 5. Sınıf Türkçe", "turkce"),
        ("matematik.html", "📐 5. Sınıf Matematik", "mat"),
        ("fen-bilimleri.html", "🔬 5. Sınıf Fen", "fen"),
        ("sosyal-bilgiler.html", "🌍 5. Sınıf Sosyal", "sosyal"),
        ("din-kulturu.html", "🕌 5. Sınıf Din", "din"),
        ("ingilizce.html", "🇬🇧 5. Sınıf İngilizce", "ingilizce"),
        ("mebi-sorulari.html", "⭐ 7. Sınıf MEBİ Yazılıları", "mebi"),
        ("qr_giris.html", "📱 Ağ / TV Giriş", "qr"),
    ]
    nav_html = ""
    for href, title, key in links:
        act = " active" if key == active_tab else ""
        nav_html += f'<a href="{href}" class="nav-link{act}">{title}</a>\n'
    return f"""
    <header class="site-header">
      <div class="nav-bar">
        <a href="index.html" class="brand-link">
          <span class="brand-badge">AKILLI PORTAL</span>
          <span>Etkileşimli Yazılı Hazırlık</span>
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
        <p style="font-weight: 700; color: #1e293b; font-size: 1rem;">Akıllı Yazılıya Hazırlık Portalı</p>
        <p style="margin-top: 4px;">Tüm Sorular Çözümlü • PDF Üzerinde Doğrudan Çalışma • Mobil, Bilgisayar, Tablet ve Smart TV Uyumlu</p>
        <p style="margin-top: 8px; font-size: 0.82rem; color: #94a3b8;">Her Hakkı Saklıdır</p>
      </div>
    </footer>
    """

def get_score_modal():
    return """
    <div id="scoreModal" class="modal-overlay">
      <div class="modal-content">
        <h2>🎉 Sınav Çalışması Tamamlandı!</h2>
        <div class="modal-score" id="finalScoreVal">100</div>
        <p style="font-weight: 700; color: #64748b; margin-bottom: 12px;">Toplam Puan / 100</p>
        <p id="scoreFeedback" style="font-size: 1.05rem; line-height: 1.5; color: #334155;">Harika bir çalışma gerçekleştirdin!</p>
        <button class="btn-modal" onclick="portalApp.closeModal()">Kapat ve İncelemeye Devam Et</button>
      </div>
    </div>
    """

def build_q_strip(q_num, title, points, q_audio, sol_audio, q_speak_text, sol_speak_text, solution_html, placeholder="Cevabını buraya yaz..."):
    # escape quotes for onclick
    q_speak_esc = q_speak_text.replace("'", "\\'").replace('"', '&quot;')
    sol_speak_esc = sol_speak_text.replace("'", "\\'").replace('"', '&quot;')
    sol_id = f"sol_reveal_{q_num}"

    return f"""
    <div class="q-strip" id="q_strip_{q_num}">
      <div class="q-strip-header">
        <div class="q-strip-title">
          <span class="q-num-badge">Soru {q_num}</span>
          <strong>{title}</strong>
          <span class="q-pts-pill">{points} Puan</span>
        </div>
        <div class="q-strip-actions">
          <button class="btn-q-action audio-play" onclick="portalApp.playAudio('{q_audio}', 'q_strip_{q_num}', '{q_speak_esc}')">🔊 Soruyu Dinle</button>
          <button class="btn-q-action audio-sol" onclick="portalApp.playAudio('{sol_audio}', 'q_strip_{q_num}', '{sol_speak_esc}')">🎙️ Çözümü Dinle</button>
          <button class="btn-q-action solution-btn" onclick="portalApp.toggleSolution('{sol_id}')">✅ Çözümü Aç / Kapat</button>
        </div>
      </div>
      <textarea class="student-input-box" placeholder="{placeholder}"></textarea>
      <div id="{sol_id}" class="q-solution-reveal">
        <div class="sol-title">📌 Öğretmen Çözümü & Model Cevap:</div>
        <div class="sol-body">{solution_html}</div>
        <div class="self-grading">
          <span>Bu sorudan aldığın puan:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_{q_num}', {points}, {points}, this)">{points} Puan (Tam Doğru)</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_{q_num}', {points}, {points//2}, this)">{points//2} Puan (Kısmi)</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_{q_num}', {points}, 0, this)">0 Puan</button>
        </div>
      </div>
    </div>
    """

# =========================================================================
# 1. TÜRKÇE (Sorular: 1, 2, 3, 4, 5, 6 - Toplam 100 Puan)
# =========================================================================
def generate_turkce():
    q1 = build_q_strip(
        1, "Pusula Metninden Sözcük Bulma", 15,
        "turkce_q1.mp3", "turkce_sol1.mp3",
        "Soru 1. Pusula metninde geçen; buluş, yosun ve mıknatıs tanımlarına karşılık gelen sözcükleri yazınız.",
        "Soru 1'in çözümü. 1: İcat, 2: Yosun, 3: Mıknatıs.",
        "1. <strong>İcat</strong> (Bilinmeyen yeni bir bulguya ulaşma, buluş)<br>2. <strong>Yosun</strong> (Suda veya taşların üzerinde yetişen ilkel bitkiler)<br>3. <strong>Mıknatıs</strong> (Demiri çeken oksit; demirkapan)",
        "1: İcat, 2: Yosun, 3: Mıknatıs..."
    )

    q2 = build_q_strip(
        2, "Yapay Zeka ve Çevre Metninden Sonuç Çıkarma", 20,
        "turkce_q2.mp3", "turkce_sol2.mp3",
        "Soru 2. Yapay zekânın çevre üzerindeki elektrik ve su tüketimi etkisini anlatan metinden çıkardığınız sonucu yazınız.",
        "Soru 2'nin çözümü. Yapay zeka teknolojileri kullanılırken su ve enerji israfını önlemek için net ve doğrudan ifadeler kullanılmalıdır.",
        "<strong>Metinden Çıkarılan Sonuç:</strong><br>Yapay zekâ sunucularının soğutulması yüksek miktarda su ve elektrik tüketimine neden olur. Bu yüzden gereksiz uzun sohbetlerden kaçınmalı, yapay zekâya doğrudan ve net komutlar vererek doğal kaynakların israfını önlemeliyiz.",
        "Metinden çıkardığınız sonucu kendi cümlelerinizle yazınız..."
    )

    q3 = build_q_strip(
        3, "Satranç Metninin Anahtar Kelimeleri", 15,
        "turkce_q3.mp3", "turkce_sol3.mp3",
        "Soru 3. Satrancın zihinsel gelişime faydalarını anlatan metnin anahtar kelimelerini belirleyerek iki tanesini yazınız.",
        "Soru 3'ün çözümü. Anahtar kelimeler: Satranç, zihinsel gelişim, planlama veya strateji.",
        "<strong>Anahtar Kelimeler:</strong><br>• <strong>Satranç</strong><br>• <strong>Zihinsel / Bilişsel Gelişim</strong> (veya: <em>Stratejik Düşünme, Planlama</em> kabul edilir).",
        "İki anahtar kelime yazınız (Örn: Satranç, Zihinsel gelişim)..."
    )

    q4 = build_q_strip(
        4, "Söz Sanatları: Kişileştirmeye İki Örnek", 15,
        "turkce_q4.mp3", "turkce_sol4.mp3",
        "Soru 4. İnsana ait özelliklerin doğaya veya cansız varlıklara aktarıldığı kişileştirme sanatına iki örnek veriniz.",
        "Soru 4'ün çözümü. Örnek bir: Rüzgar pencereleri öfkeyle dövüyordu. Örnek iki: Papatyalar sabah güneşine gülümsedi.",
        "<strong>Örnek Cümleler (Öğrenci Modeli):</strong><br>1. <em>'Rüzgâr bütün gece penceremize öfkeyle vurdu.'</em> (Öfkelenmek insana aittir, rüzgara verilmiştir.)<br>2. <em>'Sabah güneş açınca çiçekler neşeyle birbirine fısıldadı.'</em> (Fısıldaşmak insana aittir.)",
        "1. Cümle: ... \n2. Cümle: ..."
    )

    q5 = build_q_strip(
        5, "Kritik Yazım Kurallarını Örneklendirme", 20,
        "turkce_q5.mp3", "turkce_sol5.mp3",
        "Soru 5. Belirli tarihler, coğrafi ikinci yer adları ve cadde sokak kurallarını örnekleyen birer cümle yazınız.",
        "Soru 5'in çözümü. 1: 12 Mayıs 2018 Cumartesi günü doğdu. 2: Van Gölü kıyısına gittik. 3: Atatürk Caddesi, Zambak Sokakta oturuyoruz.",
        "<strong>I. Belirli Tarih Kuralı:</strong> 'Kardeşim <strong>12 Mayıs 2018 Cumartesi</strong> günü dünyaya geldi.'<br><strong>II. Coğrafi Yer Adı:</strong> 'Tatilimizi <strong>Van Gölü</strong> kıyısında geçirdik.'<br><strong>III. Cadde ve Sokak:</strong> 'Okulumuz <strong>Cumhuriyet Bulvarı, Menekşe Sokak</strong> üzerindedir.'",
        "I. Tarih cümlesi:\nII. Göl/Dağ/Nehir cümlesi:\nIII. Cadde/Sokak cümlesi:"
    )

    q6 = build_q_strip(
        6, "Bitki veya Hayvan Betimlemesi", 15,
        "turkce_q6.mp3", "turkce_sol6.mp3",
        "Soru 6. İlginç bulduğunuz bir bitki veya hayvanın belirgin özelliklerini betimleyiniz.",
        "Soru 6'nın çözümü. Örneğin bukalemun renk değiştirme özelliği ve bağımsız hareket eden gözleriyle mükemmel bir uyum sergiler.",
        "<strong>Örnek Betimleme (Bukalemun):</strong><br>Bukalemunlar, bulundukları ortama göre saniyeler içinde renk değiştirebilen olağanüstü sürüngenlerdir. Birbirinden bağımsız 360 derece dönebilen gözleri ve vücut boyundan daha uzun yapışkan dilleri sayesinde avlarını hiç hareket etmeden yakalayabilirler.",
        "Seçtiğiniz bir canlıyı renk, şekil ve hareket özellikleriyle anlatınız..."
    )

    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>5. Sınıf Türkçe 1. Dönem 1. Yazılı - Tüm Sorular Çözümlü</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body class="theme-turkce">
  {get_header('turkce')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>📚</span> 5. Sınıf Türkçe 1. Dönem 1. Yazılı</h1>
        <p>Orijinal Sınav Kağıdı Üzerinde Soru Soru Çözüm • 6 Sorunun Tamamı • PC ve Mobilde Doğal Seslendirme</p>
      </div>
      <div class="score-box">
        <div class="score-val" id="currentScoreVal">0</div>
        <div class="score-lbl">Mevcut Puan / 100</div>
      </div>
    </div>

    <!-- Audio Player Bar -->
    <div class="audio-bar">
      <div class="audio-bar-info">
        <div class="audio-icon-pulse">🔊</div>
        <div>
          <strong style="display:block; font-size:0.95rem;">Türkçe Sesli Rehber (PC & Mobil Uyumlu)</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır — Dinlemek için ses butonlarına tıklayın</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.playAudio('turkce_summary.mp3', null, '5. Sınıf Türkçe 1. Dönem 1. Yazılı Konu Özeti. Metinde anlam, söz sanatlarından kişileştirme, belirli tarihlerde ve coğrafi adlarda büyük harflerin yazımı konuları sınavın temelini oluşturur.')">📢 Konu Özetini Dinle</button>
      </div>
    </div>

    <!-- Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="pdf-pane">📄 Orijinal PDF Üzerinde Tüm Soruları Çöz</button>
      <button class="tab-btn" data-tab="answer-key-pane">🔑 Öğretmen Cevap Anahtarı</button>
      <button class="tab-btn" data-tab="summary-pane">💡 Sınavda Çıkacak Hap Bilgiler</button>
    </div>

    <!-- TAB 1: WORKBENCH -->
    <div id="pdf-pane" class="tab-pane active">
      <div class="interactive-pdf-container">
        
        <!-- Sayfa 1 -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Orijinal Soru Kağıdı - Sayfa 1 (Soru 1, Soru 2, Soru 3)</span>
            <span style="font-size:0.85rem; opacity:0.85;">1. Dönem 1. Yazılı</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/pdf_pages/turkce/page_1.png" alt="Türkçe Sayfa 1" loading="eager">
          </div>
          <div class="pdf-question-controls">
            {q1}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q2}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q3}
          </div>
        </div>

        <!-- Sayfa 2 -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Orijinal Soru Kağıdı - Sayfa 2 (Soru 4, Soru 5, Soru 6)</span>
            <span style="font-size:0.85rem; opacity:0.85;">1. Dönem 1. Yazılı</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/pdf_pages/turkce/page_2.png" alt="Türkçe Sayfa 2" loading="lazy">
          </div>
          <div class="pdf-question-controls">
            {q4}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q5}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q6}
          </div>
        </div>

      </div>

      <div style="text-align: center; margin: 36px 0;">
        <button class="btn-start" style="padding: 18px 42px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 Türkçe Sınav Notumu Hesapla
        </button>
      </div>
    </div>

    <!-- TAB 2: ANSWER KEY -->
    <div id="answer-key-pane" class="tab-pane">
      <div class="pdf-interactive-page">
        <div class="page-banner" style="background:#047857;">
          <span>📄 Orijinal Öğretmen Cevap Anahtarı Sayfa 3 & 4</span>
          <span style="font-size:0.85rem; opacity:0.85;">Resmi MEB / Yayın Çözümleri</span>
        </div>
        <div class="pdf-image-wrap">
          <img src="assets/pdf_pages/turkce/page_3.png" alt="Türkçe Cevap 3" loading="lazy">
        </div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
          <img src="assets/pdf_pages/turkce/page_4.png" alt="Türkçe Cevap 4" loading="lazy">
        </div>
      </div>
    </div>

    <!-- TAB 3: SUMMARY -->
    <div id="summary-pane" class="tab-pane">
      <div class="summary-cards">
        <div class="summary-card">
          <h4>📖 1. Sözcükte Anlam ve Bağlam</h4>
          <ul>
            <li><strong>Gerçek Anlam:</strong> Kelimenin ilk temel anlamı.</li>
            <li><strong>Mecaz Anlam:</strong> Soyutlaşmış ve gerçek anlamından uzaklaşmış kullanım.</li>
            <li><strong>Terim Anlam:</strong> Belirli bir bilim, meslek ve sanata özgü kavramlar (icat, yosun, mıknatıs).</li>
          </ul>
        </div>
        <div class="summary-card">
          <h4>🎭 2. Söz Sanatları: Kişileştirme (Teşhis)</h4>
          <ul>
            <li>İnsana özgü niteliklerin (sevinme, kızma, gülme) insan dışı varlıklara verilmesidir.</li>
          </ul>
        </div>
        <div class="summary-card">
          <h4>✍️ 3. Büyük Harflerin Kullanımı</h4>
          <ul>
            <li>Belirli tarih: 29 Ekim 1923 Cuma günü.</li>
            <li>Yer adı tür bildirimi: Van Gölü, Ağrı Dağı, Tuna Nehri.</li>
            <li>Mahalle, cadde, sokak: Cumhuriyet Mahallesi, Menekşe Sokak.</li>
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

print("Generator functions ready!")
