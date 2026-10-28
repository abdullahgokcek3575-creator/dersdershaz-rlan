# -*- coding: utf-8 -*-
"""
Full Generator for all subjects:
1. turkce.html (6 questions)
2. matematik.html (10 questions)
3. fen-bilimleri.html (7 questions)
4. sosyal-bilgiler.html (7 questions)
5. din-kulturu.html (5 sections A-E)
6. ingilizce.html (5 sections A-E)
7. mebi-sorulari.html (7. Sınıf MEBİ Tüm Dersler Yazılı Çalışması)
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
    q_speak_esc = q_speak_text.replace("'", "\\'").replace('"', '&quot;').replace('\n', ' ')
    sol_speak_esc = sol_speak_text.replace("'", "\\'").replace('"', '&quot;').replace('\n', ' ')
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
# 2. MATEMATİK (10 Sorunun Tamamı - 10 x 10 = 100 Puan)
# =========================================================================
def generate_matematik():
    q1 = build_q_strip(1, "Çizim Araçlarının İsimleri", 10, "mat_q1.mp3", "mat_sol1.mp3",
        "Soru 1. Aşağıda verilen dört adet çizim aracının isimlerini altlarına yazınız.",
        "Soru 1'in çözümü. Sırasıyla: Gönye, Cetvel, Açıölçer yani iletki, ve Pergel.",
        "1. <strong>Gönye</strong><br>2. <strong>Cetvel</strong><br>3. <strong>Açıölçer (İletki)</strong><br>4. <strong>Pergel</strong>",
        "1: Gönye, 2: Cetvel, 3: Açıölçer, 4: Pergel...")

    q2 = build_q_strip(2, "Geometrik Çizimlerin Sembolik Gösterimi", 10, "mat_q2.mp3", "mat_sol2.mp3",
        "Soru 2. A ve V noktalarıyla verilen doğru parçası ve ışının sembolle gösterimini yazınız.",
        "Soru 2'nin çözümü. A şıkkı doğru parçası olduğu için köşeli parantez AV veya köşeli parantez VA. B şıkkı ışın olduğu için köşeli parantez AV şeklinde gösterilir.",
        "a) Doğru Parçası: <strong>[AV]</strong> veya <strong>[VA]</strong><br>b) Işın (A noktası kapalı, V yönünde sonsuz): <strong>[AV</strong> veya <strong>[AV)</strong>",
        "a) [AV] ... b) [AV ...")

    q3 = build_q_strip(3, "Açının Kolları, Köşesi ve Sembolle Gösterimi", 10, "mat_q3.mp3", "mat_sol3.mp3",
        "Soru 3. Şekilde verilen açının kollarını, köşesini ve sembolle gösterimlerini yazınız.",
        "Soru 3'ün çözümü. Açının kolları LM ışını ve LK ışınıdır. Köşesi L noktasıdır. Sembolle gösterimi M L K açısı, K L M açısı veya sadece L açısıdır.",
        "a) <strong>Açının Kolları:</strong> [LM ışını ve [LK ışını<br>b) <strong>Açının Köşesi:</strong> L noktası<br>c) <strong>Sembolle Gösterimleri:</strong> ML̂K, KL̂M, L̂",
        "a) Kolları: ... b) Köşesi: ... c) Sembolle:")

    q4 = build_q_strip(4, "Pergel ile 3 cm Yarıçaplı Çember Çizimi", 10, "mat_q4.mp3", "mat_sol4.mp3",
        "Soru 4. Pergel kullanarak 3 santimetre yarıçaplı bir çember çiziniz.",
        "Soru 4'ün çözümü. Pergelin sivri ucu ile kalem ucu arasındaki mesafe cetvel üzerinde 3 santimetre açılır. Sivri uç merkez olarak sabitlenip 360 derece döndürülerek çizilir.",
        "<strong>Çizim Adımları:</strong><br>1. Cetvel üzerinde pergelin açıklığı tam <strong>3 cm</strong> ayarlanır.<br>2. Sayfada bir 'M' (Merkez) noktası belirlenir.<br>3. Pergelin iğneli ucu M noktasına sabitlenerek kalem 360° döndürülür.<br><em>Elde edilen çemberin yarıçapı r = 3 cm, çapı R = 6 cm olur.</em>",
        "Çizim adımlarını veya pergel açıklığını yazınız...")

    q5 = build_q_strip(5, "Çemberin Elemanları", 10, "mat_q5.mp3", "mat_sol5.mp3",
        "Soru 5. Aşağıda verilen çemberin şekillerle belirtilen elemanlarını yazınız.",
        "Soru 5'in çözümü. Çemberin elemanları: Çap, Yarıçap ve Merkez.",
        "a) <strong>Çap:</strong> Çemberin merkezinden geçen ve iki noktayı birleştiren en uzun doğru parçasıdır (2r).<br>b) <strong>Yarıçap:</strong> Merkezden çember üzerindeki herhangi bir noktaya olan uzaklıktır (r).<br>c) <strong>Merkez:</strong> Çemberin tam orta sabit noktasıdır (M).",
        "a) Çap, b) Yarıçap, c) Merkez...")

    q6 = build_q_strip(6, "CD Doğru Parçasına A Noktasından Dikme Çizimi", 10, "mat_q6.mp3", "mat_sol6.mp3",
        "Soru 6. CD doğru parçasına A noktasından dikme çiziniz.",
        "Soru 6'nın çözümü. Gönyenin dik kenarlarından biri CD doğrusunun üzerine yerleştirilir, diğer dik kenar A noktasına getirilerek aşağı doğru dikme doğru parçası çizilir.",
        "<strong>Dikme Çizimi:</strong><br>Gönye kullanılarak A noktasından CD doğrusuna 90 derecelik dikme indirilir. Sembolle: <strong>[AH] ⊥ CD</strong>.",
        "Nasıl çizileceğini açıklayınız...")

    q7 = build_q_strip(7, "d Doğrusuna 2 cm Uzaklıkta Üç Nokta Belirleme", 10, "mat_q7.mp3", "mat_sol7.mp3",
        "Soru 7. d doğrusuna 2 santimetre uzaklıkta olan üç nokta belirleyiniz.",
        "Soru 7'nin çözümü. d doğrusu üzerinde farklı yerlerden 2 santimetrelik dikmeler çıkılarak K, L, M noktaları işaretlenir. Bu noktalar d doğrusuna paralel bir doğru üzerinde yer alır.",
        "<strong>Çözüm:</strong><br>d doğrusuna dik doğrultuda 2 cm mesafede <strong>K, L, M</strong> noktaları işaretlenir. Bu üç nokta birleştirildiğinde d doğrusuna paralel yeni bir doğru oluşur.",
        "K, L, M noktalarının konumunu açıklayınız...")

    q8 = build_q_strip(8, "Açıyı İsimlendirip Açıölçerle Ölçme", 10, "mat_q8.mp3", "mat_sol8.mp3",
        "Soru 8. Şekilde verilen açıyı isimlendirip açıölçerle ölçünüz ve ölçüsünü sembolle gösteriniz.",
        "Soru 8'in çözümü. Açının ölçüsü 40 derecedir. Gösterimi m A B C açısı eşittir 40 derece.",
        "<strong>Ölçüm Sonucu:</strong><br>• Açının Adı: ABC açısı (B̂)<br>• Ölçüsü: <strong>40°</strong><br>• Sembolle Gösterimi: <strong>m(AB̂C) = 40°</strong> veya <strong>s(B̂) = 40°</strong>",
        "Açının ismi ve ölçüsü: m(...) = ... derece")

    q9 = build_q_strip(9, "Aynı Kağıttaki İki Doğrunun Oluşturabileceği Durumlar", 10, "mat_q9.mp3", "mat_sol9.mp3",
        "Soru 9. Aynı kağıt üzerine çizilebilecek iki doğrunun oluşturabileceği tüm durumları çizerek yazınız.",
        "Soru 9'un çözümü. İki doğru paralel olabilir, tek bir noktada kesişebilir, dik kesişebilir veya çakışık olabilir.",
        "<strong>1. Paralel Doğrular:</strong> Hiçbir noktada kesişmezler (d // e).<br><strong>2. Kesişen Doğrular:</strong> Tek bir ortak noktada kesişirler.<br><strong>3. Dik Kesişen Doğrular:</strong> Aralarındaki açı 90° olarak kesişirler (d ⊥ e).<br><strong>4. Çakışık Doğrular:</strong> Tüm noktaları ortaktır, üst üste binerler.",
        "1. Paralel, 2. Kesişen, 3. Dik kesişen, 4. Çakışık...")

    q10 = build_q_strip(10, "Komşu Tümler ve Komşu Bütünler Açıları Bulma", 10, "mat_q10.mp3", "mat_sol10.mp3",
        "Soru 10. Komşu tümler ve komşu bütünler açılardan yararlanarak FUR ve DNY açılarının ölçüsünü bulunuz.",
        "Soru 10'un çözümü. Tümler açılar toplamı 90 derecedir: 90 eksi 40 eşittir 50 derece. Bütünler açılar toplamı 180 derecedir: 180 eksi 128 eşittir 52 derece.",
        "<strong>1. Durum (Tümler Açılar - Toplam 90°):</strong><br>m(FÛR) = 90° - 40° = <strong>50°</strong><br><br><strong>2. Durum (Bütünler Açılar - Toplam 180°):</strong><br>m(DNY) = 180° - 128° = <strong>52°</strong>",
        "m(FUR) = 90 - 40 = ... , m(DNY) = 180 - 128 = ...")

    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>5. Sınıf Matematik 1. Dönem 1. Yazılı - 10 Sorunun Tamamı Çözümlü</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body class="theme-mat">
  {get_header('mat')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>📐</span> 5. Sınıf Matematik 1. Dönem 1. Yazılı</h1>
        <p>10 Sorunun Tamamı İnteraktif Çözümlü • PDF Üzerinde Doğrudan Çalışma • 100 Puanlık Sınav</p>
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
          <strong style="display:block; font-size:0.95rem;">Matematik Sesli Rehber (PC & Mobil Uyumlu)</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır — Dinlemek için ses butonlarına tıklayın</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.playAudio('mat_summary.mp3', null, '5. Sınıf Matematik 1. Dönem 1. Yazılı Konu Özeti. Geometrik çizim araçları, doğru parçası ve ışın sembolleri, pergel ile çember çizimi, tümler açılar 90 derece ve bütünler açılar 180 derecedir.')">📢 Konu Özetini Dinle</button>
      </div>
    </div>

    <!-- Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="pdf-pane">📄 Orijinal PDF Üzerinde 10 Soruyu Çöz</button>
      <button class="tab-btn" data-tab="answer-key-pane">🔑 Resmi Çözüm Anahtarı</button>
      <button class="tab-btn" data-tab="summary-pane">💡 Sınavda Çıkacak Hap Bilgiler</button>
    </div>

    <!-- TAB 1: WORKBENCH -->
    <div id="pdf-pane" class="tab-pane active">
      <div class="interactive-pdf-container">
        
        <!-- Sayfa 1 (Soru 1-4) -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Soru Kağıdı Sayfa 1 (Soru 1, 2, 3, 4)</span>
            <span style="font-size:0.85rem; opacity:0.85;">40 Puan</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/pdf_pages/matematik/page_1.png" alt="Matematik Sayfa 1" loading="eager">
          </div>
          <div class="pdf-question-controls">
            {q1}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q2}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q3}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q4}
          </div>
        </div>

        <!-- Sayfa 2 (Soru 5-10) -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Soru Kağıdı Sayfa 2 (Soru 5, 6, 7, 8, 9, 10)</span>
            <span style="font-size:0.85rem; opacity:0.85;">60 Puan</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/pdf_pages/matematik/page_2.png" alt="Matematik Sayfa 2" loading="lazy">
          </div>
          <div class="pdf-question-controls">
            {q5}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q6}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q7}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q8}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q9}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q10}
          </div>
        </div>

      </div>

      <div style="text-align: center; margin: 36px 0;">
        <button class="btn-start" style="padding: 18px 42px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 Matematik Sınav Notumu Hesapla
        </button>
      </div>
    </div>

    <!-- TAB 2: ANSWER KEY -->
    <div id="answer-key-pane" class="tab-pane">
      <div class="pdf-interactive-page">
        <div class="page-banner" style="background:#047857;">
          <span>📄 Orijinal Öğretmen Çözüm Anahtarı Sayfa 3 & 4</span>
          <span style="font-size:0.85rem; opacity:0.85;">Resmi Çözümler</span>
        </div>
        <div class="pdf-image-wrap">
          <img src="assets/pdf_pages/matematik/page_3.png" alt="Matematik Cevap 3" loading="lazy">
        </div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
          <img src="assets/pdf_pages/matematik/page_4.png" alt="Matematik Cevap 4" loading="lazy">
        </div>
      </div>
    </div>

    <!-- TAB 3: SUMMARY -->
    <div id="summary-pane" class="tab-pane">
      <div class="summary-cards">
        <div class="summary-card">
          <h4>📐 1. Geometrik Çizim Araçları</h4>
          <ul>
            <li><strong>Cetvel:</strong> Doğru parçası çizimi ve uzunluk ölçümü.</li>
            <li><strong>Gönye:</strong> 90 derecelik diklik ve dikme çizimleri.</li>
            <li><strong>İletki (Açıölçer):</strong> Açının derece cinsinden ölçümü (0° - 180°).</li>
            <li><strong>Pergel:</strong> Belirli yarıçapta çember ve yay çizimi.</li>
          </ul>
        </div>
        <div class="summary-card">
          <h4>📏 2. Tümler ve Bütünler Açılar</h4>
          <ul>
            <li><strong>Tümler Açılar:</strong> Ölçüleri toplamı 90°'dir. Örn: 40°'nin tümleri 50°'dir.</li>
            <li><strong>Bütünler Açılar:</strong> Ölçüleri toplamı 180°'dir. Örn: 128°'nin bütünleri 52°'dir.</li>
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

# =========================================================================
# 3. FEN BİLİMLERİ (7 Sorunun Tamamı - Toplam 100 Puan)
# =========================================================================
def generate_fen():
    q1 = build_q_strip(1, "Güneş'in 5 Temel Özelliği", 15, "fen_q1.mp3", "fen_sol1.mp3",
        "Soru 1. Görselleri inceleyerek Güneş'in özelliklerinden 5 tanesini yazınız.",
        "Soru 1'in çözümü. 1: Dünyaya en yakın yıldızdır. 2: Isı ve ışık kaynağımızdır. 3: Çok sıcak gazlardan oluşur. 4: Şekli küreseldir. 5: Kendi ekseni etrafında saat yönünün tersine döner.",
        "1. <strong>Dünya'ya en yakın yıldızdır.</strong><br>2. <strong>Isı ve ışık kaynağımızdır.</strong><br>3. <strong>Sıcak gazlardan (hidrojen ve helyum) oluşur.</strong><br>4. <strong>Şekli küreye benzer.</strong><br>5. <strong>Kendi ekseni etrafında saat yönünün tersine döner</strong> (yaklaşık 25 gün).",
        "1: ...\n2: ...\n3: ...\n4: ...\n5: ...")

    q2 = build_q_strip(2, "Pepee ve Ninesi: Ay'ın Atmosfersizliği ve Yaşam", 15, "fen_q2.mp3", "fen_sol2.mp3",
        "Soru 2. Ay'da atmosfer olmadığı için Dünya'daki hangi olaylar görülmez ve Ay'a giderken ne götürülmelidir?",
        "Soru 2'nin çözümü. A şıkkı: Yağmur, rüzgar gibi hava olayları görülmez, ses iletilmez. B şıkkı: Oksijen tüpü, uzay giysisi, su ve besin götürülmelidir.",
        "<strong>a) Ay'da Meydana Gelmeyen Olaylar:</strong><br>• Yağmur, kar, fırtına gibi hava olayları gerçekleşmez.<br>• Rüzgâr oluşmaz.<br>• Ses yayılmaz (uzay boşluğu).<br><br><strong>b) Dünya'dan Götürülmesi Gerekenler:</strong><br>• Oksijen tüpü / hava<br>• Su ve besin maddeleri<br>• Özel koruyucu uzay giysisi",
        "a) Görülmeyen olaylar: ...\nb) Götürülecekler: ...")

    q3 = build_q_strip(3, "Dünya ve Ay'ın Hareket Süreleri", 15, "fen_q3.mp3", "fen_sol3.mp3",
        "Soru 3. Ay'ın dolanma yönü ve süreleri: a) Dolanma yönü, b) Dolanma süresi, c) Kendi ekseni etrafında dönme süresi.",
        "Soru 3'ün çözümü. Dolanma yönü saat yönünün tersinedir yani batıdan doğuya. Dolanma süresi yaklaşık 27 gün 8 saattir. Kendi etrafında dönme süresi de yaklaşık 27 gün 8 saattir.",
        "a) <strong>Dolanma Yönü:</strong> Saat yönünün tersine (batıdan doğuya doğru).<br>b) <strong>Dünya Etrafında Dolanma Süresi:</strong> Yaklaşık <strong>27 gün 8 saat</strong>.<br>c) <strong>Kendi Ekseni Etrafında Dönme Süresi:</strong> Yaklaşık <strong>27 gün 8 saat</strong>.<br><em>Not: İki süre eşit olduğu için Dünya'dan Ay'ın hep aynı yüzü görünür!</em>",
        "a) Yön: ...\nb) Dolanma süresi: ...\nc) Dönme süresi: ...")

    q4 = build_q_strip(4, "Ay'ın Evreleri (Ana ve Ara Evreler)", 15, "fen_q4.mp3", "fen_sol4.mp3",
        "Soru 4. Ay'ın Dünya'dan gözlemlenen evrelerinin adını, ana ve ara evrelerini yazınız.",
        "Soru 4'ün çözümü. 1: Yeni ay, 2: Hilal, 3: İlk dördün, 4: Şişkin ay, 5: Dolunay, 6: Şişkin ay, 7: Son dördün, 8: Hilal. Ana evreler: Yeni ay, İlk dördün, Dolunay, Son dördün.",
        "<strong>a) Kutucuklar:</strong> 1: Yeni Ay, 2: Hilal, 3: İlk Dördün, 4: Şişkin Ay, 5: Dolunay, 6: Şişkin Ay, 7: Son Dördün, 8: Hilal<br><strong>b) Ana Evreler:</strong> <em>Yeni Ay, İlk Dördün, Dolunay, Son Dördün</em><br><strong>c) Ara Evreler:</strong> <em>Hilal, Şişkin Ay</em>",
        "Ana evreler: ...\nAra evreler: ...")

    q5 = build_q_strip(5, "Ay'ın 1, 3, 5, 7 Konumlarındaki Görünümü", 10, "fen_q5.mp3", "fen_sol5.mp3",
        "Soru 5. Ay 1, 3, 5 ve 7 numaralı konumlardayken Dünya'dan görünümünü yazınız.",
        "Soru 5'in çözümü. 1 konumunda Yeni ay görünmez. 3 konumunda İlk dördün düz D harfi. 5 konumunda Dolunay tamamen parlak. 7 konumunda Son dördün ters D harfi.",
        "• <strong>1 Konumu:</strong> <strong>Yeni Ay</strong> (Karanlık görünür, Dünya'dan seçilemez).<br>• <strong>3 Konumu:</strong> <strong>İlk Dördün</strong> (Ay'ın sağ yarısı aydınlık, düz 'D' harfi).<br>• <strong>5 Konumu:</strong> <strong>Dolunay</strong> (Ay'ın Dünya'ya bakan yüzü tamamen aydınlık daire).<br>• <strong>7 Konumu:</strong> <strong>Son Dördün</strong> (Ay'ın sol yarısı aydınlık, ters 'D' harfi).",
        "1: Yeni ay, 3: İlk dördün, 5: Dolunay, 7: Son dördün...")

    q6 = build_q_strip(6, "Güneş, Dünya ve Ay'ın Hareket Süreleri", 15, "fen_q6.mp3", "fen_sol6.mp3",
        "Soru 6. Görselde K, L, M, N, O harfleriyle belirtilen hareketlerin adlarını ve sürelerini yazınız.",
        "Soru 6'nın çözümü. K Güneşin dönmesi 25 gün. L Dünyanın dolanması 365 gün 6 saat. M Ayın dönmesi 27 gün 8 saat. N Ayın dolanması 27 gün 8 saat. O Dünyanın dönmesi 24 saat.",
        "<strong>Hareketler ve Tamamlanma Süreleri:</strong><br>• <strong>K:</strong> Güneş'in kendi ekseninde dönmesi → <strong>Yaklaşık 25 gün</strong><br>• <strong>L:</strong> Dünya'nın Güneş etrafında dolanması → <strong>365 gün 6 saat (1 yıl)</strong><br>• <strong>M:</strong> Ay'ın kendi ekseninde dönmesi → <strong>Yaklaşık 27 gün 8 saat</strong><br>• <strong>N:</strong> Ay'ın Dünya etrafında dolanması → <strong>Yaklaşık 27 gün 8 saat</strong><br>• <strong>O:</strong> Dünya'nın kendi ekseninde dönmesi → <strong>24 saat (1 gün)</strong>",
        "K: Güneş dönmesi ...\nL: Dünya dolanması ...\nM: Ay dönmesi ...\nN: Ay dolanması ...\nO: Dünya dönmesi ...")

    q7 = build_q_strip(7, "Özdeş Dinamometrelerde Ağırlık Hesaplama", 15, "fen_q7.mp3", "fen_sol7.mp3",
        "Soru 7. K cisminin ağırlığı 72 Newton olduğuna göre L, M, N, P ve R cisimlerinin ağırlıklarını bulunuz.",
        "Soru 7'nin çözümü. Dinamometrenin her bir bölmesi 12 Newton'dur. L 60 N, M 48 N, N 36 N, P 24 N, R 12 Newton'dur.",
        "<strong>Çözüm Adımları:</strong><br>K cismi 6 bölme uzatmış ve 72 N ise: 1 bölme = 72 ÷ 6 = <strong>12 N</strong>'dur.<br>• <strong>L (5 bölme):</strong> 5 × 12 = <strong>60 N</strong><br>• <strong>M (4 bölme):</strong> 4 × 12 = <strong>48 N</strong><br>• <strong>N (3 bölme):</strong> 3 × 12 = <strong>36 N</strong><br>• <strong>P (2 bölme):</strong> 2 × 12 = <strong>24 N</strong><br>• <strong>R (1 bölme):</strong> 1 × 12 = <strong>12 N</strong>",
        "L = ... N, M = ... N, N = ... N, P = ... N, R = ... N")

    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>5. Sınıf Fen Bilimleri 1. Dönem 1. Yazılı - Tüm Sorular Çözümlü</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body class="theme-fen">
  {get_header('fen')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>🔬</span> 5. Sınıf Fen Bilimleri 1. Dönem 1. Yazılı</h1>
        <p>Güneş, Dünya ve Ay'ın Hareketleri • Dinamometre ile Kuvvet Ölçümü • 7 Sorunun Tamamı Çözümlü</p>
      </div>
      <div class="score-box">
        <div class="score-val" id="currentScoreVal">0</div>
        <div class="score-lbl">Mevcut Puan / 100</div>
      </div>
    </div>

    <!-- Audio Bar -->
    <div class="audio-bar">
      <div class="audio-bar-info">
        <div class="audio-icon-pulse">🔊</div>
        <div>
          <strong style="display:block; font-size:0.95rem;">Fen Bilimleri Sesli Rehber</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır — Dinlemek için butonlara tıklayın</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.playAudio('fen_summary.mp3', null, '5. Sınıf Fen Bilimleri 1. Dönem 1. Yazılı Konu Özeti. Güneş gazlardan oluşur ve saat yönünün tersine 25 günde döner. Ayda atmosfer yoktur. Ayın ana evreleri yeni ay, ilk dördün, dolunay ve son dördündür. Kuvvet birimi Newton olup dinamometre yayındaki uzama uygulanan kuvvetle doğru orantılıdır.')">📢 Konu Özetini Dinle</button>
      </div>
    </div>

    <!-- Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="pdf-pane">📄 Orijinal PDF Üzerinde Tüm Soruları Çöz</button>
      <button class="tab-btn" data-tab="answer-key-pane">🔑 Resmi Çözüm Anahtarı</button>
      <button class="tab-btn" data-tab="summary-pane">💡 Sınavda Çıkacak Hap Bilgiler</button>
    </div>

    <!-- TAB 1: WORKBENCH -->
    <div id="pdf-pane" class="tab-pane active">
      <div class="interactive-pdf-container">
        
        <!-- Sayfa 1 -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Soru Kağıdı Sayfa 1 (Soru 1, 2, 3, 4)</span>
            <span style="font-size:0.85rem; opacity:0.85;">60 Puan</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/pdf_pages/fen/page_1.png" alt="Fen Sayfa 1" loading="eager">
          </div>
          <div class="pdf-question-controls">
            {q1}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q2}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q3}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q4}
          </div>
        </div>

        <!-- Sayfa 2 -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Soru Kağıdı Sayfa 2 (Soru 5, 6, 7)</span>
            <span style="font-size:0.85rem; opacity:0.85;">40 Puan</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/pdf_pages/fen/page_2.png" alt="Fen Sayfa 2" loading="lazy">
          </div>
          <div class="pdf-question-controls">
            {q5}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q6}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q7}
          </div>
        </div>

      </div>

      <div style="text-align: center; margin: 36px 0;">
        <button class="btn-start" style="padding: 18px 42px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 Fen Bilimleri Sınav Notumu Hesapla
        </button>
      </div>
    </div>

    <!-- TAB 2: ANSWER KEY -->
    <div id="answer-key-pane" class="tab-pane">
      <div class="pdf-interactive-page">
        <div class="page-banner" style="background:#047857;">
          <span>📄 Orijinal Öğretmen Çözüm Anahtarı Sayfa 3 & 4</span>
          <span style="font-size:0.85rem; opacity:0.85;">Resmi Çözümler</span>
        </div>
        <div class="pdf-image-wrap">
          <img src="assets/pdf_pages/fen/page_3.png" alt="Fen Cevap 3" loading="lazy">
        </div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
          <img src="assets/pdf_pages/fen/page_4.png" alt="Fen Cevap 4" loading="lazy">
        </div>
      </div>
    </div>

    <!-- TAB 3: SUMMARY -->
    <div id="summary-pane" class="tab-pane">
      <div class="summary-cards">
        <div class="summary-card">
          <h4>☀️ 1. Güneş'in Temel Özellikleri</h4>
          <ul>
            <li>Şekli küredir, %73 Hidrojen ve %25 Helyum gazlarından oluşur.</li>
            <li>Dünyamızın temel ısı ve ışık kaynağıdır.</li>
            <li>Kendi ekseni etrafında saat yönünün tersine döner (yaklaşık 25 gün).</li>
          </ul>
        </div>
        <div class="summary-card">
          <h4>🌑 2. Ay'ın Evreleri</h4>
          <ul>
            <li>Ana Evreler: Yeni Ay → İlk Dördün → Dolunay → Son Dördün.</li>
            <li>Ara Evreler: Hilal ve Şişkin Ay.</li>
            <li>İki ana evre arası yaklaşık 1 haftadır (7 gün).</li>
          </ul>
        </div>
        <div class="summary-card">
          <h4>⚖️ 3. Dinamometre</h4>
          <ul>
            <li>Kuvvet ölçüm aracıdır, birimi Newton (N)'dur.</li>
            <li>Yayın uzama miktarı cismin ağırlığıyla doğru orantılıdır.</li>
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

print("Matematik and Fen generators created successfully!")
