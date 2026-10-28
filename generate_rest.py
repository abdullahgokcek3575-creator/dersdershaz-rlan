# -*- coding: utf-8 -*-
"""
Generate Sosyal, Din, İngilizce, MEBİ 7. Sınıf and update build process.
"""

from generate_mat_fen import get_header, get_footer, get_score_modal, build_q_strip

# =========================================================================
# 4. SOSYAL BİLGİLER (7 Sorunun Tamamı - Toplam 100 Puan)
# =========================================================================
def generate_sosyal():
    q1 = build_q_strip(1, "Hak ve Rol Tanımları", 10, "sosyal_q1.mp3", "sosyal_sol1.mp3",
        "Soru 1. Öğrencilerle ilgilenmek ve ev işlerinde yardımcı olmayı isteyen rollerin adlarını yazınız.",
        "Soru 1'in çözümü. 1: Öğretmen, 2: Anne veya Baba rolü.",
        "1. Öğrencilerle ilgilenmek: <strong>Öğretmen rolü</strong><br>2. Ev işlerinde çocukların yardımını istemek: <strong>Anne / Baba rolü</strong>",
        "1: Öğretmen, 2: Anne / Baba...")

    q2 = build_q_strip(2, "Osman Furkan'ın Gruplardaki Rolleri", 20, "sosyal_q2.mp3", "sosyal_sol2.mp3",
        "Soru 2. Osman Furkan'ın içinde bulunduğu gruplardaki rollerini yazınız.",
        "Soru 2'nin çözümü. Ailede: Çocuk ve abi. Okulda: Öğrenci ve sınıf arkadaşı. Futbol takımında: Takım kaptanı veya lideri.",
        "• <strong>Aile Grubunda:</strong> Evlat (Çocuk) ve Abi rolü<br>• <strong>Okul Grubunda (5. Sınıf):</strong> Öğrenci ve Sınıf Arkadaşı rolü<br>• <strong>Futbol Takımında:</strong> Takım Kaptanı (Lideri) rolü",
        "Ailede: ... , Okulda: ... , Takımda: ...")

    q3 = build_q_strip(3, "Mangala Oyununun Farklı Kıtalarında Oynanması", 10, "sosyal_q3.mp3", "sosyal_sol3.mp3",
        "Soru 3. Mangala oyununun Asya, Afrika ve Amerika'da oynanması neyin göstergesidir?",
        "Soru 3'ün çözümü. Kültürel ögelerin evrenselleştiğinin ve farklı toplumlar arasında kültürel etkileşim olduğunun göstergesidir.",
        "<strong>Açıklama:</strong><br>Kültürel miras ögelerimizin evrenselleştiğini, farklı coğrafya ve kıtalardaki toplumları ortak bir eğlence ve zekâ oyunu etrafında birleştirdiğini, <strong>kültürel etkileşim ve zenginliğin</strong> kanıtı olduğunu gösterir.",
        "Kültürel etkileşim ve ortak miras açısından açıklayınız...")

    q4 = build_q_strip(4, "Kültürel Değerlerimiz ve Geleneklerimiz", 15, "sosyal_q4.mp3", "sosyal_sol4.mp3",
        "Soru 4. Metindeki boşluklara gelmesi gereken kültürel özelliklerimizi yazınız.",
        "Soru 4'ün çözümü. 1: Zeybek, 2: Ebru sanatı, 3: Mahya, 4: Mantı, 5: Cumba.",
        "1. Cepken giyilen halk oyunu: <strong>Zeybek</strong><br>2. Su üzerine yağlı boya sanatı: <strong>Ebru</strong><br>3. İki minare arasına asılan ışıklı yazı: <strong>Mahya</strong><br>4. Kayseri'nin ünlü yemeği: <strong>Mantı</strong><br>5. Evlerin dışarı çıkıntı yapan oda bölümü: <strong>Cumba</strong>",
        "1: Zeybek, 2: Ebru, 3: Mahya, 4: Mantı, 5: Cumba...")

    q5 = build_q_strip(5, "Sadaka Taşı Uygulaması ve Amacı", 15, "sosyal_q5.mp3", "sosyal_sol5.mp3",
        "Soru 5. Selçuklu ve Osmanlı döneminde cami ve çeşme yanlarına konan taşın adı ve amacı nedir?",
        "Soru 5'in çözümü. Adı sadaka taşıdır. Amacı ihtiyaç sahiplerini rencide etmeden, gizlice yardım ulaştırmaktır.",
        "• <strong>Uygulamanın Adı:</strong> <strong>Sadaka Taşı</strong><br>• <strong>Yapılış Amacı:</strong> İhtiyaç sahiplerini ve yoksul insanları incitmeden, mahcup etmeden, gece karanlığında gizlice ihtiyaçları kadar parayı almalarını sağlayarak toplumsal dayanışmayı en asil şekilde yaşatmaktır.",
        "Uygulamanın adı: ... \nAmacı: ...")

    q6 = build_q_strip(6, "Tekalif-i Milliye Emirleri", 15, "sosyal_q6.mp3", "sosyal_sol6.mp3",
        "Soru 6. Milli Mücadele döneminde ordunun ihtiyaçlarını karşılamak için çıkarılan emirlere ne denir ve amacı nedir?",
        "Soru 6'nın çözümü. Tekalif-i Milliye Emirleridir. Ordunun giyecek, yiyecek, cephane ve taşıt ihtiyaçlarını milletin dayanışmasıyla karşılamaktır.",
        "• <strong>Emirlerin Adı:</strong> <strong>Tekâlif-i Millîye Emirleri</strong><br>• <strong>Amacı:</strong> Sakarya Meydan Muharebesi öncesinde ordunun giyecek, yiyecek, silah, cephane ve taşıt ihtiyaçlarını halkın fedakârlığı ve yardımlaşması ile temin etmektir.",
        "Emirlerin adı: ... \nAmacı: ...")

    q7 = build_q_strip(7, "Şehirlerin Göreceli Konum Özellikleri", 15, "sosyal_q7.mp3", "sosyal_sol7.mp3",
        "Soru 7. Zonguldak, Nevşehir ve Mersin illerinin göreceli konum özelliklerini yazınız.",
        "Soru 7'nin çözümü. 1: Yeraltı maden kaynakları. 2: Doğal ve tarihi turizm güzellikleri. 3: Ekonomik faaliyetler, tarım ve liman ticareti.",
        "1. Zonguldak (taşkömürü & petrol): <strong>Yeraltı Kaynakları (Madenler)</strong><br>2. Nevşehir (Peribacaları, Göreme): <strong>Doğal ve Tarihî Güzellikler (Turizm)</strong><br>3. Mersin (Uluslararası liman, muz ve limon üretimi): <strong>Ekonomik Faaliyetler, Ulaşım ve Tarım</strong>",
        "1: Yeraltı kaynakları, 2: Doğal güzellikler, 3: Ekonomik faaliyetler...")

    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>5. Sınıf Sosyal Bilgiler 1. Dönem 1. Yazılı - 7 Sorunun Tamamı Çözümlü</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body class="theme-sosyal">
  {get_header('sosyal')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>🌍</span> 5. Sınıf Sosyal Bilgiler 1. Dönem 1. Yazılı</h1>
        <p>Roller & Sorumluluklar • Kültürel Miras • Sadaka Taşı • Tekalif-i Milliye • 7 Sorunun Tamamı</p>
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
          <strong style="display:block; font-size:0.95rem;">Sosyal Bilgiler Sesli Rehber</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır — Dinlemek için butonlara tıklayın</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.playAudio('sosyal_summary.mp3', null, '5. Sınıf Sosyal Bilgiler 1. Dönem 1. Yazılı Konu Özeti. Roller ve sorumluluklar, zeybek, ebru, mahya gibi kültürel zenginliklerimiz, Osmanlıdaki sadaka taşı geleneği, Tekalifi Milliye emirleri ve şehirlerimizin göreceli konum özellikleri sınav konularımızdır.')">📢 Konu Özetini Dinle</button>
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
            <span style="font-size:0.85rem; opacity:0.85;">55 Puan</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/pdf_pages/sosyal/page_1.png" alt="Sosyal Sayfa 1" loading="eager">
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
            <span style="font-size:0.85rem; opacity:0.85;">45 Puan</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/pdf_pages/sosyal/page_2.png" alt="Sosyal Sayfa 2" loading="lazy">
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
          🏆 Sosyal Bilgiler Sınav Notumu Hesapla
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
          <img src="assets/pdf_pages/sosyal/page_3.png" alt="Sosyal Cevap 3" loading="lazy">
        </div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
          <img src="assets/pdf_pages/sosyal/page_4.png" alt="Sosyal Cevap 4" loading="lazy">
        </div>
      </div>
    </div>

    <!-- TAB 3: SUMMARY -->
    <div id="summary-pane" class="tab-pane">
      <div class="summary-cards">
        <div class="summary-card">
          <h4>👥 1. Hak, Sorumluluk ve Roller</h4>
          <ul>
            <li><strong>Hak:</strong> Kanunların bireye tanıdığı yetkilerdir (sağlık, eğitim hakkı).</li>
            <li><strong>Sorumluluk:</strong> Bireyin üzerine düşen görevleri yapmasıdır.</li>
            <li>Bir kişi aynı anda ailede çocuk, okulda öğrenci, sporda kaleci olabilir.</li>
          </ul>
        </div>
        <div class="summary-card">
          <h4>🤝 2. Dayanışma Kurumları</h4>
          <ul>
            <li><strong>Sadaka Taşı:</strong> İhtiyaç sahiplerini incitmeden yapılan gizli yardımlaşmadır.</li>
            <li><strong>Tekâlif-i Millîye:</strong> Millî Mücadele'de ordunun donatılması için halkın yaptığı fedakârlıklardır.</li>
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

# =========================================================================
# 5. DİN KÜLTÜRÜ (A, B, C, D, E Bölümleri - Toplam 100 Puan)
# =========================================================================
def generate_din():
    qA = build_q_strip("A", "Evrendeki Düzen ve Dengeye 3 Örnek", 15, "din_q1.mp3", "din_sol1.mp3",
        "Bölüm A. Allah'ın evreni bir denge ve düzen içinde yaratmasına üç örnek yazınız.",
        "Bölüm A'nın çözümü. 1: Gece ve gündüzün düzenli birbirini izlemesi. 2: Mevsimlerin değişmesi. 3: Yağmurla bitkilerin büyümesi.",
        "1. <strong>Gece ve gündüzün düzenli olarak birbirini izlemesi.</strong><br>2. <strong>Mevsimlerin belli bir ahenk ve düzen içinde değişmesi.</strong><br>3. <strong>Yağmurla birlikte bitkilerin büyüyüp besin üretmesi.</strong><br><em>(Gezegenlerin yörüngeleri veya canlıların solunum dengesi de kabul edilir.)</em>",
        "1: ...\n2: ...\n3: ...")

    qB = build_q_strip("B", "Allah'ın Güzel İsimleri (Esmâ-i Hüsnâ)", 30, "din_q2.mp3", "din_sol2.mp3",
        "Bölüm B. Ayetlerdeki ifadelerin Allah'ın hangi ismine işaret ettiğini yazınız: Bilir, İşitir, Görür, Gücü yeter.",
        "Bölüm B'nin çözümü. Her şeyi bilen: Alîm. Her şeyi işiten: Semî. Her şeyi gören: Basîr. Her şeye gücü yeten: Kadir.",
        "• '…O, göklerde ve yerde olan her şeyi bilir.' → <strong>Alîm</strong><br>• 'Allah her şeyi işitmekte ve her şeyi görmektedir.' → <strong>Semî</strong> ve <strong>Basîr</strong><br>• 'Her şeyi işiten ve bilen odur.' → <strong>Semî</strong> ve <strong>Alîm</strong><br>• 'O, her şeye hakkıyla gücü yetendir.' → <strong>Kadir</strong>",
        "Alîm, Semî, Basîr, Kadir...")

    qC = build_q_strip("C", "Esmâyıhüsna Kavramının Anlamı", 10, "din_q3.mp3", "din_sol3.mp3",
        "Bölüm C. Sinan'ın annesine sorduğu 'Esmâyıhüsna' ifadesinin anlamı nedir?",
        "Bölüm C'nin çözümü. Allah'ın en güzel 99 ismi anlamına gelir.",
        "<strong>Doğru Cevap:</strong><br><strong>Allah'ın en güzel isimleri (Esmâ-i Hüsnâ)</strong>.<br>Yüce Allah'ın Kur'an ve hadislerde bildirilen 99 güzel ismine verilen addır.",
        "Allah'ın en güzel isimleri...")

    qD = build_q_strip("D", "Doğru - Yanlış İfadeleri", 35, "din_q4.mp3", "din_sol4.mp3",
        "Bölüm D. 7 adet dini ifadenin doğru mu yanlış mı olduğunu belirtiniz.",
        "Bölüm D'nin çözümü. 1 Doğru, 2 Yanlış çünkü İhlas suresinde peygamberler değil tevhitten bahsedilir, 3 Doğru, 4 Doğru, 5 Yanlış birden çok yaratıcı olsa kargaşa olurdu, 6 Yanlış samed ismi ihtiyaç duyulmayan demektir, 7 Doğru.",
        "1. Her varlığın bir amaca yönelik yaratılması Allah'ın birliğine delildir. → <strong>DOĞRU ✓</strong><br>2. İhlas suresinde bazı peygamberlerden bahsedilir. → <strong>YANLIŞ ❌</strong> (Tevhitten bahseder)<br>3. Tevhit inancı İslam'ın özünü oluşturan esaslardandır. → <strong>DOĞRU ✓</strong><br>4. Rahman ve Rahim merhameti ifade eder. → <strong>DOĞRU ✓</strong><br>5. Birden fazla yaratıcı olsaydı evrende düzen olurdu. → <strong>YANLIŞ ❌</strong> (Kargaşa çıkardı)<br>6. Ehad ismi Allah'ın hiçbir şeye ihtiyacı olmadığını ifade eder. → <strong>YANLIŞ ❌</strong> (Bu Samed'dir, Ehad tektir demektir)<br>7. İhlas samimiyet ve temizlik anlamına gelir. → <strong>DOĞRU ✓</strong>",
        "1: D, 2: Y, 3: D, 4: D, 5: Y, 6: Y, 7: D...")

    qE = build_q_strip("E", "İhlas Suresi Boşluk Doldurma", 10, "din_q5.mp3", "din_sol5.mp3",
        "Bölüm E. İhlas suresinin okunuşundaki boşlukları doldurunuz.",
        "Bölüm E'nin çözümü. 1: ehad, 2: Allahüssamed, 3: yelid ve yûled, 4: ve lem yeküllehû.",
        "<strong>Bismillahirrahmanirrahim</strong><br>1. Kul hüvellâhü <strong>ehad</strong><br>2. <strong>Allâhü's</strong>-samed<br>3. Lem <strong>yelid</strong> ve lem <strong>yûled</strong><br>4. <strong>Ve lem</strong> yekün lehû küfüven ehad",
        "1: ehad, 2: Allahüssamed, 3: yelid - yûled, 4: Ve lem...")

    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>5. Sınıf Din Kültürü 1. Dönem 1. Yazılı - Tüm Sorular Çözümlü</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body class="theme-din">
  {get_header('din')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>🕌</span> 5. Sınıf Din Kültürü 1. Dönem 1. Yazılı</h1>
        <p>Allah İnancı • Evrendeki Düzen • Esma-i Hüsna • İhlas Suresi • Tüm Bölümler A, B, C, D, E</p>
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
          <strong style="display:block; font-size:0.95rem;">Din Kültürü Sesli Rehber</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır — Dinlemek için butonlara tıklayın</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.playAudio('din_summary.mp3', null, '5. Sınıf Din Kültürü 1. Dönem 1. Yazılı Konu Özeti. Evrendeki mükemmel ahenk, Allahın varlığı ve birliği yani tevhit, Semî, Basîr, Alîm ve Kadir isimleri ile İhlas suresinin anlamı ve okunuşu sınav konularımızdır.')">📢 Konu Özetini Dinle</button>
      </div>
    </div>

    <!-- Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="pdf-pane">📄 Orijinal PDF Üzerinde Tüm Bölümleri Çöz</button>
      <button class="tab-btn" data-tab="answer-key-pane">🔑 Resmi Çözüm Anahtarı</button>
      <button class="tab-btn" data-tab="summary-pane">💡 Sınavda Çıkacak Hap Bilgiler</button>
    </div>

    <!-- TAB 1: WORKBENCH -->
    <div id="pdf-pane" class="tab-pane active">
      <div class="interactive-pdf-container">
        
        <!-- Sayfa 2 (A, B, C) -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Sınav Kağıdı Sayfa 2 (Bölüm A, B, C)</span>
            <span style="font-size:0.85rem; opacity:0.85;">55 Puan</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/pdf_pages/din/page_2.png" alt="Din Sayfa 2" loading="eager">
          </div>
          <div class="pdf-question-controls">
            {qA}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {qB}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {qC}
          </div>
        </div>

        <!-- Sayfa 3 (D, E) -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Sınav Kağıdı Sayfa 3 (Bölüm D, E)</span>
            <span style="font-size:0.85rem; opacity:0.85;">45 Puan</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/pdf_pages/din/page_3.png" alt="Din Sayfa 3" loading="lazy">
          </div>
          <div class="pdf-question-controls">
            {qD}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {qE}
          </div>
        </div>

      </div>

      <div style="text-align: center; margin: 36px 0;">
        <button class="btn-start" style="padding: 18px 42px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 Din Kültürü Sınav Notumu Hesapla
        </button>
      </div>
    </div>

    <!-- TAB 2: ANSWER KEY -->
    <div id="answer-key-pane" class="tab-pane">
      <div class="pdf-interactive-page">
        <div class="page-banner" style="background:#047857;">
          <span>📄 Orijinal Öğretmen Çözüm Anahtarı Sayfa 4 & 5</span>
          <span style="font-size:0.85rem; opacity:0.85;">Resmi Çözümler</span>
        </div>
        <div class="pdf-image-wrap">
          <img src="assets/pdf_pages/din/page_4.png" alt="Din Cevap 4" loading="lazy">
        </div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
          <img src="assets/pdf_pages/din/page_5.png" alt="Din Cevap 5" loading="lazy">
        </div>
      </div>
    </div>

    <!-- TAB 3: SUMMARY -->
    <div id="summary-pane" class="tab-pane">
      <div class="summary-cards">
        <div class="summary-card">
          <h4>🌟 1. Esmâ-i Hüsnâ (Allah'ın Güzel İsimleri)</h4>
          <ul>
            <li><strong>Alîm:</strong> Her şeyi bilen.</li>
            <li><strong>Semî:</strong> Her şeyi işiten.</li>
            <li><strong>Basîr:</strong> Her şeyi gören.</li>
            <li><strong>Kadir:</strong> Her şeye gücü yeten.</li>
            <li><strong>Rahman & Rahim:</strong> Merhamet eden ve esirgeyen.</li>
          </ul>
        </div>
        <div class="summary-card">
          <h4>📖 2. İhlas Suresi ve Tevhit</h4>
          <ul>
            <li><strong>Tevhit:</strong> Allah'ın bir ve tek olduğuna iman etmektir. Zıttı şirk koşmaktır.</li>
            <li><strong>Ehad:</strong> Allah birdir, tektir.</li>
            <li><strong>Samed:</strong> Herkes O'na muhtaç, O hiçbir şeye muhtaç değildir.</li>
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

# =========================================================================
# 6. İNGİLİZCE (Bölüm A, B, C, D, E - Toplam 100 Puan)
# =========================================================================
def generate_ingilizce():
    qA = build_q_strip("A", "Fred's Weekly Schedule (Ders Programı)", 30, "ing_q1.mp3", "ing_sol1.mp3",
        "Part A. Answer the questions according to Fred's weekly timetable: 1. Total classes in a week, 2. Classes on Friday, 3. English class days.",
        "Part A solution. 1: Fred has twenty classes in a week. 2: On Friday he has Turkish, Music and Information Technologies. 3: Fred has English on Tuesday and Thursday.",
        "1. <strong>How many classes does Fred have in a week?</strong><br>→ <em>He has <strong>20 classes</strong> in a week.</em> (5 days × 4 classes)<br><br>2. <strong>Which classes does he have on Friday?</strong><br>→ <em>He has <strong>Turkish, Music and ICT</strong> (Information and Communication Technology).</em><br><br>3. <strong>When does Fred have English class?</strong><br>→ <em>He has English class on <strong>Tuesday and Thursday</strong>.</em>",
        "1: 20 classes\n2: Turkish, Music, ICT\n3: Tuesday and Thursday...")

    qB = build_q_strip("B", "Telling the Time (Saatleri Yazma)", 20, "ing_q2.mp3", "ing_sol2.mp3",
        "Part B. Look at the clocks and write down the time.",
        "Part B solution. Clock one: It is eleven o'clock. Clock two: It is quarter past seven. Clock three: It is quarter to ten. Clock four: It is half past seven.",
        "• 1. Saat (11:00): <strong>It's eleven o'clock.</strong><br>• 2. Saat (07:15): <strong>It's quarter past seven.</strong><br>• 3. Saat (09:45): <strong>It's quarter to ten.</strong><br>• 4. Saat (07:30): <strong>It's half past seven.</strong>",
        "1: It's eleven o'clock...\n2: It's quarter past seven...\n3: It's quarter to ten...\n4: It's half past seven...")

    qC = build_q_strip("C", "Mia's Daily Routine Reading Text", 40, "ing_q3.mp3", "ing_sol3.mp3",
        "Part C. Read the text about Mia's daily routine and answer the five comprehension questions.",
        "Part C solution. 1: She wakes up at 6:30 a.m. 2: Yes, she walks to school. 3: She plays volleyball with her friends in the park. 4: No, she has dinner at 7:00 p.m. 5: She plays with her friends.",
        "1. <strong>What time does Mia wake up?</strong><br>→ <em>She wakes up at <strong>6:30 a.m.</strong> every morning.</em><br><br>2. <strong>Does Mia walk to school?</strong><br>→ <em><strong>Yes, she does.</strong> (Because it is very close to her house.)</em><br><br>3. <strong>What does Mia do at 5:00 p.m.?</strong><br>→ <em>She <strong>plays volleyball with her friends in the park</strong>.</em><br><br>4. <strong>Does Mia have dinner at 6:00 p.m.?</strong><br>→ <em><strong>No, she doesn't.</strong> She has dinner at 7:00 p.m.</em><br><br>5. <strong>Who does Mia play volleyball with?</strong><br>→ <em>She plays volleyball <strong>with her friends</strong>.</em>",
        "1: At 6:30 a.m.\n2: Yes, she does.\n3: Plays volleyball...\n4: No, she doesn't.\n5: With her friends...")

    qD = build_q_strip("D", "Numbers in Words (Sayıların Yazılışı)", 6, "ing_q4.mp3", "ing_sol4.mp3",
        "Part D. Write the numbers in words: 92, 100, 65.",
        "Part D solution. 92 is ninety-two. 100 is one hundred. 65 is sixty-five.",
        "1. 92 = <strong>ninety-two</strong><br>2. 100 = <strong>one hundred</strong> (a hundred)<br>3. 65 = <strong>sixty-five</strong>",
        "1: ninety-two, 2: one hundred, 3: sixty-five...")

    qE = build_q_strip("E", "Must and Mustn't (Zorunluluk ve Yasaklar)", 4, "ing_q5.mp3", "ing_sol5.mp3",
        "Part E. Fill in the blanks with must or mustn't.",
        "Part E solution. 1 must follow rules. 2 mustn't use phones in library. 3 must be kind. 4 mustn't eat in lab.",
        "1. You <strong>must</strong> follow the rules at school. (Zorunluluk)<br>2. You <strong>mustn't</strong> use your mobile phones in the library. (Yasak)<br>3. You <strong>must</strong> be kind to your classmates. (Gereklilik)<br>4. You <strong>mustn't</strong> eat or drink in the lab. (Yasak)",
        "1: must, 2: mustn't, 3: must, 4: mustn't...")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>5. Sınıf İngilizce 1. Dönem 1. Yazılı - Tüm Sorular Çözümlü</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body class="theme-ingilizce">
  {get_header('ingilizce')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>🇬🇧</span> 5. Sınıf İngilizce 1. Dönem 1. Yazılı</h1>
        <p>School Life • Telling the Time • Daily Routines • Must / Mustn't • Tüm Bölümler A, B, C, D, E</p>
      </div>
      <div class="score-box">
        <div class="score-val" id="currentScoreVal">0</div>
        <div class="score-lbl">Score / 100</div>
      </div>
    </div>

    <!-- Audio Bar -->
    <div class="audio-bar">
      <div class="audio-bar-info">
        <div class="audio-icon-pulse">🔊</div>
        <div>
          <strong style="display:block; font-size:0.95rem;">English Teacher Audio Guide (PC & Mobile)</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Ready — Click audio buttons to listen</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Pause / Resume</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Stop</button>
        <button class="btn-audio primary" onclick="portalApp.playAudio('ing_summary.mp3', null, '5th Grade English 1st Term 1st Exam Summary. School life, telling the time, daily routines in simple present tense, numbers and rules with must and mustn\\'t.')">📢 Listen Unit Summary</button>
      </div>
    </div>

    <!-- Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="pdf-pane">📄 Orijinal PDF Üzerinde Tüm Soruları Çöz</button>
      <button class="tab-btn" data-tab="answer-key-pane">🔑 Answer Key (Cevap Anahtarı)</button>
      <button class="tab-btn" data-tab="summary-pane">💡 Revision Notes (Hap Bilgiler)</button>
    </div>

    <!-- TAB 1: WORKBENCH -->
    <div id="pdf-pane" class="tab-pane active">
      <div class="interactive-pdf-container">
        
        <!-- Sayfa 4 (Part A & B) -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Exam Paper Page 4 (Part A: Timetable, Part B: Clocks)</span>
            <span style="font-size:0.85rem; opacity:0.85;">50 Points</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/pdf_pages/ingilizce/page_4.png" alt="İngilizce Sayfa 4" loading="eager">
          </div>
          <div class="pdf-question-controls">
            {qA}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {qB}
          </div>
        </div>

        <!-- Sayfa 5 (Part C, D, E) -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 Exam Paper Page 5 (Part C: Reading, Part D: Numbers, Part E: Must/Mustn't)</span>
            <span style="font-size:0.85rem; opacity:0.85;">50 Points</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/pdf_pages/ingilizce/page_5.png" alt="İngilizce Sayfa 5" loading="lazy">
          </div>
          <div class="pdf-question-controls">
            {qC}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {qD}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {qE}
          </div>
        </div>

      </div>

      <div style="text-align: center; margin: 36px 0;">
        <button class="btn-start" style="padding: 18px 42px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 Calculate My English Score
        </button>
      </div>
    </div>

    <!-- TAB 2: ANSWER KEY -->
    <div id="answer-key-pane" class="tab-pane">
      <div class="pdf-interactive-page">
        <div class="page-banner" style="background:#047857;">
          <span>📄 Official Teacher Answer Key Pages (Pages 6 & 7)</span>
          <span style="font-size:0.85rem; opacity:0.85;">Official Solutions</span>
        </div>
        <div class="pdf-image-wrap">
          <img src="assets/pdf_pages/ingilizce/page_6.png" alt="İngilizce Cevap 6" loading="lazy">
        </div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
          <img src="assets/pdf_pages/ingilizce/page_7.png" alt="İngilizce Cevap 7" loading="lazy">
        </div>
      </div>
    </div>

    <!-- TAB 3: SUMMARY -->
    <div id="summary-pane" class="tab-pane">
      <div class="summary-cards">
        <div class="summary-card">
          <h4>⏰ 1. Telling the Time</h4>
          <ul>
            <li><strong>Tam saatler:</strong> It's two o'clock. (Saat 2:00)</li>
            <li><strong>Çeyrek geçe:</strong> It's quarter past four. (Saat 4:15)</li>
            <li><strong>Buçuk:</strong> It's half past six. (Saat 6:30)</li>
            <li><strong>Çeyrek kala:</strong> It's quarter to ten. (Saat 9:45)</li>
          </ul>
        </div>
        <div class="summary-card">
          <h4>🚫 2. Must & Mustn't</h4>
          <ul>
            <li><strong>Must:</strong> Yapılması zorunlu kurallar. (You must listen to your teacher.)</li>
            <li><strong>Mustn't:</strong> Yapılması kesinlikle yasak olanlar. (You mustn't run in the corridors.)</li>
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

print("Writing files...")
with open(r'd:\gpt\5_sinif_calisma_portali\sosyal-bilgiler.html', 'w', encoding='utf-8') as f:
    f.write(generate_sosyal())
with open(r'd:\gpt\5_sinif_calisma_portali\din-kulturu.html', 'w', encoding='utf-8') as f:
    f.write(generate_din())
with open(r'd:\gpt\5_sinif_calisma_portali\ingilizce.html', 'w', encoding='utf-8') as f:
    f.write(generate_ingilizce())
print("All 3 written!")
