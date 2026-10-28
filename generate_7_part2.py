# -*- coding: utf-8 -*-
"""
Generate 7th Grade Fen Bilimleri (9 Questions) and Din Kültürü (9 Questions)
"""

import os
from generate_7_part1 import get_header, get_footer, get_score_modal, build_q_strip

# =========================================================================
# 3. 7. SINIF FEN BİLİMLERİ (9 Soru - 100 Puan)
# =========================================================================
def generate_7_fen():
    q1 = build_q_strip(1, "Uzay Araçlarının Özellikleri Tablosu", 10, "fen7_q1.mp3", "fen7_sol1.mp3",
        "Soru 1. Yapay uydu, uzay istasyonu ve uzay mekiği için belirli bir yörüngede dolanma, içinde astronot bulundurma ve tekrar kullanılabilme özelliklerini VAR veya YOK olarak doldurunuz.",
        "Soru 1 çözümü. Yapay uydu: Yörüngede dolanma VAR, astronot YOK, tekrar kullanılabilme YOK. Uzay istasyonu: Yörüngede dolanma VAR, astronot VAR, tekrar kullanılabilme YOK. Uzay mekiği: Yörüngede dolanma VAR, astronot VAR, tekrar kullanılabilme VAR.",
        "• <strong>Yapay Uydu:</strong> Yörüngede Dolanma: <strong>VAR</strong> | Astronot: <strong>YOK</strong> | Tekrar Kullanılabilme: <strong>YOK</strong><br>• <strong>Uzay İstasyonu:</strong> Yörüngede Dolanma: <strong>VAR</strong> | Astronot: <strong>VAR</strong> | Tekrar Kullanılabilme: <strong>YOK</strong><br>• <strong>Uzay Mekiği:</strong> Yörüngede Dolanma: <strong>VAR</strong> | Astronot: <strong>VAR</strong> | Tekrar Kullanılabilme: <strong>VAR</strong>",
        "Yapay uydu: ... \nUzay istasyonu: ... \nUzay mekiği: ...")

    q2 = build_q_strip(2, "Mars Projesi Uzay Araçları Analizi", 15, "fen7_q2.mp3", "fen7_sol2.mp3",
        "Soru 2. Gökmen 1, Keşif X, Haberleşme TR ve Uluslararası Yaşam Merkezi araçlarını inceleyerek soruları cevaplayınız.",
        "Soru 2 çözümü. a: İki numaralı Keşif X uzay sondasıdır çünkü insansız robotik araştırma aracıdır. b: Her iki araç da Mars yörüngesinde dolanmaktadır. c: Gökmen 1 bir uzay roketidir ve fırlatma görevi görür, Keşif X ise uzay sondasıdır ve bilimsel veri toplar.",
        "<strong>a) Uzay Sondası:</strong> <strong>2 numaralı Keşif-X</strong> aracıdır. Çünkü içinde astronot bulunmayan, gök cisimlerini uzaktan veya yüzeyden incelemek için gönderilen robotik araçtır.<br><br><strong>b) Ortak Özellik:</strong> Her iki araç da <strong>Mars yörüngesinde dolanmaktadır</strong>.<br><br><strong>c) Temel Fark:</strong> Gökmen-1 bir <strong>uzay roketidir</strong> (astronot ve yükleri uzaya taşır/fırlatır). Keşif-X ise bir <strong>uzay sondasıdır</strong> (ulaştığı yüzeyde veri ve numune toplayıp analiz yapar).",
        "a) Uzay sondası ve nedeni: ... \nb) Ortak özellik: ... \nc) Temel fark: ...")

    q3 = build_q_strip(3, "Uzay Kirliliği Problemi ve Çözüm Yolları", 10, "fen7_q3.mp3", "fen7_sol3.mp3",
        "Soru 3. Uzay kirliliği nedir, gelecekte günlük hayatımızda ne gibi aksaklıklara yol açabilir ve çözüm önerilerini değerlendiriniz.",
        "Soru 3 çözümü. a: Problem uzay kirliliğidir, işlevsiz uyduların ve roket parçalarının çarpışma riski oluşturmasıdır. b: Aktif uydulara çarparsa televizyon yayınları, hava durumu ve navigasyon GPS sistemleri çöker. c: Atmosfere çekip yakmak veya dev ağlarla toplamak yöntemleri değerlendirilir.",
        "<strong>a) Problem:</strong> <strong>Uzay Kirliliği</strong>. Görevini tamamlamış uyduların ve roket enkazlarının yörüngede birikmesidir.<br><br><strong>b) Günlük Hayata Etkileri:</strong> Aktif uydulara çarparak hasar vermesi durumunda <strong>GPS (navigasyon) sistemleri bozulabilir, TV ve internet yayınları kesilebilir, hava tahminleri yapılamaz</strong>.<br><br><strong>c) Çözüm Değerlendirmesi:</strong> 1. Yöntem (atmosferde yakmak) çöpleri tamamen yok ettiği için kalıcıdır; ancak çok yüksek irtifadaki uyduları atmosfere çekmek zor olduğundan 2. yöntem (robotik ağ/kıskaç ile toplamak) daha kontrollü bir çözümdür.",
        "a) Problem ve nedeni: ... \nb) Olası aksaklıklar: ... \nc) Seçtiğiniz çözüm: ...")

    q4 = build_q_strip(4, "Yıldızların Yaşam Döngüsü ve Kara Delik", 10, "fen7_q4.mp3", "fen7_sol4.mp3",
        "Soru 4. Yıldızların doğum yeri olan yapı nedir ve Güneş yaşamının sonunda bir kara deliğe dönüşebilir mi?",
        "Soru 4 çözümü. a: Yıldızların ortak doğum yeri bulutsu yani nebuladır. Süpernova için başlangıçta büyük kütleli olmalıdır. b: Hayır, Güneş küçük kütleli olduğu için kara deliğe dönüşemez, beyaz cüce olarak ömrünü tamamlar.",
        "<strong>a) Doğum Yeri ve Kütle:</strong> Tüm yıldızların doğum yeri <strong>Bulutsu (Nebula)</strong>'dur. Süpernova patlaması için başlangıçta <strong>büyük kütleli</strong> bir yıldız olması gerekir.<br><br><strong>b) Güneş Kara Delik Olur mu?</strong> <strong>Hayır, beklenemez.</strong> Çünkü Güneş orta büyüklükte (küçük kütleli) bir yıldızdır. Sadece büyük kütleli yıldızlar süpernova geçirip kara delik veya nötron yıldızına dönüşür; Güneş ise kızıl devden sonra <strong>beyaz cüce</strong> olarak ömrünü tamamlayacaktır.",
        "a) Doğum yeri ve kütle: ... \nb) Güneş kara delik olur mu? ...")

    q5 = build_q_strip(5, "X, Y, Z Gök Cisimlerinin Bilimsel Karşılıkları", 10, "fen7_q5.mp3", "fen7_sol5.mp3",
        "Soru 5. Kendini tanıtan X, Y ve Z gök cisimlerinin adlarını yazınız ve son evrelerinin neden farklı olduğunu açıklayınız.",
        "Soru 5 çözümü. X bulutsu yani nebula, Y kara delik, Z küçük kütleli yıldız yani Güneştir. Farkın nedeni yıldızların başlangıçtaki kütlelerinin farklı olmasıdır.",
        "<strong>a) Kavram Karşılıkları:</strong><br>• <strong>X:</strong> <strong>Bulutsu (Nebula)</strong><br>• <strong>Y:</strong> <strong>Kara Delik</strong> (Büyük kütleli yıldızın sonu)<br>• <strong>Z:</strong> <strong>Küçük Kütleli Yıldız / Güneş</strong> (Sonu beyaz cüce)<br><br><strong>b) Farkın Temel Nedeni:</strong> Yıldızların <strong>başlangıçtaki kütleleridir</strong>. Başlangıç kütlesi büyük olan yıldızlar süpernovayla kara deliğe dönüşürken, küçük kütleli olanlar patlama yapmadan beyaz cüceye dönüşür.",
        "X: ... \nY: ... \nZ: ... \nb) Temel farkın nedeni: ...")

    q6 = build_q_strip(6, "Evren, Galaksi ve Yıldız Kavramları", 10, "fen7_q6.mp3", "fen7_sol6.mp3",
        "Soru 6. Bahsedilen kavramları büyükten küçüğe sıralayınız ve boşlukları doldurunuz.",
        "Soru 6 çözümü. a: Evren büyüktür Galaksi büyüktür Yıldız. b: 1 Samanyolu galaksisi, 2 Evren, 3 Yıldız.",
        "<strong>a) Kavramlar ve Büyükten Küçüğe Sıralaması:</strong><br><strong>Evren > Galaksi (Gök Ada) > Yıldız</strong><br><br><strong>b) Cümle Tamamlama:</strong><br>1. Galaksimizin adı: <strong>Samanyolu</strong> galaksisidir.<br>2. En büyük yapıya: <strong>Evren</strong> denir.<br>3. Küresel gök cisimlerine: <strong>Yıldız</strong> denir.",
        "a) Sıralama: ... \nb) 1: ..., 2: ..., 3: ...")

    q7 = build_q_strip(7, "Fiziksel Anlamda İş Kavramı", 10, "fen7_q7.mp3", "fen7_sol7.mp3",
        "Soru 7. Sandığı iten kişi ile poşetleri yatay taşıyan kişiden hangisi fiziksel anlamda iş yapmıştır ve şartı nedir?",
        "Soru 7 çözümü. a: Sandığı iterek hareket ettiren kişi iş yapmıştır. b: Fiziksel anlamda iş sayılması için uygulanan kuvvet ile cismin hareket yönü aynı doğrultuda olmalıdır.",
        "<strong>a) İş Yapan Kişi:</strong> <strong>Görsel 1'deki kişi (Sandığı iterek hareket ettiren)</strong> fiziksel anlamda iş yapmıştır.<br><br><strong>b) İş Olma Şartı:</strong> Bir eylemin fiziksel anlamda iş sayılabilmesi için cisme bir <strong>kuvvet uygulanmalı</strong> ve cisim bu <strong>kuvvetle aynı doğrultuda yol almalıdır</strong>. Görsel 2'de kuvvet yukarı yönlü, hareket yatay doğrultuda (birbirine dik) olduğu için iş yapılmamıştır.",
        "a) İş yapan kişi: ... \nb) Fiziksel iş şartı: ...")

    q8 = build_q_strip(8, "Haltercinin Durumlarında İş Analizi", 15, "fen7_q8.mp3", "fen7_sol8.mp3",
        "Soru 8. Haltercinin halteri kaldırdığı 1. durum ve sabit tuttuğu 2. durumda fiziksel anlamda iş yapılmış mıdır?",
        "Soru 8 çözümü. 1. durumda yukarı yönlü kuvvet uygulanmış ve halter yukarı hareket ettiği için iş yapılmıştır. 2. durumda halter sabit durduğu ve yer değiştirmediği için iş yapılmamıştır.",
        "• <strong>1. Durum (Kaldırma Anı):</strong> <strong>EVET, iş yapılmıştır.</strong> Çünkü halterci yukarı yönde kuvvet uygulamış ve halter bu kuvvet doğrultusunda yukarı doğru yer değiştirmiştir (yol almıştır).<br><br>• <strong>2. Durum (Sabit Tutma Anı):</strong> <strong>HAYIR, iş yapılmamıştır.</strong> Çünkü halter sabit tutulduğu için yer değiştirme (yol alma) sıfırdır. Yol alınmadığı sürece kuvvet uygulansa bile fiziksel iş yapılmaz.",
        "1. Durum: ... \n2. Durum: ...")

    q9 = build_q_strip(9, "Kinetik ve Potansiyel Enerji Karşılaştırması", 10, "fen7_q9.mp3", "fen7_sol9.mp3",
        "Soru 9. Dalda duran elmanın ve yere düşen elmanın sahip olduğu enerji çeşitlerini ve aralarındaki farkı açıklayınız.",
        "Soru 9 çözümü. a: Dalda duran elma çekim potansiyel enerjisine sahiptir, kütleye ve yüksekliğe bağlıdır. b: Düşen elma kinetik enerjiye sahiptir. c: Kinetik enerji hareketten ve süratten, potansiyel enerji ise konumdan ve yükseklikten kaynaklanır.",
        "<strong>a) Dalda Duran Elma:</strong> <strong>Çekim Potansiyel Enerjisi</strong>'ne sahiptir. Bu enerji elmanın <strong>kütlesine</strong> ve yerden olan <strong>yüksekliğine</strong> bağlıdır.<br><br><strong>b) Düşmekte Olan Elma:</strong> Hareketinden dolayı <strong>Kinetik Enerji</strong> kazanır.<br><br><strong>c) Temel Fark:</strong> Kinetik enerji cismin <strong>hareket durumundan (süratinden)</strong> dolayı ortaya çıkarken, çekim potansiyel enerjisi cismin bulunduğu <strong>konumdan (yerden yüksekliğinden)</strong> kaynaklanır.",
        "a) Duran elma: ... \nb) Düşen elma: ... \nc) İki enerjinin temel farkı: ...")

    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>7. Sınıf Fen Bilimleri 1. Dönem 1. Yazılı - MEBİ Soruları ve Çözümleri</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body class="theme-fen">
  {get_header('fen7')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>🔬</span> 7. Sınıf Fen Bilimleri 1. Dönem 1. Yazılı (MEBİ)</h1>
        <p>Uzay Araştırmaları • Yıldızların Yaşamı • Fiziksel İş ve Enerji Dönüşümleri • 9 Sorunun Tamamı</p>
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
          <strong style="display:block; font-size:0.95rem;">Fen Bilimleri MEBİ Sesli Rehber</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır — Dinlemek için ses butonlarına tıklayın</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.speakText('7. Sınıf Fen Bilimleri 1. Dönem 1. Yazılı MEBİ Konu Özeti. Uzay araştırmaları, yapay uydu, uzay sondası ve uzay kirliliği, bulutsudan yıldızların doğumu ve süpernova patlaması ile kara delik oluşumu, fiziksel anlamda iş şartı kuvvet ve yol doğrultusu ilişkisi, kinetik ve çekim potansiyel enerjisi sınavın temel konularıdır.')">📢 Sınav Konu Özetini Dinle</button>
      </div>
    </div>

    <!-- Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="pdf-pane">📄 Orijinal MEBİ PDF'i Üzerinde Soruları Çöz</button>
      <button class="tab-btn" data-tab="answer-key-pane">🔑 Resmi Çözümler (Sayfa 10 & 11)</button>
    </div>

    <!-- TAB 1: WORKBENCH -->
    <div id="pdf-pane" class="tab-pane active">
      <div class="interactive-pdf-container">
        
        <!-- Sayfa 1 -->
        <div class="pdf-interactive-page">
          <div class="page-banner"><span>📄 MEBİ Soru Kitapçığı - Sayfa 1 (Soru 1)</span><span>10 Puan</span></div>
          <div class="pdf-image-wrap"><img src="assets/pdf_pages/fen_mebi/page_1.png" alt="Fen Sayfa 1" loading="eager"></div>
          <div class="pdf-question-controls">{q1}</div>
        </div>

        <!-- Sayfa 2 & 3 -->
        <div class="pdf-interactive-page">
          <div class="page-banner"><span>📄 MEBİ Soru Kitapçığı - Sayfa 2 & 3 (Soru 2, Soru 3)</span><span>25 Puan</span></div>
          <div class="pdf-image-wrap"><img src="assets/pdf_pages/fen_mebi/page_2.png" alt="Fen Sayfa 2" loading="lazy"></div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/fen_mebi/page_3.png" alt="Fen Sayfa 3" loading="lazy"></div>
          <div class="pdf-question-controls">{q2}<hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">{q3}</div>
        </div>

        <!-- Sayfa 4, 5, 6 -->
        <div class="pdf-interactive-page">
          <div class="page-banner"><span>📄 MEBİ Soru Kitapçığı - Sayfa 4, 5 & 6 (Soru 4, Soru 5, Soru 6)</span><span>30 Puan</span></div>
          <div class="pdf-image-wrap"><img src="assets/pdf_pages/fen_mebi/page_4.png" alt="Fen Sayfa 4" loading="lazy"></div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/fen_mebi/page_5.png" alt="Fen Sayfa 5" loading="lazy"></div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/fen_mebi/page_6.png" alt="Fen Sayfa 6" loading="lazy"></div>
          <div class="pdf-question-controls">{q4}<hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">{q5}<hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">{q6}</div>
        </div>

        <!-- Sayfa 7, 8, 9 -->
        <div class="pdf-interactive-page">
          <div class="page-banner"><span>📄 MEBİ Soru Kitapçığı - Sayfa 7, 8 & 9 (Soru 7, Soru 8, Soru 9)</span><span>35 Puan</span></div>
          <div class="pdf-image-wrap"><img src="assets/pdf_pages/fen_mebi/page_7.png" alt="Fen Sayfa 7" loading="lazy"></div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/fen_mebi/page_8.png" alt="Fen Sayfa 8" loading="lazy"></div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/fen_mebi/page_9.png" alt="Fen Sayfa 9" loading="lazy"></div>
          <div class="pdf-question-controls">{q7}<hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">{q8}<hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">{q9}</div>
        </div>

      </div>

      <div style="text-align: center; margin: 36px 0;">
        <button class="btn-start" style="padding: 18px 42px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 7. Sınıf Fen Bilimleri Notumu Hesapla
        </button>
      </div>
    </div>

    <!-- TAB 2: OFFICIAL SOLUTIONS -->
    <div id="answer-key-pane" class="tab-pane">
      <div class="pdf-interactive-page">
        <div class="page-banner" style="background:#047857;">
          <span>📄 MEBİ Resmi Öğretmen Çözüm Anahtarı (Sayfa 10 & 11)</span>
          <span style="font-size:0.85rem; opacity:0.85;">Temel Eğitim Genel Müdürlüğü</span>
        </div>
        <div class="pdf-image-wrap"><img src="assets/pdf_pages/fen_mebi/page_10.png" alt="Çözüm 10" loading="lazy"></div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/fen_mebi/page_11.png" alt="Çözüm 11" loading="lazy"></div>
      </div>
    </div>

  </main>

  {get_score_modal()}
  {get_footer()}

  <script src="assets/js/app.js"></script>
  <script>
    initLesson('fen_7', 'tr-TR');
  </script>
</body>
</html>
"""

# =========================================================================
# 4. 7. SINIF DİN KÜLTÜRÜ (9 Soru - 100 Puan)
# =========================================================================
def generate_7_din():
    q1 = build_q_strip(1, "Varlıklar Âlemi ve Meleklerin Özellikleri", 10, "din7_q1.mp3", "din7_sol1.mp3",
        "Soru 1. Ahmet'in düşüncesinden hareketle meleklerin varlığı ve duyu organlarıyla algılanamaması durumunu açıklayınız.",
        "Soru 1 çözümü. Melekler gözle görülemeyen nurani varlıklardır. Varlıkları vahiy yoluyla yani Kuran ve peygamberimizin bildirmesiyle bilinir.",
        "<strong>Meleklerin Özellikleri:</strong><br>Melekler duyu organlarımızla (göz, kulak vb.) algılanamayan, nurdan yaratılmış ruhani varlıklardır. Gözle görülememeleri onların yok olduğu anlamına gelmez; akıl, rüzgar ve elektrik gibi meleklerin varlığını da Allah'ın peygamberleri aracılığıyla bildirdiği vahiy sayesinde kesin olarak biliriz.",
        "Meleklerin varlığı ve algılanamaması hakkında açıklamanızı yazınız...")

    q2 = build_q_strip(2, "Dört Büyük Melek ve Görevleri Tablosu", 15, "din7_q2.mp3", "din7_sol2.mp3",
        "Soru 2. Dört büyük meleğin isimlerini ve görevlerini yazınız.",
        "Soru 2 çözümü. Cebrail vahiy getirmekle, Mikail tabiat olaylarını düzenlemekle, İsrafil sura üflemekle, Azrail ise eceli gelen canlıların canını almakla görevlidir.",
        "• <strong>Cebrail (a.s.):</strong> Allah'ın emir ve vahiylerini peygamberlere iletmekle görevlidir.<br>• <strong>Mikâil (a.s.):</strong> Yağmur, rüzgâr gibi tabiat olaylarını ve rızıkları idare etmekle görevlidir.<br>• <strong>İsrâfil (a.s.):</strong> Kıyamet günü ve yeniden dirilişte Sûr borusuna üflemekle görevlidir.<br>• <strong>Azrâil (a.s.):</strong> Eceli gelen canlıların ruhunu teslim almakla görevlidir.",
        "Cebrail, Mikail, İsrafil, Azrail görevleri...")

    q3 = build_q_strip(3, "Diğer Melekler (Kirâmen Kâtibîn, Münker-Nekir)", 10, "din7_q3.mp3", "din7_sol3.mp3",
        "Soru 3. Kabirde sorgu yapan ve insanların amellerini yazan meleklerin adlarını yazınız.",
        "Soru 3 çözümü. İyilik ve kötülükleri yazan melekler Kiramen Katibin, kabirde sorgulayan melekler Münker ve Nekirdir.",
        "• <strong>İnsanların sevap ve günahlarını kaydeden melekler:</strong> <strong>Kirâmen Kâtibîn</strong> (Yazıcı Melekler)<br>• <strong>Kabirde insanları sorguya çeken melekler:</strong> <strong>Münker ve Nekir</strong><br>• <strong>Cennet ve cehennem görevlisi melekler:</strong> Rıdvan (Cennet) ve Mâlik (Cehennem)",
        "Kirâmen Kâtibîn, Münker-Nekir...")

    q4 = build_q_strip(4, "Ahiret Hayatının Aşamaları (Kıyamet, Baas, Haşr, Mizan)", 15, "din7_q4.mp3", "din7_sol4.mp3",
        "Soru 4. Ayetlerde bahsedilen ahiret aşamalarını tespit ediniz: Baas, Haşr, Mizan, Cennet ve Cehennem.",
        "Soru 4 çözümü. Kabirlerden çıkıp dirilme Baas, toplanma meydanı Mahşer ve Haşr, amellerin tartılması Mizan, amellere göre gidecek yer Cennet veya Cehennemdir.",
        "• <strong>Ölümden sonra yeniden diriliş:</strong> <strong>Ba's (Yeniden Diriliş)</strong><br>• <strong>İnsanların toplanması ve toplanma yeri:</strong> <strong>Haşr ve Mahşer</strong><br>• <strong>Amellerin, sevap ve günahların tartıldığı ilahi adalet terazisi:</strong> <strong>Mîzan</strong><br>• <strong>Sorgu ve hesap sonrası ebedi kalış yerleri:</strong> <strong>Cennet veya Cehennem</strong>",
        "Baas, Haşr, Mizan, Cennet/Cehennem...")

    q5 = build_q_strip(5, "Ömür, Ecel ve Ahiret Sorumluluğu", 10, "din7_q5.mp3", "din7_sol5.mp3",
        "Soru 5. Canlıların yaşam süresinin sınırlı olması, ömür ve ecel kavramları ile ahiret bilinci ilişkisini açıklayınız.",
        "Soru 5 çözümü. Her canlının bir eceli vardır. Ömür bir emanettir. Ahirete inanan insan zamanını ve ömrünü faydalı amellerle değerlendirir.",
        "<strong>Ömür, Ecel ve Sorumluluk:</strong><br>Her canlının Allah tarafından takdir edilmiş bir yaşam süresi (<strong>ömür</strong>) ve bu sürenin sona erdiği an (<strong>ecel</strong>) vardır. Ahiret inancına sahip birey, dünyanın geçici bir imtihan yeri olduğunu bilir; bu yüzden ömrünü güzel ahlakla, kul hakkından sakınarak ve topluma faydalı amellerle geçirir.",
        "Ömür, ecel ve sorumluluk bilincini açıklayınız...")

    q6 = build_q_strip(6, "Amel Defteri ve İlahi Adalet", 10, "din7_q6.mp3", "din7_sol6.mp3",
        "Soru 6. İnsanların bölük bölük kabirlerinden çıkması ve amel defterlerinin verilmesi neyi ifade eder?",
        "Soru 6 çözümü. Kıyametten sonraki yeniden dirilişi yani baası ve herkesin dünyada yaptıklarının hesabını vereceği ilahi adaleti ifade eder.",
        "<strong>Açıklama:</strong><br>İnsanların kabirlerinden çıkması <strong>yeniden dirilişi (ba's)</strong> simgeler. Herkesin dünyada yaptığı zerre kadar hayrın da şerrin de kaydedildiği <strong>amel defteri</strong> kendisine verilerek eksiksiz bir adaletle hesaba çekilecektir.",
        "Açıklamanızı yazınız...")

    q7 = build_q_strip(7, "Melek ve Ahiret İnancının İnsana Kazandırdıkları", 10, "din7_q7.mp3", "din7_sol7.mp3",
        "Soru 7. Melek ve ahiret inancının bireyin davranışlarına ve iç huzuruna sağladığı iki katkıyı yazınız.",
        "Soru 7 çözümü. 1: Kişi daima gözetlendiğini bilerek kötülüklerden ve haksızlıktan uzak durur. 2: Adaletin tecelli edeceğini bilerek zorluklar karşısında sabreder ve ümitsizliğe düşmez.",
        "1. <strong>Otokontrol ve Sorumluluk Bilinci:</strong> İnsan meleklerin kendisini kaydettiğini bildiği için kimsenin görmediği yerlerde bile yalandan, hırsızlıktan ve kötülükten uzak durur.<br>2. <strong>İç Huzur ve Adalet İnancı:</strong> Dünyada haksızlığa uğrasa bile ahirette hakkını alacağını bilmek insanı teselli eder, ölüm korkusunu hafifletir ve huzur verir.",
        "İki temel katkıyı yazınız...")

    q8 = build_q_strip(8, "İnanç ve İnsan Davranışı İlişkisi", 10, "din7_q8.mp3", "din7_sol8.mp3",
        "Soru 8. Eren ve Selma'nın diyalogundan hareketle inancın amele ve ahlaka yansımasını açıklayınız.",
        "Soru 8 çözümü. İnanç sadece dille söylemekten ibaret değildir. Gerçek iman, dürüstlük, merhamet ve yardımseverlik gibi ahlaki davranışlarla hayat bulur.",
        "<strong>İnanç-Ahlak İlişkisi:</strong><br>İnanç, insanın tutum ve davranışlarının temel belirleyicisidir. Allah'a ve ahirete samimiyetle inanan bir kişi, inancını sözde bırakmaz; dürüst, adil, yardımsever ve merhametli davranarak inancını ahlakına yansıtır.",
        "Açıklamanızı yazınız...")

    q9 = build_q_strip(9, "Hz. İsa'nın Hayatı ve Mucizeleri", 10, "din7_q9.mp3", "din7_sol9.mp3",
        "Soru 9. Kur'an-ı Kerim'de bildirilen Hz. İsa'nın hayatına dair iki temel özelliği veya mucizesini yazınız.",
        "Soru 9 çözümü. Babasız dünyaya gelmesi, beşikteyken konuşması, çamurdan kuş yapıp canlandırması, hastaları iyileştirmesi ve kendisine İncil verilmiş olmasıdır.",
        "• <strong>Babası olmadan, mucizevi şekilde Hz. Meryem'den dünyaya gelmiştir.</strong><br>• <strong>Henüz beşikte bir bebekken konuşmuştur.</strong><br>• <strong>Allah'ın izniyle körleri ve alacalı hastaları iyileştirmiş, ölüleri diriltmiştir.</strong><br>• <strong>Kendisine dört büyük kutsal kitaptan biri olan İncil verilmiştir.</strong>",
        "Hz. İsa'nın iki mucizesini yazınız...")

    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>7. Sınıf Din Kültürü 1. Dönem 1. Yazılı - MEBİ Soruları ve Çözümleri</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body class="theme-din">
  {get_header('din7')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>🕌</span> 7. Sınıf Din Kültürü 1. Dönem 1. Yazılı (MEBİ)</h1>
        <p>Melek ve Ahiret İnancı • Dört Büyük Melek • Ahiretin Aşamaları • 9 Sorunun Tamamı Çözümlü</p>
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
          <strong style="display:block; font-size:0.95rem;">Din Kültürü MEBİ Sesli Rehber</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır — Dinlemek için ses butonlarına tıklayın</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.speakText('7. Sınıf Din Kültürü 1. Dönem 1. Yazılı MEBİ Konu Özeti. Varlıklar alemi ve melekler, dört büyük melek Cebrail, Mikail, İsrafil ve Azrail, Kiramen Katibin ve Münker Nekir melekleri, ahiret hayatının aşamaları ölüm, kıyamet, baas, haşr, mizan, cennet ve cehennem ile ahiret inancının insan davranışlarına etkisi sınavın temel konularıdır.')">📢 Sınav Konu Özetini Dinle</button>
      </div>
    </div>

    <!-- Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="pdf-pane">📄 Orijinal MEBİ PDF'i Üzerinde Soruları Çöz</button>
      <button class="tab-btn" data-tab="answer-key-pane">🔑 Resmi Çözümler (Sayfa 6, 7, 8)</button>
    </div>

    <!-- TAB 1: WORKBENCH -->
    <div id="pdf-pane" class="tab-pane active">
      <div class="interactive-pdf-container">
        
        <!-- Sayfa 1 & 2 -->
        <div class="pdf-interactive-page">
          <div class="page-banner"><span>📄 MEBİ Soru Kitapçığı - Sayfa 1 & 2 (Soru 1, Soru 2, Soru 3, Soru 4)</span><span>50 Puan</span></div>
          <div class="pdf-image-wrap"><img src="assets/pdf_pages/din_mebi/page_1.png" alt="Din Sayfa 1" loading="eager"></div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/din_mebi/page_2.png" alt="Din Sayfa 2" loading="lazy"></div>
          <div class="pdf-question-controls">{q1}<hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">{q2}<hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">{q3}<hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">{q4}</div>
        </div>

        <!-- Sayfa 3, 4, 5 -->
        <div class="pdf-interactive-page">
          <div class="page-banner"><span>📄 MEBİ Soru Kitapçığı - Sayfa 3, 4 & 5 (Soru 5, 6, 7, 8, 9)</span><span>50 Puan</span></div>
          <div class="pdf-image-wrap"><img src="assets/pdf_pages/din_mebi/page_3.png" alt="Din Sayfa 3" loading="lazy"></div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/din_mebi/page_4.png" alt="Din Sayfa 4" loading="lazy"></div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/din_mebi/page_5.png" alt="Din Sayfa 5" loading="lazy"></div>
          <div class="pdf-question-controls">{q5}<hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">{q6}<hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">{q7}<hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">{q8}<hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">{q9}</div>
        </div>

      </div>

      <div style="text-align: center; margin: 36px 0;">
        <button class="btn-start" style="padding: 18px 42px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 7. Sınıf Din Kültürü Notumu Hesapla
        </button>
      </div>
    </div>

    <!-- TAB 2: OFFICIAL SOLUTIONS -->
    <div id="answer-key-pane" class="tab-pane">
      <div class="pdf-interactive-page">
        <div class="page-banner" style="background:#047857;">
          <span>📄 MEBİ Resmi Öğretmen Çözüm Anahtarı (Sayfa 6, 7, 8)</span>
          <span style="font-size:0.85rem; opacity:0.85;">Temel Eğitim Genel Müdürlüğü</span>
        </div>
        <div class="pdf-image-wrap"><img src="assets/pdf_pages/din_mebi/page_6.png" alt="Çözüm 6" loading="lazy"></div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/din_mebi/page_7.png" alt="Çözüm 7" loading="lazy"></div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/din_mebi/page_8.png" alt="Çözüm 8" loading="lazy"></div>
      </div>
    </div>

  </main>

  {get_score_modal()}
  {get_footer()}

  <script src="assets/js/app.js"></script>
  <script>
    initLesson('din_7', 'tr-TR');
  </script>
</body>
</html>
"""

out_dir = r"d:\gpt\5_sinif_calisma_portali"
with open(os.path.join(out_dir, "7-fen-bilimleri.html"), "w", encoding="utf-8") as f:
    f.write(generate_7_fen())
with open(os.path.join(out_dir, "7-din-kulturu.html"), "w", encoding="utf-8") as f:
    f.write(generate_7_din())
print("7-fen-bilimleri.html and 7-din-kulturu.html created!")
