# -*- coding: utf-8 -*-
"""
Generate complete 7th Grade MEBİ Interactive Study Pages:
- 7-turkce.html (10 Questions)
- 7-sosyal-bilgiler.html (5 Questions)
- 7-fen-bilimleri.html (9 Questions)
- 7-ingilizce.html (10 Questions)
- 7-din-kulturu.html (9 Questions)
- 7-matematik.html (22 Questions)
Each page has direct HD PDF page background, audio reading, official solutions, student writing boxes, and grading.
"""

import os, sys

def get_header(active_tab="home"):
    links = [
        ("index.html", "🏠 Ana Sayfa", "home"),
        ("7-turkce.html", "📚 7. Türkçe", "turkce7"),
        ("7-matematik.html", "📐 7. Matematik", "mat7"),
        ("7-fen-bilimleri.html", "🔬 7. Fen", "fen7"),
        ("7-sosyal-bilgiler.html", "🌍 7. Sosyal", "sosyal7"),
        ("7-din-kulturu.html", "🕌 7. Din", "din7"),
        ("7-ingilizce.html", "🇬🇧 7. İngilizce", "ing7"),
        ("turkce.html", "📘 5. Sınıf Portalı", "5sinif"),
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
          <span class="brand-badge" style="background: linear-gradient(135deg, #0f766e, #0d9488);">7. SINIF MEBİ</span>
          <span>Yazılıya Hazırlık Portalı</span>
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
        <p style="font-weight: 700; color: #1e293b; font-size: 1rem;">7. Sınıf MEBİ Yazılıya Hazırlık Portalı</p>
        <p style="margin-top: 4px;">Tüm Sorular Çözümlü • Orijinal MEBİ PDF'leri Üzerinde Doğrudan Çalışma • PC, Telefon, Tablet, Smart TV Uyumlu</p>
        <p style="margin-top: 8px; font-size: 0.82rem; color: #94a3b8;">Temel Eğitim Genel Müdürlüğü Müfredat Uyumlu</p>
      </div>
    </footer>
    """

def get_score_modal():
    return """
    <div id="scoreModal" class="modal-overlay">
      <div class="modal-content">
        <h2>🎉 Sınav Tamamlandı!</h2>
        <div class="modal-score" id="finalScoreVal">100</div>
        <p style="font-weight: 700; color: #64748b; margin-bottom: 12px;">Toplam Başarı Puanı / 100</p>
        <p id="scoreFeedback" style="font-size: 1.05rem; line-height: 1.5; color: #334155;">Harika bir çalışma gerçekleştirdin!</p>
        <button class="btn-modal" onclick="portalApp.closeModal()">Kapat ve İncelemeye Devam Et</button>
      </div>
    </div>
    """

def build_q_strip(q_num, title, points, q_audio, sol_audio, q_speak_text, sol_speak_text, solution_html, placeholder="Cevabınızı buraya yazınız..."):
    q_speak_esc = q_speak_text.replace("'", "\\'").replace('"', '&quot;').replace('\n', ' ')
    sol_speak_esc = sol_speak_text.replace("'", "\\'").replace('"', '&quot;').replace('\n', ' ')
    sol_id = f"sol_reveal_7_{q_num}"

    return f"""
    <div class="q-strip" id="q_strip_7_{q_num}">
      <div class="q-strip-header">
        <div class="q-strip-title">
          <span class="q-num-badge" style="background:#ccfbf1; color:#0f766e;">Soru {q_num}</span>
          <strong>{title}</strong>
          <span class="q-pts-pill">{points} Puan</span>
        </div>
        <div class="q-strip-actions">
          <button class="btn-q-action audio-play" onclick="portalApp.playAudio('{q_audio}', 'q_strip_7_{q_num}', '{q_speak_esc}')">🔊 Soruyu Dinle</button>
          <button class="btn-q-action audio-sol" onclick="portalApp.playAudio('{sol_audio}', 'q_strip_7_{q_num}', '{sol_speak_esc}')">🎙️ Çözümü Dinle</button>
          <button class="btn-q-action solution-btn" onclick="portalApp.toggleSolution('{sol_id}')">✅ Çözümü Aç / Kapat</button>
        </div>
      </div>
      <textarea class="student-input-box" placeholder="{placeholder}"></textarea>
      <div id="{sol_id}" class="q-solution-reveal">
        <div class="sol-title">📌 MEBİ Resmi Öğretmen Çözümü & Model Yanıt:</div>
        <div class="sol-body">{solution_html}</div>
        <div class="self-grading">
          <span>Puanlama:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q7_{q_num}', {points}, {points}, this)">{points} Puan (Tam Doğru)</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q7_{q_num}', {points}, {points//2}, this)">{points//2} Puan (Kısmi)</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q7_{q_num}', {points}, 0, this)">0 Puan</button>
        </div>
      </div>
    </div>
    """

# =========================================================================
# 1. 7. SINIF TÜRKÇE (10 Soru - 100 Puan)
# =========================================================================
def generate_7_turkce():
    q1 = build_q_strip(1, "Hürkuş Metninden Kelime Tahmini", 10, "turkce7_q1.mp3", "turkce7_sol1.mp3",
        "Soru 1. Hürkuş metninden hareketle; keşif, teçhizat ve manevra kelimelerinin anlamlarını tahmin ediniz.",
        "Soru 1 çözümü. Keşif: Gizli olan bir şey hakkında geniş bilgi edinme veya araştırma yaparak yeni bilgiler elde etme. Teçhizat: Silah dışındaki savaş gereçleri, araç gereçlerin tümü. Manevra: Bir araca istenilen hareketi yaptırmak veya yönünü değiştirmek.",
        "• <strong>a. Keşif:</strong> Gizli olan veya bilinmeyen bir yer, durum hakkında geniş bilgi edinme, inceleyip araştırma yapma.<br>• <strong>b. Teçhizat:</strong> Bir görev için gerekli olan araç gereçlerin, alet ve teknik donanımların tümü.<br>• <strong>c. Manevra:</strong> Bir araca istenilen hareketi yaptırmak, yönünü değiştirmek veya kontrol etmek.",
        "a. keşif: ... \nb. teçhizat: ... \nc. manevra: ...")

    q2 = build_q_strip(2, "Arılar Metninin Konusu", 10, "turkce7_q2.mp3", "turkce7_sol2.mp3",
        "Soru 2. Arıların doğadaki rolünü anlatan metnin konusunu yazınız.",
        "Soru 2 çözümü. Metnin konusu, arıların doğadaki önemi, bitkilerin tozlaşmasına katkısı ve doğadaki yaşam dengesindeki rolüdür.",
        "<strong>Metnin Konusu:</strong><br>Arıların doğadaki önemi, bitkilerin tozlaşması ve çoğalmasındaki rolü ile yaşam dengesinin korunmasına katkısıdır.",
        "Metnin konusunu yazınız...")

    q3 = build_q_strip(3, "Demirci Hasan ve Kasaba Halkının Kararı", 10, "turkce7_q3.mp3", "turkce7_sol3.mp3",
        "Soru 3. Demirci Hasan'ın ocağını hararetli yakması ve köylülerin ellerinde kılıçlar bulunması kasaba halkının nasıl bir karar aldığını gösterir?",
        "Soru 3 çözümü. Ocağın hararetli yanması vatan savunması ateşini, tarım aletleri yerine kılıç tutulması halkın teslim olmayıp ellerindeki her imkanı silaha dönüştürerek vatanı savunma kararı aldığını gösterir.",
        "<strong>Kasaba Halkının Kararı:</strong><br>Ocağın hararetle yanması hazırlığın büyüklüğünü ve halkın içindeki vatan savunması ateşini simgeler. Tarım aletlerinin yerini kılıçların alması ise halkın teslim olmayıp <strong>vatanlarını canla başla savunma ve mücadele etme kararı</strong> aldığını gösterir.",
        "Kasaba halkının aldığı kararı açıklayınız...")

    q4 = build_q_strip(4, "Şerife Bacı Metnini Tamamlama", 10, "turkce7_q4.mp3", "turkce7_sol4.mp3",
        "Soru 4. Metni Şerife Bacı'nın kararlılığını yansıtacak şekilde fedakarlık, sarsılmaz irade, hürriyet ve vatan sağ olsun ifadeleriyle tamamlayınız.",
        "Soru 4 çözümü. Örnek tamamlama: Çünkü o biliyordu ki bu mermiler ulaşmazsa hürriyet ateşi sönecektir. Sarsılmaz iradesi ve fedakarlığıyla vatan sağ olsun diyerek bir dağ gibi dimdik yoluna devam etti.",
        "<strong>Örnek Tamamlama Metni:</strong><br><em>'...Çünkü o biliyordu ki bu mermiler ulaşmazsa <strong>hürriyet</strong> ateşi sönecek, vatanın istikbali karanlığa gömülecekti. Bebeğinden vazgeçmişti ama <strong>sarsılmaz iradesiyle</strong> vatanından vazgeçmiyordu. Onun bu sessiz <strong>fedakârlığı</strong> destana dönüştü. Tek bir düşüncesi vardı: “<strong>Vatan sağ olsun!</strong>” Bu inançla bir dağ gibi dimdik yoluna devam etti.'</em>",
        "Metni uygun ifadelerle tamamlayınız...")

    q5 = build_q_strip(5, "Ece'nin Tutumu ve Mehmet'in Değişimi", 10, "turkce7_q5.mp3", "turkce7_sol5.mp3",
        "Soru 5. Mehmet'in öz güven kazanmasında Ece'nin sergilediği tutumun rolü nedir? İki ipucuyla açıklayınız.",
        "Soru 5 çözümü. Ece ona acıyarak yardım etmek yerine görevi paylaşmış, takıldığında araya girmeyip sabırla beklemiş ve kitabı aralarına bırakarak eşitlik hissettirmiştir.",
        "<strong>Ece'nin Tutumu ve İpuçları:</strong><br>Ece ona acımak yerine <em>'Bunu birlikte okuyabiliriz'</em> diyerek görevi eşit paylaştırmış, Mehmet duraksadığında sözünü kesmeyip sabırla beklemiş ve kitabı aralarına bırakarak güven vermiştir. Bu baskısız empati sayesinde Mehmet gruba ait hissetmiş ve inisiyatif alarak kendi kitabını seçmiştir.",
        "Metinden iki ipucuyla Mehmet'in değişimini açıklayınız...")

    q6 = build_q_strip(6, "Forsa Hikayesinden Kelime Tahmini", 10, "turkce7_q6.mp3", "turkce7_sol6.mp3",
        "Soru 6. Forsa hikayesinden alınan bitap, iştiyak ve teselli kelimelerinin anlamlarını gerekçeleriyle yazınız.",
        "Soru 6 çözümü. a bitap: Yorgun, güçsüz. Gerekçe: kolları eski kuvvetini kaybetmiş, kemik torbasına dönmüştü. b iştiyak: Özlem, şiddetli arzu. Gerekçe: yanıp tutuşurdu, hasretle atarken. c teselli: Avuntu, moral. Gerekçe: acısını bir an olsun unuttururdu.",
        "• <strong>a. Bitap:</strong> Yorgun, dermansız, bitkin. <em>Gerekçe:</em> 'Kolları eski kuvvetini kaybetmiş, heybetli vücudu erimiş, kemik torbasına dönmüştü.'<br>• <strong>b. İştiyak:</strong> Şiddetli arzu, hasret, özlem. <em>Gerekçe:</em> 'Türk yelkenlisi görmenin iştiyakıyla yanıp tutuşurdu, kalbi hasretle atarken.'<br>• <strong>c. Teselli:</strong> Avuntu, acıyı hafifletme. <em>Gerekçe:</em> 'Dalga sesleri ona ufak bir teselli verir, acısını bir an olsun unuttururdu.'",
        "a. bitap: ... \nb. iştiyak: ... \nc. teselli: ...")

    q7 = build_q_strip(7, "Metin Yapısı ve Yazarın Vurgusu", 10, "turkce7_q7.mp3", "turkce7_sol7.mp3",
        "Soru 7. Vatan toprağına sadakat metninde kullanılan metin yapısını ve yazarın vurgulamak istediği ana bilgiyi yazınız.",
        "Soru 7 çözümü. Metin yapısı karşılaştırma ve zıtlıktır. Yazar milli birlik ve dayanışma olmadan sadece askeri gücün yeterli olmadığını, kenetlenen milletlerin bağımsızlığını koruduğunu vurgulamıştır.",
        "• <strong>Metin Yapısı:</strong> <strong>Karşılaştırma / Zıtlık</strong> (Dayanışmayı kaybedip yok olan medeniyetler ile kenetlenip bağımsız kalan milletler karşılaştırılmıştır).<br>• <strong>Vurgulanan Temel Bilgi:</strong> Vatanın korunması ve bekası sadece askeri güç ve sınırlarla değil, bireylerin milli bir bilinçle birbirine kenetlenmesi ve dayanışmasıyla mümkündür.",
        "Metin yapısı: ... \nVurgulanan bilgi: ...")

    q8 = build_q_strip(8, "Küresel Isınma Metni Anahtar Kelimeleri", 10, "turkce7_q8.mp3", "turkce7_sol8.mp3",
        "Soru 8. Küresel ısınma metninin içeriğini yansıtan üç anahtar kelime belirleyip sebep-sonuç ilişkisini açıklayınız.",
        "Soru 8 çözümü. Anahtar kelimeler: Küresel ısınma, buzul erimesi, deniz seviyesi. Sebep sonuç: Küresel ısınma buzulların erimesine, buzulların erimesi deniz seviyelerinin yükselmesine yol açar.",
        "• <strong>Üç Anahtar Kelime:</strong> <strong>Küresel Isınma, Buzul Erimesi, Deniz Seviyesi</strong> (veya <em>Sera Gazları, Ekosistem</em>).<br>• <strong>Sebep-Sonuç İlişkisi:</strong> Atmosferdeki sera gazları küresel ısınmaya (sebep), küresel ısınma kutuplardaki buzulların erimesine (sonuç), eriyen buzullar ise deniz seviyesinin yükselerek kıyı ekosistemlerinin zarar görmesine yol açar.",
        "Anahtar kelimeler ve sebep-sonuç ilişkisi...")

    q9 = build_q_strip(9, "Yazım Yanlışı ve Noktalama İşaretleri", 10, "turkce7_q9.mp3", "turkce7_sol9.mp3",
        "Soru 9. İkilemelerin doğru yazımı ve noktalı virgül ile üç noktanın kullanım amaçları.",
        "Soru 9 çözümü. a şıkkı: Doğru cümle apar topar toplayıp hızlı hızlı sınıftan çıktı. İkilemeler ayrı yazılır, araya kısa çizgi konmaz. b şıkkı: 1 noktalı virgül özneyi ayırmak için, 2 üç nokta eksiltili cümle için, 3 noktalı virgül sıralı cümleleri ayırmak için.",
        "<strong>a. Doğru Cümle:</strong><br><em>“Sınav kâğıtlarını <strong>apar topar</strong> toplayıp <strong>hızlı hızlı</strong> sınıftan çıktı ancak dışarıda yağmur yağıyordu.”</em> (İkilemeler daima ayrı yazılır, aralarına kısa çizgi konmaz).<br><br><strong>b. Noktalama İşaretleri ve Amaçları:</strong><br>1. <strong>Noktalı Virgül (;)</strong> → İkiden fazla eş değer ögeler arasında virgül bulunan cümlede özneyi diğer ögelerden ayırmak için.<br>2. <strong>Üç Nokta (...)</strong> → Anlatımı tamamlanmamış (eksiltili) cümlenin sonuna konur.<br>3. <strong>Noktalı Virgül (;)</strong> → Ögeleri arasında virgül bulunan sıralı cümleleri birbirinden ayırmak için.",
        "a. Doğru cümle: ... \nb. Noktalama işaretleri amaçları: ...")

    q10 = build_q_strip(10, "Doğa Sevgisi Temalı Bilgilendirici Metin Taslağı", 10, "turkce7_q10.mp3", "turkce7_sol10.mp3",
        "Soru 10. Doğa sevgisi temalı bilgilendirici metin için giriş gelişme sonuç taslağı hazırlayınız ve metin yazınız.",
        "Soru 10 çözümü. Giriş: Doğanın tanımı ve insan için önemi. Gelişme: Doğayı koruma sorumlulukları, çevre kirliliği ve ağaçlandırma. Sonuç: Doğayı korumanın kendi geleceğimizi korumak olduğu vurgulanır.",
        "<strong>Metin Taslağı:</strong><br>• <strong>Giriş:</strong> Doğanın insanın varlığını borçlu olduğu en büyük yuva olduğu ve yaşamsal önemi açıklanır.<br>• <strong>Gelişme:</strong> Çevre kirliliği, orman tahribatı gibi tehlikeler ve bireysel sorumluluklar (geri dönüşüm, su tasarrufu, fidan dikimi) örneklenir.<br>• <strong>Sonuç:</strong> Doğayı korumanın aslında insanın kendi geleceğini korumak olduğu vurgulanarak farkındalık oluşturulur.<br><br><strong>Örnek Başlık:</strong> <em>DOĞA: BİZİM ORTAK EVİMİZ</em>",
        "Giriş, gelişme ve sonuç taslağınızı yazınız...")

    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>7. Sınıf Türkçe 1. Dönem 1. Yazılı - MEBİ Soruları ve Çözümleri</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body class="theme-turkce">
  {get_header('turkce7')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>📚</span> 7. Sınıf Türkçe 1. Dönem 1. Yazılı (MEBİ)</h1>
        <p>10 Sorunun Tamamı İnteraktif Çözümlü • Orijinal MEBİ PDF Sayfaları • PC ve Mobil Ses Motoru</p>
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
          <strong style="display:block; font-size:0.95rem;">Türkçe MEBİ Sesli Rehber</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır — Dinlemek için ses butonlarına tıklayın</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.speakText('7. Sınıf Türkçe 1. Dönem 1. Yazılı MEBİ Konu Özeti. Metinde anlam, Hürkuş ve Forsa metinleri, sözcükte anlam tahmini, Şerife Bacı Milli Mücadele metni tamamlama, sebep sonuç ilişkisi, ikilemelerin yazımı ve noktalama işaretleri sınavın ana konularıdır.')">📢 Sınav Konu Özetini Dinle</button>
      </div>
    </div>

    <!-- Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="pdf-pane">📄 Orijinal MEBİ PDF'i Üzerinde Soruları Çöz</button>
      <button class="tab-btn" data-tab="answer-key-pane">🔑 Resmi Çözümler (Sayfa 6-9)</button>
    </div>

    <!-- TAB 1: WORKBENCH -->
    <div id="pdf-pane" class="tab-pane active">
      <div class="interactive-pdf-container">
        
        <!-- Sayfa 1 -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 MEBİ Soru Kitapçığı - Sayfa 1 (Soru 1, Soru 2, Soru 3)</span>
            <span style="font-size:0.85rem; opacity:0.85;">1. Dönem 1. Yazılı</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/pdf_pages/turkce_mebi/page_1.png" alt="Türkçe Sayfa 1" loading="eager">
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
            <span>📄 MEBİ Soru Kitapçığı - Sayfa 2 (Soru 4, Soru 5)</span>
            <span style="font-size:0.85rem; opacity:0.85;">1. Dönem 1. Yazılı</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/pdf_pages/turkce_mebi/page_2.png" alt="Türkçe Sayfa 2" loading="lazy">
          </div>
          <div class="pdf-question-controls">
            {q4}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q5}
          </div>
        </div>

        <!-- Sayfa 3 -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 MEBİ Soru Kitapçığı - Sayfa 3 (Soru 6, Soru 7)</span>
            <span style="font-size:0.85rem; opacity:0.85;">1. Dönem 1. Yazılı</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/pdf_pages/turkce_mebi/page_3.png" alt="Türkçe Sayfa 3" loading="lazy">
          </div>
          <div class="pdf-question-controls">
            {q6}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q7}
          </div>
        </div>

        <!-- Sayfa 4 & 5 -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 MEBİ Soru Kitapçığı - Sayfa 4 & 5 (Soru 8, Soru 9, Soru 10)</span>
            <span style="font-size:0.85rem; opacity:0.85;">1. Dönem 1. Yazılı</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/pdf_pages/turkce_mebi/page_4.png" alt="Türkçe Sayfa 4" loading="lazy">
          </div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;">
            <img src="assets/pdf_pages/turkce_mebi/page_5.png" alt="Türkçe Sayfa 5" loading="lazy">
          </div>
          <div class="pdf-question-controls">
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
          🏆 7. Sınıf Türkçe Notumu Hesapla
        </button>
      </div>
    </div>

    <!-- TAB 2: OFFICIAL SOLUTIONS -->
    <div id="answer-key-pane" class="tab-pane">
      <div class="pdf-interactive-page">
        <div class="page-banner" style="background:#047857;">
          <span>📄 MEBİ Resmi Öğretmen Çözüm Anahtarı (Sayfa 6, 7, 8, 9)</span>
          <span style="font-size:0.85rem; opacity:0.85;">Temel Eğitim Genel Müdürlüğü</span>
        </div>
        <div class="pdf-image-wrap"><img src="assets/pdf_pages/turkce_mebi/page_6.png" alt="Çözüm 6" loading="lazy"></div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/turkce_mebi/page_7.png" alt="Çözüm 7" loading="lazy"></div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/turkce_mebi/page_8.png" alt="Çözüm 8" loading="lazy"></div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/turkce_mebi/page_9.png" alt="Çözüm 9" loading="lazy"></div>
      </div>
    </div>

  </main>

  {get_score_modal()}
  {get_footer()}

  <script src="assets/js/app.js"></script>
  <script>
    initLesson('turkce_7', 'tr-TR');
  </script>
</body>
</html>
"""

# =========================================================================
# 2. 7. SINIF SOSYAL BİLGİLER (5 Soru - 100 Puan)
# =========================================================================
def generate_7_sosyal():
    q1 = build_q_strip(1, "Empati Kurma Konuşma Metni", 20, "sosyal7_q1.mp3", "sosyal7_sol1.mp3",
        "Soru 1. Selim'in yüksek sesten rahatsız olan arkadaşı Ezel ile empati kurduğunu gösteren bir konuşma metni yazınız.",
        "Soru 1 çözümü. Selim'in Ezel'in duygularını ve hassasiyetini anladığını gösteren ifadeler: Ben de rahatsız olduğum bir ortamda eğlenemezdim. İstersen sinema yerine açık havada dolaşmaya çıkabiliriz.",
        "<strong>Örnek Empati Konuşması:</strong><br><em>'Seni çok iyi anlıyorum Ezel. Yüksek sesin seni rahatsız etmesi çok doğal. Kendini kötü hissettiğin bir ortamda bulunmanı istemem. İstersen sinemaya gitmek yerine sakin bir kafede oturabilir ya da parkta yürüyüş yapabiliriz.'</em>",
        "Selim'in empati kuran konuşmasını yazınız...")

    q2 = build_q_strip(2, "Sen Dilini Ben Diline Çevirme", 20, "sosyal7_q2.mp3", "sosyal7_sol2.mp3",
        "Soru 2. Sürekli geç kalmandan bıktım ve salonu dağınık bırakıyorsun cümlelerini ben diline çeviriniz.",
        "Soru 2 çözümü. 1: Geç kaldığında kendimi önemsiz veya değersiz hissediyorum ve endişeleniyorum. 2: Salon dağınık kaldığında aradığımı bulamıyorum ve bu beni rahatsız ediyor.",
        "• <strong>1. Cümle:</strong> <em>'Sürekli geç kalmandan bıktım!'</em><br>→ <strong>Ben Dili:</strong> <strong>'Buluşmalarımıza geç kaldığında vaktimi değerlendiremediğimi düşünüyor ve kendimi değersiz hissediyorum.'</strong><br><br>• <strong>2. Cümle:</strong> <em>'Salonu dağınık bırakıyorsun.'</em><br>→ <strong>Ben Dili:</strong> <strong>'Salon dağınık kaldığında aradığım eşyaları bulmakta zorlanıyor ve dinlenemediğim için huzursuz oluyorum.'</strong>",
        "1. Ben dili: ... \n2. Ben dili: ...")

    q3 = build_q_strip(3, "Özel Gereksinimli Bireyler İçin Slogan", 20, "sosyal7_q3.mp3", "sosyal7_sol3.mp3",
        "Soru 3. Oyun parklarının özel gereksinimli çocukların ihtiyaçlarına uygun düzenlenmesi için bir slogan yazınız.",
        "Soru 3 çözümü. Örnek sloganlar: Engelleri oyunla aşalım. Her çocuk için engelsiz parklar. Parkta engel yok, oyunda birlik çok.",
        "<strong>Örnek Sloganlar:</strong><br>• <em>“Engelleri oyunla aşalım, parklarda buluşalım!”</em><br>• <em>“Her çocuğun hakkı oyun, engelsiz parklar kurun!”</em><br>• <em>“Parkta engel yok, hepimize yer çok!”</em>",
        "Sloganınızı yazınız...")

    q4 = build_q_strip(4, "Mustafa Kemal Paşa ve Anadolu Halkı", 20, "sosyal7_q4.mp3", "sosyal7_sol4.mp3",
        "Soru 4. Mustafa Kemal Paşa'nın Samsun'a çıkmasında hangi gelişmeler etkili oldu ve Anadolu halkının yaklaşımı nasıl oldu?",
        "Soru 4 çözümü. a şıkkı: Osmanlı devletinin 1. dünya savaşında yenilmesi, Mondros ateşkes antlaşması ve Anadolunun işgale uğraması. b şıkkı: Anadolu halkı tüm imkansızlıklara rağmen yurdunu savunmak için seferber olmuş ve ordusuyla kenetlenmiştir.",
        "<strong>a) Etkili Olan Tarihsel Gelişmeler:</strong><br>Osmanlı Devleti’nin I. Dünya Savaşı’ndan yenik çıkması, Mondros Ateşkes Antlaşması’nın ağır şartları ve yurdun İtilaf Devletleri tarafından işgal edilmeye başlanması.<br><br><strong>b) Anadolu Halkının Yaklaşımı:</strong><br>Anadolu halkı tüm yokluk ve imkânsızlıklara rağmen vatanını savunmak için seferber olmuş; Kuvâ-yı Millîye birliklerini kurup elindeki tüm imkânları ordusuyla paylaşmıştır.",
        "a) Gelişmeler: ... \nb) Halkın yaklaşımı: ...")

    q5 = build_q_strip(5, "Küreselleşme ve İletişimdeki Değişim", 20, "sosyal7_q5.mp3", "sosyal7_sol5.mp3",
        "Soru 5. Küreselleşmenin iletişim alanında yol açtığı değişime günlük yaşamdan bir örnek veriniz.",
        "Soru 5 çözümü. Eskiden mektuplar günlerce haftalarca sonra ulaşırken, günümüzde genel ağ ve akıllı telefonlar sayesinde dünyanın öbür ucundaki biriyle anında görüntülü görüşülebilmektedir.",
        "<strong>Günlük Yaşamdan Örnek:</strong><br>Eskiden uzaktaki bir akraba veya arkadaşla haberleşmek için yazılan mektupların ulaşması günler hatta haftalar sürerken, günümüzde internet, akıllı telefonlar ve görüntülü arama uygulamaları sayesinde dünyanın diğer ucundaki insanlarla saniyeler içinde yüz yüze iletişim kurulabilmektedir.",
        "Günlük yaşamdan örneğinizi yazınız...")

    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>7. Sınıf Sosyal Bilgiler 1. Dönem 1. Yazılı - MEBİ Soruları ve Çözümleri</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body class="theme-sosyal">
  {get_header('sosyal7')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>🌍</span> 7. Sınıf Sosyal Bilgiler 1. Dönem 1. Yazılı (MEBİ)</h1>
        <p>Empati ve İletişim • Ben Dili • Milli Mücadele • Küreselleşme • 5 Sorunun Tamamı Çözümlü</p>
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
          <strong style="display:block; font-size:0.95rem;">Sosyal Bilgiler MEBİ Sesli Rehber</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır — Dinlemek için ses butonlarına tıklayın</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.speakText('7. Sınıf Sosyal Bilgiler 1. Dönem 1. Yazılı MEBİ Özeti. Etkili iletişim, sen dili yerine ben dili kullanımı, empati kurma becerisi, özel gereksinimli bireylerin hakları, Mustafa Kemal Paşanın Samsuna çıkışı ve Milli Mücadele ruhu ile küreselleşmenin iletişime etkileri sınavın temel konularıdır.')">📢 Sınav Konu Özetini Dinle</button>
      </div>
    </div>

    <!-- Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="pdf-pane">📄 Orijinal MEBİ PDF'i Üzerinde Soruları Çöz</button>
      <button class="tab-btn" data-tab="answer-key-pane">🔑 Resmi Çözümler (Sayfa 3 & 4)</button>
    </div>

    <!-- TAB 1: WORKBENCH -->
    <div id="pdf-pane" class="tab-pane active">
      <div class="interactive-pdf-container">
        
        <!-- Sayfa 1 -->
        <div class="pdf-interactive-page">
          <div class="page-banner">
            <span>📄 MEBİ Soru Kitapçığı - Sayfa 1 (Soru 1, Soru 2, Soru 3)</span>
            <span style="font-size:0.85rem; opacity:0.85;">1. Dönem 1. Yazılı</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/pdf_pages/sosyal_mebi/page_1.png" alt="Sosyal Sayfa 1" loading="eager">
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
            <span>📄 MEBİ Soru Kitapçığı - Sayfa 2 (Soru 4, Soru 5)</span>
            <span style="font-size:0.85rem; opacity:0.85;">1. Dönem 1. Yazılı</span>
          </div>
          <div class="pdf-image-wrap">
            <img src="assets/pdf_pages/sosyal_mebi/page_2.png" alt="Sosyal Sayfa 2" loading="lazy">
          </div>
          <div class="pdf-question-controls">
            {q4}
            <hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">
            {q5}
          </div>
        </div>

      </div>

      <div style="text-align: center; margin: 36px 0;">
        <button class="btn-start" style="padding: 18px 42px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 7. Sınıf Sosyal Bilgiler Notumu Hesapla
        </button>
      </div>
    </div>

    <!-- TAB 2: OFFICIAL SOLUTIONS -->
    <div id="answer-key-pane" class="tab-pane">
      <div class="pdf-interactive-page">
        <div class="page-banner" style="background:#047857;">
          <span>📄 MEBİ Resmi Öğretmen Çözüm Anahtarı (Sayfa 3 & 4)</span>
          <span style="font-size:0.85rem; opacity:0.85;">Temel Eğitim Genel Müdürlüğü</span>
        </div>
        <div class="pdf-image-wrap"><img src="assets/pdf_pages/sosyal_mebi/page_3.png" alt="Çözüm 3" loading="lazy"></div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/sosyal_mebi/page_4.png" alt="Çözüm 4" loading="lazy"></div>
      </div>
    </div>

  </main>

  {get_score_modal()}
  {get_footer()}

  <script src="assets/js/app.js"></script>
  <script>
    initLesson('sosyal_7', 'tr-TR');
  </script>
</body>
</html>
"""

# Let's write turkce and sosyal
out_dir = r"d:\gpt\5_sinif_calisma_portali"
with open(os.path.join(out_dir, "7-turkce.html"), "w", encoding="utf-8") as f:
    f.write(generate_7_turkce())
with open(os.path.join(out_dir, "7-sosyal-bilgiler.html"), "w", encoding="utf-8") as f:
    f.write(generate_7_sosyal())
print("7-turkce.html and 7-sosyal-bilgiler.html created!")
