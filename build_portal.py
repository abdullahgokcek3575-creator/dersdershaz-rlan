# -*- coding: utf-8 -*-
"""
5. Sınıf 1. Dönem 1. Yazılıya Hazırlık Etkileşimli Portalı Oluşturucu
Tüm dersler için sesli anlatımlı, görüntülü, etkileşimli çözümlü web sayfalarını üretir.
"""

import os, sys, json

OUTPUT_DIR = r"d:\gpt\5_sinif_calisma_portali"
DOWNLOADS_DIR = r"C:\Users\User\Downloads\2026-2027\5\Etkilesimli_Calisma_Portali"

def get_header(current_page="home"):
    links = [
        ("index.html", "🏠 Ana Sayfa", "home"),
        ("fen-bilimleri.html", "🔬 Fen Bilimleri", "fen"),
        ("matematik.html", "📐 Matematik", "mat"),
        ("turkce.html", "📚 Türkçe", "turkce"),
        ("sosyal-bilgiler.html", "🌍 Sosyal Bilgiler", "sosyal"),
        ("din-kulturu.html", "🕌 Din Kültürü", "din"),
        ("ingilizce.html", "🇬🇧 İngilizce", "ingilizce"),
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
        <p><strong>5. Sınıf 1. Dönem 1. Yazılı Akıllı Hazırlık Portalı</strong></p>
        <p>MEB Yeni Müfredatı (Türkiye Yüzyılı Maarif Modeli) Uyumlu Etkileşimli Çalışma Materyali</p>
        <p style="margin-top: 8px; font-size: 0.82rem; color: #94a3b8;">Sesli Dinleme • Görsel Çözümler • Puanlama ve Deneme Simülatörü</p>
      </div>
    </footer>
    """

def get_score_modal():
    return """
    <div id="scoreModal" class="modal-overlay">
      <div class="modal-content">
        <h2>🎉 Sınav Tamamlandı!</h2>
        <div class="modal-score" id="finalScoreVal">100</div>
        <p style="font-weight: 700; color: #64748b; margin-bottom: 12px;">Toplam Puan / 100</p>
        <p id="scoreFeedback" style="font-size: 1.05rem; line-height: 1.5; color: #334155;">Harika bir çalışma gerçekleştirdin!</p>
        <button class="btn-modal" onclick="portalApp.closeModal()">Kapat ve İncelemeye Devam Et</button>
      </div>
    </div>
    """

# -------------------------------------------------------------
# 1. INDEX / DASHBOARD
# -------------------------------------------------------------
def build_index():
    html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>5. Sınıf 1. Dönem 1. Yazılı Etkileşimli Hazırlık Portalı</title>
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  {get_header('home')}

  <main class="container">
    <section class="hero">
      <div style="display: inline-block; background: rgba(255,255,255,0.2); padding: 4px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 700; margin-bottom: 12px;">
        🎯 2026-2027 EĞİTİM DÖNEMİ 1. YAZILILAR
      </div>
      <h1>5. Sınıf 1. Dönem 1. Yazılı Akıllı Çalışma Portalı</h1>
      <p>Yazılı sınavlarına en yüksek verimle hazırlan! Sesli konu anlatımı, etkileşimli soru çözümleri, ipuçları ve detaylı çözümlerle tüm dersler parmaklarının ucunda.</p>
      
      <div class="hero-stats">
        <div class="stat-pill">📚 6 Temel Ders</div>
        <div class="stat-pill">🔊 Akıllı Sesli Anlatım</div>
        <div class="stat-pill">🖼️ Görsel ve Şematik Çözümler</div>
        <div class="stat-pill">⭐ Kendini Puanla Simülatörü</div>
      </div>
    </section>

    <h2 style="font-size: 1.5rem; margin-bottom: 20px; color: #1e293b; display: flex; align-items: center; gap: 8px;">
      <span>📖</span> Ders Seçimi Yaparak Çalışmaya Başla
    </h2>

    <div class="subject-grid">
      
      <!-- FEN BİLİMLERİ -->
      <div class="subject-card theme-fen">
        <div class="card-top">
          <div class="card-icon">🔬</div>
          <span class="card-badge">8 Soru • 100 Puan</span>
        </div>
        <h3>Fen Bilimleri</h3>
        <p>Güneş ve Ay'ın yapısı, Dünya ve Ay'ın hareketleri, Ay'ın evreleri, Kuvvetin ölçülmesi ve dinamometreler.</p>
        <div class="topic-tags">
          <span class="tag">Güneş'in Özellikleri</span>
          <span class="tag">Ay'ın Evreleri</span>
          <span class="tag">Dinamometre</span>
          <span class="tag">Dönme & Dolanma</span>
        </div>
        <a href="fen-bilimleri.html" class="btn-start">Çalışmaya Başla ➔</a>
      </div>

      <!-- MATEMATİK -->
      <div class="subject-card theme-mat">
        <div class="card-top">
          <div class="card-icon">📐</div>
          <span class="card-badge">10 Soru • 100 Puan</span>
        </div>
        <h3>Matematik</h3>
        <p>Geometrik çizim araçları, doğru, ışın, doğru parçası, açılar, tümler-bütünler açılar ve pergel ile çember çizimi.</p>
        <div class="topic-tags">
          <span class="tag">Çizim Araçları</span>
          <span class="tag">Açılar & İletki</span>
          <span class="tag">Çember & Çap</span>
          <span class="tag">Tümler & Bütünler</span>
        </div>
        <a href="matematik.html" class="btn-start">Çalışmaya Başla ➔</a>
      </div>

      <!-- TÜRKÇE -->
      <div class="subject-card theme-turkce">
        <div class="card-top">
          <div class="card-icon">📚</div>
          <span class="card-badge">6 Soru • 100 Puan</span>
        </div>
        <h3>Türkçe</h3>
        <p>Metin anlama, sözcükte anlam, kişileştirme (teşhis) sanatı, yazım kuralları (tarihler, yer adları, cadde/sokak).</p>
        <div class="topic-tags">
          <span class="tag">Metinde Anlam</span>
          <span class="tag">Kişileştirme</span>
          <span class="tag">Yazım Kuralları</span>
          <span class="tag">Söz Varlığı</span>
        </div>
        <a href="turkce.html" class="btn-start">Çalışmaya Başla ➔</a>
      </div>

      <!-- SOSYAL BİLGİLER -->
      <div class="subject-card theme-sosyal">
        <div class="card-top">
          <div class="card-icon">🌍</div>
          <span class="card-badge">6 Soru • 100 Puan</span>
        </div>
        <h3>Sosyal Bilgiler</h3>
        <p>Birey ve toplum, gruplardaki rollerimiz, hak ve sorumluluklarımız, Sadaka Taşı kültürü ve Millî Mücadele dayanışması.</p>
        <div class="topic-tags">
          <span class="tag">Roller & Haklar</span>
          <span class="tag">Sadaka Taşı</span>
          <span class="tag">Toplumsal Birlik</span>
          <span class="tag">Millî Mücadele</span>
        </div>
        <a href="sosyal-bilgiler.html" class="btn-start">Çalışmaya Başla ➔</a>
      </div>

      <!-- DİN KÜLTÜRÜ -->
      <div class="subject-card theme-din">
        <div class="card-top">
          <div class="card-icon">🕌</div>
          <span class="card-badge">5 Bölüm • 100 Puan</span>
        </div>
        <h3>Din Kültürü ve Ahlak Bilgisi</h3>
        <p>Evrendeki mükemmel düzen, Esmâ-i Hüsnâ (Alîm, Semî, Basîr, Kadîr), Tevhit inancı ve İhlas Suresi ve meali.</p>
        <div class="topic-tags">
          <span class="tag">Evrendeki Düzen</span>
          <span class="tag">Esmâ-i Hüsnâ</span>
          <span class="tag">Tevhit İnancı</span>
          <span class="tag">İhlas Suresi</span>
        </div>
        <a href="din-kulturu.html" class="btn-start">Çalışmaya Başla ➔</a>
      </div>

      <!-- İNGİLİZCE -->
      <div class="subject-card theme-ingilizce">
        <div class="card-top">
          <div class="card-icon">🇬🇧</div>
          <span class="card-badge">5 Bölüm • 100 Puan</span>
        </div>
        <h3>İngilizce</h3>
        <p>School & Classroom Life, Fred's timetable, telling the time, Mia's daily routine, must & mustn't okul kuralları.</p>
        <div class="topic-tags">
          <span class="tag">School Subjects</span>
          <span class="tag">Telling Time</span>
          <span class="tag">Daily Routines</span>
          <span class="tag">Must / Mustn't</span>
        </div>
        <a href="ingilizce.html" class="btn-start">Çalışmaya Başla ➔</a>
      </div>

    </div>

    <!-- Nasıl Çalışılmalı Rehberi -->
    <section style="background: white; border-radius: 16px; padding: 28px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); margin-top: 10px;">
      <h3 style="margin-bottom: 16px; font-size: 1.3rem; color: #1e293b;">💡 Portaldan En Yüksek Verimi Nasıl Alırsın?</h3>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px;">
        <div style="background: #f8fafc; padding: 16px; border-radius: 12px; border-left: 4px solid #4f46e5;">
          <h4 style="font-size: 1rem; margin-bottom: 6px; color: #1e293b;">1. Hap Bilgileri Sesli Dinle</h4>
          <p style="font-size: 0.9rem; color: #64748b;">Her dersin girişinde sınavda kesin çıkacak özet bilgiler yer alır. Sesli dinleme butonuna basarak kulaklıkla tekrar yapabilirsin.</p>
        </div>
        <div style="background: #f8fafc; padding: 16px; border-radius: 12px; border-left: 4px solid #10b981;">
          <h4 style="font-size: 1rem; margin-bottom: 6px; color: #1e293b;">2. Soruları Kendi Başına Çöz</h4>
          <p style="font-size: 0.9rem; color: #64748b;">Doğrudan cevaba bakmak yerine önce kutucuğa kendi cevabını yaz. Zorlanırsan "İpucu" butonundan tüyo al.</p>
        </div>
        <div style="background: #f8fafc; padding: 16px; border-radius: 12px; border-left: 4px solid #f59e0b;">
          <h4 style="font-size: 1rem; margin-bottom: 6px; color: #1e293b;">3. Model Çözümü İncele & Puanla</h4>
          <p style="font-size: 0.9rem; color: #64748b;">"Resmi Çözümü Gör"e tıklayarak öğretmenlerin tam puan verdiği anahtar kelimeleri gör ve kendini puanlayarak notunu hesapla.</p>
        </div>
      </div>
    </section>
  </main>

  {get_footer()}
</body>
</html>"""
    return html

# Write out index.html
with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(build_index())
print("index.html created.")

# -------------------------------------------------------------
# 2. FEN BİLİMLERİ SAYFASI
# -------------------------------------------------------------
def build_fen():
    html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>5. Sınıf Fen Bilimleri 1. Dönem 1. Yazılı Hazırlık</title>
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body class="theme-fen">
  {get_header('fen')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>🔬</span> Fen Bilimleri 1. Dönem 1. Yazılı</h1>
        <p>Güneş, Dünya ve Ay'ın Hareketleri • Ay'ın Evreleri • Kuvvet ve Dinamometre</p>
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
          <strong style="display:block; font-size:0.95rem;">Sesli Asistan & Dinleme Rehberi</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır (Dinlemek için aşağıdaki ses butonlarına tıklayın)</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.playAudio('fen_summary.mp3')">📢 Tüm Konu Özetini Dinle</button>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="summary-pane">💡 Sınavda Çıkacak Hap Bilgiler</button>
      <button class="tab-btn" data-tab="questions-pane">📝 İnteraktif Yazılı Soruları (Çözümlü)</button>
      <button class="tab-btn" data-tab="pdf-pane">📄 Orijinal Sınav Kağıdı & Çözüm Anahtarı</button>
    </div>

    <!-- TAB 1: SUMMARY -->
    <div id="summary-pane" class="tab-pane active">
      <div id="fenSummaryArea" class="summary-cards">
        <div class="summary-card">
          <h4>☀️ 1. Güneş'in Özellikleri</h4>
          <ul>
            <li><strong>Şekli:</strong> Küreseldir.</li>
            <li><strong>Yapısı:</strong> Sıcak gazlardan (yaklaşık %73 Hidrojen, %25 Helyum) oluşur.</li>
            <li><strong>Enerji:</strong> Dünya'mızın temel ısı ve ışık kaynağıdır.</li>
            <li><strong>Yıldız Türü:</strong> Dünya'ya en yakın orta büyüklükte bir yıldızdır.</li>
            <li><strong>Hareketi:</strong> Kendi ekseni etrafında <em>saat yönünün tersine (batıdan doğuya)</em> döner. Bir tam dönüşü yaklaşık 25 gün sürer.</li>
          </ul>
        </div>

        <div class="summary-card">
          <h4>🌑 2. Ay'ın Yapısı ve Atmosferi</h4>
          <ul>
            <li><strong>Şekli:</strong> Küreseldir, Dünya'nın tek doğal uydusudur.</li>
            <li><strong>Atmosferi:</strong> Yok denecek kadar incedir.</li>
            <li><strong>Atmosfer Yokluğunun Sonuçları:</strong> Yağmur, rüzgâr gibi hava olayları görülmez; gece ile gündüz sıcaklık farkı aşırı fazladır; ses yayılmaz (uzay boşluğu).</li>
            <li><strong>Ay'a giderken:</strong> Oksijen tüpü, uzay giysisi, su ve besin götürülmesi zorunludur.</li>
          </ul>
        </div>

        <div class="summary-card">
          <h4>🔄 3. Ay'ın Hareketleri ve Evreleri</h4>
          <ul>
            <li><strong>Dönme & Dolanma:</strong> Ay hem kendi etrafında döner hem de Dünya etrafında dolanır. İki hareket de yaklaşık <strong>27 gün 8 saat</strong> sürer.</li>
            <li><strong>Hep Aynı Yüz:</strong> Bu iki süre eşit olduğu için Dünya'dan bakıldığında Ay'ın hep aynı yüzü görülür!</li>
            <li><strong>Ana Evreler:</strong> Yeni Ay ➔ İlk Dördün ➔ Dolunay ➔ Son Dördün (Evreler arası yaklaşık 1 hafta geçer).</li>
            <li><strong>Ara Evreler:</strong> Hilal ve Şişkin Ay.</li>
          </ul>
        </div>

        <div class="summary-card">
          <h4>⚖️ 4. Kuvvet ve Dinamometre</h4>
          <ul>
            <li><strong>Kuvvet:</strong> Bir cismi hareket ettiren, durduran, yönünü veya şeklini değiştiren etkidir. Birimi <strong>Newton (N)</strong>'dur.</li>
            <li><strong>Dinamometre:</strong> İçindeki esnek yayın uzama miktarına göre kuvvet ölçer.</li>
            <li><strong>Önemli Kural:</strong> Asılan kuvvet ile yayın uzama miktarı doğru orantılıdır (Örn: 1 bölme 18 N ise, 2 bölme 36 N, 4 bölme 72 N'dur).</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- TAB 2: QUESTIONS -->
    <div id="questions-pane" class="tab-pane">
      
      <!-- Soru 1 -->
      <div class="question-card" id="q_fen_1">
        <div class="q-header">
          <span class="q-badge">Soru 1 • Güneş'in Özellikleri</span>
          <span class="q-points">15 Puan</span>
        </div>
        <div class="q-text">
          Aşağıda Dünya'mıza en yakın yıldız olan Güneş'e ait görseller incelendiğinde; Güneş'in özelliklerinden 5 tanesini maddeler halinde yazınız.
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="Cevabınızı buraya yazınız (Örn: 1. Şekli küreseldir, 2. ...)"></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('fen_q1.mp3', 'q_fen_1')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-hint" onclick="portalApp.toggleHint('q_fen_1')">💡 İpucu Al</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_fen_1')">✅ Resmi Çözümü & Model Cevabı Gör</button>
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('fen_sol1.mp3', 'q_fen_1')">🔊 Çözümü Sesli Dinle</button>
        </div>
        <div class="hint-box">
          <strong>İpucu:</strong> Şeklini, Dünya için önemini, içerdiği gazları ve kendi etrafındaki dönüş hareketini düşünün.
        </div>
        <div class="solution-box">
          <h5>✅ Öğretmen Model Cevabı (Tam Puan Kriteri):</h5>
          <div class="solution-content">
            1. Şekli küreseldir.<br>
            2. Sıcak gazlardan (Hidrojen ve Helyum) oluşur.<br>
            3. Dünya'mızın ısı ve ışık kaynağıdır.<br>
            4. Dünya'ya en yakın yıldızdır.<br>
            5. Kendi ekseni etrafında saat yönünün tersine (batıdan doğuya) döner.
          </div>
        </div>
        <div class="self-grading">
          <span>Bu sorudan kendine puan ver:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_fen_1', 15, 15, this)">15 Puan (Tam Doğru)</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_fen_1', 15, 8, this)">8 Puan (Kısmen)</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_fen_1', 15, 0, this)">0 Puan (Tekrar Et)</button>
        </div>
      </div>

      <!-- Soru 2 -->
      <div class="question-card" id="q_fen_2">
        <div class="q-header">
          <span class="q-badge">Soru 2 • Pepee ve Ay'ın Atmosferi</span>
          <span class="q-points">15 Puan</span>
        </div>
        <div class="q-text">
          Pepee'nin ninesi şu soruları soruyor:<br>
          <strong>a)</strong> Ay'da atmosfer yok denecek kadar az olduğu için Dünya'da meydana gelen olaylardan hangileri Ay'da meydana gelmez? (3 örnek veriniz)<br>
          <strong>b)</strong> Ay'da yaşayabilmek için Dünya'dan götürülmesi gereken şeylere 3 örnek veriniz.
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="a) Meydana gelmeyen olaylar:... b) Götürülmesi gerekenler:..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('fen_q2.mp3', 'q_fen_2')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-hint" onclick="portalApp.toggleHint('q_fen_2')">💡 İpucu Al</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_fen_2')">✅ Resmi Çözümü & Model Cevabı Gör</button>
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('fen_sol2.mp3', 'q_fen_2')">🔊 Çözümü Sesli Dinle</button>
        </div>
        <div class="hint-box">
          <strong>İpucu:</strong> Yağmur, rüzgar gibi olaylar havayla ilgilidir. Ay'da nefes alabilir miyiz?
        </div>
        <div class="solution-box">
          <h5>✅ Öğretmen Model Cevabı:</h5>
          <div class="solution-content">
            <strong>a) Ay'da gerçekleşmeyen olaylar:</strong><br>
            1. Yağmur, kar, rüzgâr gibi hava olayları görülmez.<br>
            2. Ses boşlukta iletilmediği için sesler duyulamaz.<br>
            3. Canlılar korunaksız olarak nefes alıp yaşayamaz (gece-gündüz sıcaklık farkı yüzlerce derecedir).<br><br>
            <strong>b) Ay'a götürülmesi gerekenler:</strong><br>
            1. Oksijen tüpü (solunum için hava),<br>
            2. Özel korumalı uzay giysisi,<br>
            3. Su ve dayanıklı besin maddeleri.
          </div>
        </div>
        <div class="self-grading">
          <span>Bu sorudan kendine puan ver:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_fen_2', 15, 15, this)">15 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_fen_2', 15, 8, this)">8 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_fen_2', 15, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- Soru 3 -->
      <div class="question-card" id="q_fen_3">
        <div class="q-header">
          <span class="q-badge">Soru 3 • Dünya ve Ay'ın Hareketleri</span>
          <span class="q-points">15 Puan</span>
        </div>
        <div class="q-text">
          Ay'ın hareketleri ile ilgili aşağıdaki soruları yanıtlayınız:<br>
          <strong>a)</strong> Ay, Dünya etrafındaki dolanma hareketini hangi yönde yapar?<br>
          <strong>b)</strong> Ay, Dünya etrafındaki dolanma hareketini ne kadar sürede tamamlar?<br>
          <strong>c)</strong> Ay kendi ekseni etrafındaki dönme hareketini ne kadar sürede tamamlar?
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="a) Yön:... b) Dolanma süresi:... c) Dönme süresi:..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('fen_q3.mp3', 'q_fen_3')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-hint" onclick="portalApp.toggleHint('q_fen_3')">💡 İpucu Al</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_fen_3')">✅ Resmi Çözümü Gör</button>
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('fen_sol3.mp3', 'q_fen_3')">🔊 Çözümü Sesli Dinle</button>
        </div>
        <div class="hint-box">
          <strong>İpucu:</strong> Ay'ın dönme ve dolanma süreleri birbirine eşittir (yaklaşık 27-28 gün). Yön ise saat yönünün tersidir.
        </div>
        <div class="solution-box">
          <h5>✅ Resmi Çözüm:</h5>
          <div class="solution-content">
            <strong>a)</strong> Saat yönünün tersine (Batıdan Doğuya).<br>
            <strong>b)</strong> Yaklaşık 27 gün 8 saat.<br>
            <strong>c)</strong> Yaklaşık 27 gün 8 saat.<br>
            <em>(Not: Dönme ve dolanma süresi eşit olduğu için Dünya'dan Ay'ın hep aynı yüzü görülür!)</em>
          </div>
        </div>
        <div class="self-grading">
          <span>Bu sorudan kendine puan ver:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_fen_3', 15, 15, this)">15 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_fen_3', 15, 8, this)">8 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_fen_3', 15, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- Soru 4 & 5 -->
      <div class="question-card" id="q_fen_4">
        <div class="q-header">
          <span class="q-badge">Soru 4 & 5 • Ay'ın Evreleri & Görünümleri</span>
          <span class="q-points">20 Puan</span>
        </div>
        <div class="q-text">
          Ay'ın Dünya etrafındaki dolanımı sırasında oluşan evrelerle ilgili:<br>
          <strong>a)</strong> Ay'ın 4 ana evresinin isimlerini sırasıyla yazınız.<br>
          <strong>b)</strong> Ay'ın ara evrelerinin isimlerini yazınız.<br>
          <strong>c)</strong> Konum 1'de (Güneş ile Dünya arasındayken) ve Konum 5'te (Dünya'nın arkasındayken) Ay'ın Dünya'dan görünümü nasıldır?
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="a) Ana evreler:... b) Ara evreler:... c) Konum 1 ve 5 görünümleri:..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('fen_q4.mp3', 'q_fen_4')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-hint" onclick="portalApp.toggleHint('q_fen_4')">💡 İpucu Al</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_fen_4')">✅ Resmi Çözümü Gör</button>
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('fen_sol4.mp3', 'q_fen_4')">🔊 Çözümü Sesli Dinle</button>
        </div>
        <div class="hint-box">
          <strong>İpucu:</strong> Konum 1'de Ay karanlıktır (Yeni Ay). Konum 5'te ise Ay tamamen aydınlık bir daire görünür (Dolunay).
        </div>
        <div class="solution-box">
          <h5>✅ Resmi Çözüm:</h5>
          <div class="solution-content">
            <strong>a) Ana Evreler:</strong> 1. Yeni Ay, 2. İlk Dördün, 3. Dolunay, 4. Son Dördün.<br>
            <strong>b) Ara Evreler:</strong> Hilal ve Şişkin Ay.<br>
            <strong>c) Görünümler:</strong><br>
            - Konum 1 (Yeni Ay): Dünya'dan hiç görünmez, karanlıktır.<br>
            - Konum 3 (İlk Dördün): Sağ tarafı aydınlık "D" harfi şeklindedir.<br>
            - Konum 5 (Dolunay): Tamamı daire şeklinde aydınlıktır.<br>
            - Konum 7 (Son Dördün): Sol tarafı aydınlık ters "D" harfi şeklindedir.
          </div>
        </div>
        <div class="self-grading">
          <span>Bu sorudan kendine puan ver:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_fen_4', 20, 20, this)">20 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_fen_4', 20, 10, this)">10 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_fen_4', 20, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- Soru 6 -->
      <div class="question-card" id="q_fen_6">
        <div class="q-header">
          <span class="q-badge">Soru 6 • Gök Cisimlerinin Hareket Süreleri</span>
          <span class="q-points">15 Puan</span>
        </div>
        <div class="q-text">
          Güneş, Dünya ve Ay'ın hareketlerinin bir tam turunu tamamlama sürelerini eşleştiriniz:<br>
          • <strong>K:</strong> Güneş'in kendi ekseni etrafında dönmesi<br>
          • <strong>L:</strong> Dünya'nın Güneş etrafında dolanması<br>
          • <strong>M:</strong> Ay'ın Dünya etrafında dolanması<br>
          • <strong>N:</strong> Ay'ın kendi ekseni etrafında dönmesi<br>
          • <strong>O:</strong> Dünya'nın kendi ekseni etrafında dönmesi
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="K: ... gün, L: ... yıl, M: ... gün, N: ... gün, O: ... saat"></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('fen_q6.mp3', 'q_fen_6')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-hint" onclick="portalApp.toggleHint('q_fen_6')">💡 İpucu Al</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_fen_6')">✅ Çözümü Gör</button>
        </div>
        <div class="solution-box">
          <h5>✅ Resmi Çözüm:</h5>
          <div class="solution-content">
            <strong>K (Güneş'in dönmesi):</strong> Yaklaşık 25 gün<br>
            <strong>L (Dünya'nın dolanması):</strong> 365 gün 6 saat (1 yıl)<br>
            <strong>M (Ay'ın dolanması):</strong> Yaklaşık 27 gün 8 saat<br>
            <strong>N (Ay'ın dönmesi):</strong> Yaklaşık 27 gün 8 saat<br>
            <strong>O (Dünya'nın dönmesi):</strong> 24 saat (1 gün)
          </div>
        </div>
        <div class="self-grading">
          <span>Bu sorudan kendine puan ver:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_fen_6', 15, 15, this)">15 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_fen_6', 15, 8, this)">8 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_fen_6', 15, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- Soru 7 -->
      <div class="question-card" id="q_fen_7">
        <div class="q-header">
          <span class="q-badge">Soru 7 • Dinamometre Ölçümleri & Kuvvet</span>
          <span class="q-points">20 Puan</span>
        </div>
        <div class="q-text">
          Özdeş dinamometrelere asılan K cisminin ağırlığı <strong>72 N</strong> olarak ölçülmüş ve dinamometrenin <strong>4 bölme</strong> uzadığı görülmüştür.<br>
          Buna göre diğer cisimlerin ağırlıklarını hesaplayınız:<br>
          • <strong>L cismi:</strong> 1 bölme uzatmıştır.<br>
          • <strong>M cismi:</strong> 2 bölme uzatmıştır.<br>
          • <strong>N cismi:</strong> 3 bölme uzatmıştır.<br>
          • <strong>P cismi:</strong> 5 bölme uzatmıştır.<br>
          • <strong>R cismi:</strong> 6 bölme uzatmıştır.
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="Her 1 bölme = ... N. L=... N, M=... N, N=... N, P=... N, R=... N"></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('fen_q7.mp3', 'q_fen_7')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-hint" onclick="portalApp.toggleHint('q_fen_7')">💡 İpucu Al</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_fen_7')">✅ Çözümü Gör</button>
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('fen_sol7.mp3', 'q_fen_7')">🔊 Çözümü Sesli Dinle</button>
        </div>
        <div class="hint-box">
          <strong>İpucu:</strong> K cismi 72 N iken 4 bölme uzatmışsa, 1 bölmeye düşen kuvvet: 72 ÷ 4 = 18 N'dur!
        </div>
        <div class="solution-box">
          <h5>✅ Adım Adım Resmi Çözüm:</h5>
          <div class="solution-content">
            1. Adım: 1 bölmeye karşılık gelen kuvveti bulalım:<br>
            <strong>72 N ÷ 4 bölme = 18 Newton / bölme</strong><br><br>
            2. Adım: Diğer cisimlerin ağırlıkları:<br>
            • <strong>L:</strong> 1 × 18 = <strong>18 N</strong><br>
            • <strong>M:</strong> 2 × 18 = <strong>36 N</strong><br>
            • <strong>N:</strong> 3 × 18 = <strong>54 N</strong><br>
            • <strong>P:</strong> 5 × 18 = <strong>90 N</strong><br>
            • <strong>R:</strong> 6 × 18 = <strong>108 N</strong>
          </div>
        </div>
        <div class="self-grading">
          <span>Bu sorudan kendine puan ver:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_fen_7', 20, 20, this)">20 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_fen_7', 20, 10, this)">10 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_fen_7', 20, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- Sınavı Bitir Butonu -->
      <div style="text-align: center; margin: 36px 0;">
        <button class="btn-start" style="padding: 16px 32px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 Sınavı Bitir ve Notumu Hesapla
        </button>
      </div>

    </div>

    <!-- TAB 3: ORIGINAL PDF VIEWER -->
    <div id="pdf-pane" class="tab-pane">
      <div style="background: white; border-radius: 12px; padding: 16px; margin-bottom: 20px; border: 1px solid #e2e8f0;">
        <p><strong>📄 5. Sınıf Fen Bilimleri 1. Dönem 1. Yazılı Orijinal Sınav Kağıdı</strong></p>
        <p style="font-size: 0.88rem; color: #64748b;">Sayfa 1 ve 2: Yazılı Sınav Soruları • Sayfa 3 ve 4: Öğretmen Cevap Anahtarı ve Çözümleri</p>
      </div>

      <div class="pdf-pages-grid">
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 1 (Soru Kağıdı)</span><span>1. Dönem 1. Yazılı</span></div>
          <img src="assets/img/fen_p1.png" alt="Fen Sayfa 1" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 2 (Soru Kağıdı)</span><span>1. Dönem 1. Yazılı</span></div>
          <img src="assets/img/fen_p2.png" alt="Fen Sayfa 2" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 3 (Cevap Anahtarı)</span><span>Resmi Çözümler</span></div>
          <img src="assets/img/fen_p3.png" alt="Fen Sayfa 3" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 4 (Cevap Anahtarı)</span><span>Resmi Çözümler</span></div>
          <img src="assets/img/fen_p4.png" alt="Fen Sayfa 4" loading="lazy">
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
</html>"""
    return html

with open(os.path.join(OUTPUT_DIR, "fen-bilimleri.html"), "w", encoding="utf-8") as f:
    f.write(build_fen())
print("fen-bilimleri.html created.")

# -------------------------------------------------------------
# 3. MATEMATİK SAYFASI
# -------------------------------------------------------------
def build_mat():
    html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>5. Sınıf Matematik 1. Dönem 1. Yazılı Hazırlık</title>
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body class="theme-mat">
  {get_header('mat')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>📐</span> Matematik 1. Dönem 1. Yazılı</h1>
        <p>Geometrik Çizim Araçları • Doğru & Işın • Açı Çeşitleri • Çember ve Dikme Çizimi</p>
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
          <strong style="display:block; font-size:0.95rem;">Sesli Matematik Asistanı</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır (Dinlemek için ses butonlarına tıklayın)</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.playAudio('mat_summary.mp3')">📢 Matematik Özetini Dinle</button>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="summary-pane">💡 Sınavda Çıkacak Hap Bilgiler</button>
      <button class="tab-btn" data-tab="questions-pane">📝 10 Soruluk Yazılı Simülatörü</button>
      <button class="tab-btn" data-tab="pdf-pane">📄 Orijinal Sınav Kağıdı & Çözümleri</button>
    </div>

    <!-- TAB 1: SUMMARY -->
    <div id="summary-pane" class="tab-pane active">
      <div id="matSummaryArea" class="summary-cards">
        <div class="summary-card">
          <h4>📏 1. Geometrik Çizim Araçları</h4>
          <ul>
            <li><strong>Cetvel:</strong> Doğru parçalarını ve uzunlukları ölçmek veya düz çizgi çekmek için kullanılır.</li>
            <li><strong>Gönye:</strong> Dik açıları (90°) çizmek ve kontrol etmek için kullanılan üçgen biçimli araçtır.</li>
            <li><strong>Açıölçer (İletki):</strong> Açıların ölçüsünü derece (°) cinsinden ölçmek ve açı çizmek için kullanılır.</li>
            <li><strong>Pergel:</strong> Çember ve daire çizmek, eşit uzunlukta yaylar belirlemek için kullanılan iki kollu araçtır.</li>
          </ul>
        </div>

        <div class="summary-card">
          <h4>🔤 2. Geometrik Kavramlar ve Semboller</h4>
          <ul>
            <li><strong>Doğru [AB veya AB]:</strong> İki ucu da sonsuza giden düz çizgi. Sembol: AB doğrusu veya ⟷AB.</li>
            <li><strong>Doğru Parçası:</strong> İki ucu da sınırlı olan çizgi. Sembol: [AB] veya [BA].</li>
            <li><strong>Işın:</strong> Bir ucu kapalı, diğer ucu sonsuza giden çizgi. Sembol: Başlangıç noktası kapalı köşeli parantez ile gösterilir: [AB (A kapalı, B sonsuz).</li>
          </ul>
        </div>

        <div class="summary-card">
          <h4>📐 3. Açılar, Tümler ve Bütünler</h4>
          <ul>
            <li><strong>Açı:</strong> Başlangıç noktaları ortak iki ışının birleşimidir. Köşe ortada yazılarak gösterilir: s(KLM) veya KLM açısı.</li>
            <li><strong>Komşu Tümler Açılar:</strong> Birer kolları ortak ve ölçüleri toplamı <strong>90°</strong> olan açılardır.</li>
            <li><strong>Komşu Bütünler Açılar:</strong> Birer kolları ortak ve ölçüleri toplamı <strong>180°</strong> olan (doğru açı oluşturan) açılardır.</li>
          </ul>
        </div>

        <div class="summary-card">
          <h4>⭕ 4. Çemberin Temel Elemanları</h4>
          <ul>
            <li><strong>Merkez:</strong> Çemberin tam ortasındaki sabit nokta. Genellikle M veya O harfiyle gösterilir.</li>
            <li><strong>Yarıçap (r):</strong> Merkezden çember üzerindeki herhangi bir noktaya çizilen doğru parçasıdır.</li>
            <li><strong>Çap (R):</strong> Merkezden geçen ve çemberin iki noktasını birleştiren en uzun doğru parçasıdır. <strong>Çap = 2 × Yarıçap (R = 2r)</strong>.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- TAB 2: QUESTIONS -->
    <div id="questions-pane" class="tab-pane">
      
      <!-- S1 -->
      <div class="question-card" id="q_mat_1">
        <div class="q-header">
          <span class="q-badge">Soru 1 • Çizim Araçları</span>
          <span class="q-points">10 Puan</span>
        </div>
        <div class="q-text">
          Aşağıdaki çizim araçlarının isimlerini altlarına yazınız:<br>
          1. Üçgen şeklindeki dik açı ölçüm aracı<br>
          2. Düz çizgi çekme ve uzunluk ölçme aleti<br>
          3. Yarım daire şeklindeki derece ölçme aleti<br>
          4. İki kollu, sivri uçlu çember çizme aleti
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="1: ... , 2: ... , 3: ... , 4: ..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('mat_q1.mp3', 'q_mat_1')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-hint" onclick="portalApp.toggleHint('q_mat_1')">💡 İpucu</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_mat_1')">✅ Çözümü Gör</button>
        </div>
        <div class="hint-box"><strong>İpucu:</strong> Gönye, Cetvel, Açıölçer (İletki), Pergel.</div>
        <div class="solution-box">
          <h5>✅ Resmi Çözüm:</h5>
          <div class="solution-content">
            1. Gönye<br>
            2. Cetvel<br>
            3. Açıölçer (İletki)<br>
            4. Pergel
          </div>
        </div>
        <div class="self-grading">
          <span>Puanın:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_mat_1', 10, 10, this)">10 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_mat_1', 10, 5, this)">5 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_mat_1', 10, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- S2 -->
      <div class="question-card" id="q_mat_2">
        <div class="q-header">
          <span class="q-badge">Soru 2 • Sembolle Gösterim</span>
          <span class="q-points">10 Puan</span>
        </div>
        <div class="q-text">
          A ve V noktalarıyla verilen geometrik çizimleri sembolle gösteriniz:<br>
          <strong>a)</strong> İki ucu da kapalı doğru parçası<br>
          <strong>b)</strong> A ucu kapalı, V ucu sonsuza giden ışın
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="a) [AV] veya ... , b) [AV"></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('mat_q2.mp3', 'q_mat_2')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-hint" onclick="portalApp.toggleHint('q_mat_2')">💡 İpucu</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_mat_2')">✅ Çözümü Gör</button>
        </div>
        <div class="hint-box"><strong>İpucu:</strong> Sınırlı uç için köşeli parantez '[' kullanılır.</div>
        <div class="solution-box">
          <h5>✅ Resmi Çözüm:</h5>
          <div class="solution-content">
            <strong>a)</strong> [AV] veya [VA] (Doğru parçası)<br>
            <strong>b)</strong> [AV (A noktasından kapalı V noktasından sonsuza uzayan ışın)
          </div>
        </div>
        <div class="self-grading">
          <span>Puanın:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_mat_2', 10, 10, this)">10 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_mat_2', 10, 5, this)">5 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_mat_2', 10, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- S3 -->
      <div class="question-card" id="q_mat_3">
        <div class="q-header">
          <span class="q-badge">Soru 3 • Açının Elemanları</span>
          <span class="q-points">10 Puan</span>
        </div>
        <div class="q-text">
          Köşesi L olan, kolları K ve M noktalarından geçen bir açıyla ilgili:<br>
          <strong>a)</strong> Açının kolları nedir?<br>
          <strong>b)</strong> Açının köşesi neresidir?<br>
          <strong>c)</strong> Sembolle 3 farklı gösterimini yazınız.
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="a) Kolları: ... b) Köşesi: ... c) Gösterimleri: ..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('mat_q3.mp3', 'q_mat_3')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_mat_3')">✅ Çözümü Gör</button>
        </div>
        <div class="solution-box">
          <h5>✅ Resmi Çözüm:</h5>
          <div class="solution-content">
            <strong>a) Açının kolları:</strong> [LM ve [LK ışınları<br>
            <strong>b) Açının köşesi:</strong> L noktası<br>
            <strong>c) Sembolle gösterimleri:</strong> ML̂K, KL̂M, L̂ açısı
          </div>
        </div>
        <div class="self-grading">
          <span>Puanın:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_mat_3', 10, 10, this)">10 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_mat_3', 10, 5, this)">5 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_mat_3', 10, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- S4 & S5 -->
      <div class="question-card" id="q_mat_4">
        <div class="q-header">
          <span class="q-badge">Soru 4 & 5 • Çember Çizimi & Elemanları</span>
          <span class="q-points">20 Puan</span>
        </div>
        <div class="q-text">
          <strong>4.</strong> Pergel kullanarak 3 santimetre yarıçaplı bir çember çizimi için adımları açıklayınız.<br>
          <strong>5.</strong> Çemberin elemanlarını (Merkez, Yarıçap, Çap) tanımlayıp çap ile yarıçap arasındaki bağıntıyı yazınız.
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="Çizim adımı ve çember elemanları..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('mat_q4.mp3', 'q_mat_4')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_mat_4')">✅ Çözümü Gör</button>
        </div>
        <div class="solution-box">
          <h5>✅ Resmi Çözüm:</h5>
          <div class="solution-content">
            <strong>Çember Çizimi:</strong> Pergelin kollarının açıklığı cetvel üzerinde 3 cm olarak ayarlanır. İğneli sivri uç merkez noktasına sabitlenir ve kalemli uç 360° döndürülerek 3 cm yarıçaplı çember çizilir.<br><br>
            <strong>Çember Elemanları:</strong><br>
            • <strong>Merkez:</strong> Çemberin tam ortasındaki nokta.<br>
            • <strong>Yarıçap (r):</strong> Merkezden çembere olan uzaklık (3 cm).<br>
            • <strong>Çap (R):</strong> Merkezden geçen iki ucu çember üzerinde olan doğru parçası (6 cm). <strong>R = 2 × r</strong>.
          </div>
        </div>
        <div class="self-grading">
          <span>Puanın:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_mat_4', 20, 20, this)">20 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_mat_4', 20, 10, this)">10 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_mat_4', 20, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- S9 & S10 -->
      <div class="question-card" id="q_mat_9">
        <div class="q-header">
          <span class="q-badge">Soru 9 & 10 • Doğruların Durumu, Tümler & Bütünler Açılar</span>
          <span class="q-points">20 Puan</span>
        </div>
        <div class="q-text">
          <strong>9.</strong> Aynı düzlemdeki iki doğrunun birbirine göre oluşturabileceği 4 durumu yazınız.<br><br>
          <strong>10.</strong> Açı hesaplamalarını yapınız:<br>
          • 40°lik açının <strong>komşu tümleri</strong> olan m(FUR) açısı kaç derecedir?<br>
          • 128°lik açının <strong>komşu bütünleri</strong> olan m(DNY) açısı kaç derecedir?
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="9: Doğruların 4 durumu... 10: m(FUR)=...° , m(DNY)=...°"></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('mat_q9.mp3', 'q_mat_9')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-hint" onclick="portalApp.toggleHint('q_mat_9')">💡 İpucu</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_mat_9')">✅ Çözümü Gör</button>
        </div>
        <div class="hint-box">
          <strong>İpucu:</strong> Tümler açıların toplamı 90°'dir. Bütünler açıların toplamı 180°'dir!
        </div>
        <div class="solution-box">
          <h5>✅ Adım Adım Resmi Çözüm:</h5>
          <div class="solution-content">
            <strong>9. İki Doğrunun Durumları:</strong><br>
            1. Paralel doğrular (d // e - Hiç kesişmezler)<br>
            2. Bir noktada kesişen doğrular<br>
            3. Dik kesişen doğrular (d ⊥ e - Aralarında 90° açı vardır)<br>
            4. Çakışık doğrular (Tüm noktaları ortaktır)<br><br>
            <strong>10. Açı Hesaplamaları:</strong><br>
            • Komşu Tümler: <strong>m(FUR) = 90° - 40° = 50°</strong><br>
            • Komşu Bütünler: <strong>m(DNY) = 180° - 128° = 52°</strong>
          </div>
        </div>
        <div class="self-grading">
          <span>Puanın:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_mat_9', 20, 20, this)">20 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_mat_9', 20, 10, this)">10 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_mat_9', 20, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- Sınavı Bitir Butonu -->
      <div style="text-align: center; margin: 36px 0;">
        <button class="btn-start" style="padding: 16px 32px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 Matematik Notumu Hesapla
        </button>
      </div>

    </div>

    <!-- TAB 3: ORIGINAL PDF VIEWER -->
    <div id="pdf-pane" class="tab-pane">
      <div style="background: white; border-radius: 12px; padding: 16px; margin-bottom: 20px; border: 1px solid #e2e8f0;">
        <p><strong>📄 5. Sınıf Matematik 1. Dönem 1. Yazılı Orijinal Sınav Kağıdı</strong></p>
        <p style="font-size: 0.88rem; color: #64748b;">Sayfa 1 ve 2: Orijinal Soru Kağıdı • Sayfa 3 ve 4: Çizimli Cevap Anahtarı</p>
      </div>

      <div class="pdf-pages-grid">
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 1 (Sorular)</span><span>Matematik Fasikülü</span></div>
          <img src="assets/img/matematik_p1.png" alt="Matematik Sayfa 1" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 2 (Sorular)</span><span>Matematik Fasikülü</span></div>
          <img src="assets/img/matematik_p2.png" alt="Matematik Sayfa 2" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 3 (Çözümler)</span><span>Çizimli Cevaplar</span></div>
          <img src="assets/img/matematik_p3.png" alt="Matematik Sayfa 3" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 4 (Çözümler)</span><span>Çizimli Cevaplar</span></div>
          <img src="assets/img/matematik_p4.png" alt="Matematik Sayfa 4" loading="lazy">
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
</html>"""
    return html

with open(os.path.join(OUTPUT_DIR, "matematik.html"), "w", encoding="utf-8") as f:
    f.write(build_mat())
print("matematik.html created.")

# -------------------------------------------------------------
# 4. TÜRKÇE SAYFASI
# -------------------------------------------------------------
def build_turkce():
    html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>5. Sınıf Türkçe 1. Dönem 1. Yazılı Hazırlık</title>
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body class="theme-turkce">
  {get_header('turkce')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>📚</span> Türkçe 1. Dönem 1. Yazılı</h1>
        <p>Metinde Anlam • Sözcük Dağarcığı • Kişileştirme Sanatı • Yazım ve Noktalama Kuralları</p>
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
          <strong style="display:block; font-size:0.95rem;">Sesli Türkçe Rehberi</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır (Dinlemek için ses butonlarına tıklayın)</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.playAudio('turkce_summary.mp3')">📢 Türkçe Konu Özetini Dinle</button>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="summary-pane">💡 Sınavda Çıkacak Hap Bilgiler</button>
      <button class="tab-btn" data-tab="questions-pane">📝 İnteraktif Yazılı Soruları</button>
      <button class="tab-btn" data-tab="pdf-pane">📄 Orijinal Sınav Kağıdı & Çözümleri</button>
    </div>

    <!-- TAB 1: SUMMARY -->
    <div id="summary-pane" class="tab-pane active">
      <div id="turkceSummaryArea" class="summary-cards">
        <div class="summary-card">
          <h4>📖 1. Sözcükte Anlam ve Bağlam</h4>
          <ul>
            <li><strong>Gerçek Anlam:</strong> Kelimenin akla gelen ilk ve temel anlamıdır. (Örn: "Ateşte su kaynadı.")</li>
            <li><strong>Mecaz Anlam:</strong> Kelimenin gerçek anlamından tamamen uzaklaşarak kazandığı yeni anlamdır. (Örn: "Öfkeden kaynıyordu.")</li>
            <li><strong>Terim Anlam:</strong> Bilim, sanat, spor veya meslek dalına özgü özel kavramlardır. (Örn: "Mıknatıs", "Doğru parçası", "Pusula".)</li>
          </ul>
        </div>

        <div class="summary-card">
          <h4>🎭 2. Söz Sanatları: Kişileştirme (Teşhis)</h4>
          <ul>
            <li><strong>Tanım:</strong> İnsana ait özelliklerin (ağlama, sevinme, konuşma, öfkelenme) insan dışındaki canlı veya cansız varlıklara aktarılması sanatıdır.</li>
            <li><strong>Örnek 1:</strong> "Rüzgâr öfkeyle pencereleri dövüyordu." (Öfkelenmek insana aittir, rüzgâra verilmiştir.)</li>
            <li><strong>Örnek 2:</strong> "Küçük papatya sabah güneşine tebessüm etti." (Tebessüm etmek insana aittir.)</li>
          </ul>
        </div>

        <div class="summary-card">
          <h4>✍️ 3. Kritik Yazım Kuralları (Büyük Harfler)</h4>
          <ul>
            <li><strong>Belirli Tarihler:</strong> Belirli bir tarihi bildiren ay ve gün adları büyük yazılır. (Örn: "29 Ekim 1923", "Sınav 15 Kasım Cuma günü.") Ancak belirli tarih bildirmeyenler küçük yazılır ("Okullar eylülde açılır").</li>
            <li><strong>Yer Adlarında İkinci İsim:</strong> İlk isimden sonra gelen deniz, göl, nehir, dağ, boğaz tür bildiren ikinci isimler büyük harfle başlar: <em>Van Gölü, Ağrı Dağı, Çanakkale Boğazı, Dicle Nehri</em>.</li>
            <li><strong>Cadde, Sokak, Meydan:</strong> Mahalle, meydan, bulvar, cadde, sokak kelimeleri büyük harfle başlar: <em>Atatürk Bulvarı, Karanfil Sokak, Taksim Meydanı</em>.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- TAB 2: QUESTIONS -->
    <div id="questions-pane" class="tab-pane">
      
      <!-- S1 -->
      <div class="question-card" id="q_tr_1">
        <div class="q-header">
          <span class="q-badge">Soru 1 • Metinden Sözcük Bulma</span>
          <span class="q-points">15 Puan</span>
        </div>
        <div class="q-text">
          <em>Metin: "Adını İtalyanca 'bussola' kelimesinden alan, üzerindeki mıknatıs iğnesiyle yön bulmaya yarayan ve âdeta 'yüzyılın icadı' olarak tanımlayabileceğimiz pusulanın tarihi oldukça eskiye dayanır. İcadından önce ağaçların üzerindeki yosunlara ve yıldızlara bakarak bulunan yönler, pusulanın icat edilmesinden sonra daha doğru ve daha hızlı şekilde saptanabilir oldu."</em><br><br>
          Aşağıda anlamları verilen sözcükleri yukarıdaki metinden bularak yazınız:<br>
          • 1: Bilinen bilgilerden yararlanarak daha önce bilinmeyen yeni bir bulguya ulaşma veya yöntem geliştirme, buluş.<br>
          • 2: Çoğu sularda, ağaç veya taşların üzerinde yetişen tallı bitkilerin ilkel yapıdaki örnekleri.<br>
          • 3: Demiri ve daha başka bazı metalleri çeken demir oksit; demirkapan.
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="1: ... , 2: ... , 3: ..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('turkce_q1.mp3', 'q_tr_1')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-hint" onclick="portalApp.toggleHint('q_tr_1')">💡 İpucu</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_tr_1')">✅ Çözümü Gör</button>
        </div>
        <div class="hint-box"><strong>İpucu:</strong> Metindeki koyu sözcükleri düşün: icat, yosun, mıknatıs.</div>
        <div class="solution-box">
          <h5>✅ Resmi Çözüm:</h5>
          <div class="solution-content">
            1. <strong>İcat</strong> (Buluş)<br>
            2. <strong>Yosun</strong><br>
            3. <strong>Mıknatıs</strong>
          </div>
        </div>
        <div class="self-grading">
          <span>Puanın:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_tr_1', 15, 15, this)">15 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_tr_1', 15, 8, this)">8 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_tr_1', 15, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- S2 -->
      <div class="question-card" id="q_tr_2">
        <div class="q-header">
          <span class="q-badge">Soru 2 • Metin Anlama (Yapay Zekâ ve Çevre)</span>
          <span class="q-points">20 Puan</span>
        </div>
        <div class="q-text">
          <em>Metin: "Yapay zekânın çevre üzerindeki etkisi sadece elektrikle sınırlı kalmıyor. Bu sistemlerin çalıştığı devasa veri merkezlerindeki sunucuların soğutulması için yüksek miktarda su tüketiliyor. Araştırmalar, yapay zekâ ile yapılan yaklaşık 20 ila 50 soruluk bir sohbetin yaklaşık yarım litrelik bir su tüketimine denk geldiğini gösteriyor. Soruya eklenen gereksiz her ifade, işlem süresini uzatarak bu tüketimi doğrudan artırıyor."</em><br><br>
          Metne göre:<br>
          <strong>a)</strong> Yapay zekâ sunucularında neden yüksek miktarda su tüketilmektedir?<br>
          <strong>b)</strong> Kullanıcıların sorularına eklediği gereksiz ifadeler çevre tüketimini nasıl etkilemektedir?
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="a) Tüketim sebebi:... b) Gereksiz ifadelerin etkisi:..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('turkce_q2.mp3', 'q_tr_2')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_tr_2')">✅ Çözümü Gör</button>
        </div>
        <div class="solution-box">
          <h5>✅ Resmi Çözüm:</h5>
          <div class="solution-content">
            <strong>a)</strong> Devasa veri merkezlerindeki sunucuların soğutulması amacıyla yüksek miktarda su tüketilmektedir.<br>
            <strong>b)</strong> Gereksiz ifadeler işlem süresini uzatmakta, bu da enerji ve su tüketimini doğrudan artırmaktadır.
          </div>
        </div>
        <div class="self-grading">
          <span>Puanın:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_tr_2', 20, 20, this)">20 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_tr_2', 20, 10, this)">10 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_tr_2', 20, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- S4 -->
      <div class="question-card" id="q_tr_4">
        <div class="q-header">
          <span class="q-badge">Soru 4 • Söz Sanatları (Kişileştirme)</span>
          <span class="q-points">15 Puan</span>
        </div>
        <div class="q-text">
          Söz sanatlarından <strong>kişileştirmeye (teşhis)</strong> uygun iki farklı örnek cümle yazınız.
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="1. Örnek cümle:... 2. Örnek cümle:..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('turkce_q4.mp3', 'q_tr_4')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-hint" onclick="portalApp.toggleHint('q_tr_4')">💡 İpucu</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_tr_4')">✅ Çözümü Gör</button>
        </div>
        <div class="hint-box"><strong>İpucu:</strong> İnsanın konuşması, ağlaması, küsmesi gibi davranışları bir hayvana, ağaca ya da buluta verin.</div>
        <div class="solution-box">
          <h5>✅ Öğretmen Model Örnekleri:</h5>
          <div class="solution-content">
            • <strong>1. Örnek:</strong> "Yorgun rüzgâr akşam olunca ağaçların dallarına yaslanıp dinlendi."<br>
            • <strong>2. Örnek:</strong> "Bulutlar gökyüzünde dertleşir gibi birbirine sokuldu."
          </div>
        </div>
        <div class="self-grading">
          <span>Puanın:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_tr_4', 15, 15, this)">15 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_tr_4', 15, 8, this)">8 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_tr_4', 15, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- S5 -->
      <div class="question-card" id="q_tr_5">
        <div class="q-header">
          <span class="q-badge">Soru 5 • Yazım Kuralları</span>
          <span class="q-points">30 Puan</span>
        </div>
        <div class="q-text">
          Aşağıdaki yazım kurallarını örnekleyen birer cümle yazınız (Her biri 10 Puan):<br><br>
          <strong>I.</strong> Belirli bir tarih bildiren ay ve gün adları büyük harfle başlar.<br>
          <strong>II.</strong> Yer adlarında ilk isimden sonra gelen ve deniz, nehir, göl, dağ, boğaz vb. tür bildiren ikinci isimler büyük harfle başlar.<br>
          <strong>III.</strong> Mahalle, meydan, bulvar, cadde, sokak adlarında geçen kelimeler büyük harfle başlar.
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="I. Cümle:... II. Cümle:... III. Cümle:..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('turkce_q5.mp3', 'q_tr_5')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_tr_5')">✅ Çözümü Gör</button>
        </div>
        <div class="solution-box">
          <h5>✅ Model Cümleler (Tam Puan Kriteri):</h5>
          <div class="solution-content">
            <strong>I. Kural Örneği:</strong> "Kardeşim <strong>12 Mayıs 2018 Cumartesi</strong> günü dünyaya geldi." (Belirli bir gün ve ay adı büyük yazılmıştır.)<br><br>
            <strong>II. Kural Örneği:</strong> "Yaz tatilinde ailece <strong>Van Gölü</strong> kıyısında piknik yaptık." (Göl adı büyük harfle başlamıştır.)<br><br>
            <strong>III. Kural Örneği:</strong> "Yeni açılan kütüphane <strong>Cumhuriyet Caddesi, Çiçek Sokak</strong> üzerinde bulunuyor." (Cadde ve sokak kelimeleri büyük yazılmıştır.)
          </div>
        </div>
        <div class="self-grading">
          <span>Puanın:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_tr_5', 30, 30, this)">30 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_tr_5', 30, 15, this)">15 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_tr_5', 30, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- Sınavı Bitir Butonu -->
      <div style="text-align: center; margin: 36px 0;">
        <button class="btn-start" style="padding: 16px 32px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 Türkçe Notumu Hesapla
        </button>
      </div>

    </div>

    <!-- TAB 3: ORIGINAL PDF VIEWER -->
    <div id="pdf-pane" class="tab-pane">
      <div style="background: white; border-radius: 12px; padding: 16px; margin-bottom: 20px; border: 1px solid #e2e8f0;">
        <p><strong>📄 5. Sınıf Türkçe 1. Dönem 1. Yazılı Orijinal Sınav Kağıdı</strong></p>
        <p style="font-size: 0.88rem; color: #64748b;">Sayfa 1 ve 2: Orijinal Sınav Kağıdı • Sayfa 3 ve 4: Öğretmen Cevap Anahtarı</p>
      </div>

      <div class="pdf-pages-grid">
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 1 (Sorular)</span><span>1. Dönem 1. Yazılı</span></div>
          <img src="assets/img/turkce_p1.png" alt="Türkçe Sayfa 1" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 2 (Sorular)</span><span>1. Dönem 1. Yazılı</span></div>
          <img src="assets/img/turkce_p2.png" alt="Türkçe Sayfa 2" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 3 (Çözümler)</span><span>Resmi Cevaplar</span></div>
          <img src="assets/img/turkce_p3.png" alt="Türkçe Sayfa 3" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 4 (Çözümler)</span><span>Resmi Cevaplar</span></div>
          <img src="assets/img/turkce_p4.png" alt="Türkçe Sayfa 4" loading="lazy">
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
</html>"""
    return html

with open(os.path.join(OUTPUT_DIR, "turkce.html"), "w", encoding="utf-8") as f:
    f.write(build_turkce())
print("turkce.html created.")

# -------------------------------------------------------------
# 5. SOSYAL BİLGİLER SAYFASI
# -------------------------------------------------------------
def build_sosyal():
    html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>5. Sınıf Sosyal Bilgiler 1. Dönem 1. Yazılı Hazırlık</title>
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body class="theme-sosyal">
  {get_header('sosyal')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>🌍</span> Sosyal Bilgiler 1. Dönem 1. Yazılı</h1>
        <p>Birey ve Toplum • Rollerimiz & Haklarımız • Sadaka Taşı Kültürü • Millî Mücadele Dayanışması</p>
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
          <strong style="display:block; font-size:0.95rem;">Sesli Sosyal Bilgiler Asistanı</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır (Dinlemek için ses butonlarına tıklayın)</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.playAudio('sosyal_summary.mp3')">📢 Sosyal Bilgiler Özetini Dinle</button>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="summary-pane">💡 Sınavda Çıkacak Hap Bilgiler</button>
      <button class="tab-btn" data-tab="questions-pane">📝 İnteraktif Yazılı Soruları</button>
      <button class="tab-btn" data-tab="pdf-pane">📄 Orijinal Sınav Kağıdı & Çözümleri</button>
    </div>

    <!-- TAB 1: SUMMARY -->
    <div id="summary-pane" class="tab-pane active">
      <div id="sosyalSummaryArea" class="summary-cards">
        <div class="summary-card">
          <h4>👥 1. Hak, Sorumluluk ve Rol</h4>
          <ul>
            <li><strong>Hak:</strong> Hukukun ve kanunların bireylere tanıdığı yetki ve olanaklardır (Eğitim hakkı, sağlık hakkı, oyun oynama hakkı).</li>
            <li><strong>Rol:</strong> Bir grup veya kurumda üzerimize düşen görev ve konumdur (Öğrenci, evlat, abi, kaleci vb.). Birey aynı anda birden fazla role sahip olabilir!</li>
            <li><strong>Sorumluluk:</strong> Üstlendiğimiz rollerin gerektirdiği ödevleri yerine getirme bilincidir.</li>
          </ul>
        </div>

        <div class="summary-card">
          <h4>🏺 2. Tarihte Yardımlaşma: Sadaka Taşları</h4>
          <ul>
            <li><strong>Nedir:</strong> Selçuklu ve Osmanlı döneminde cami, çeşme ve meydanlara konulan oyuk taşlardır.</li>
            <li><strong>Amacı:</strong> Varlıklı kimseler kimseye görünmeden bu taşa para bırakır, ihtiyaç sahipleri ise geceleri sadece ihtiyacı kadarını alırdı.</li>
            <li><strong>Kazanımı:</strong> İhtiyaç sahiplerini rencide etmeden, gururunu kırmadan yardımlaşma ve dayanışmayı sağlamaktır.</li>
          </ul>
        </div>

        <div class="summary-card">
          <h4>🇹🇷 3. Millî Mücadele ve Dayanışma</h4>
          <ul>
            <li><strong>Tekâlif-i Milliye:</strong> Mustafa Kemal Paşa tarafından Sakarya Meydan Muharebesi öncesi ordunun ihtiyaçlarını karşılamak için yayımlanan millî emirlerdir.</li>
            <li><strong>Milletin Rolü:</strong> Türk milleti çorap, çarık, yiyecek, at arabası ve silahını orduyla paylaşarak eşsiz bir dayanışma örneği sergilemiştir.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- TAB 2: QUESTIONS -->
    <div id="questions-pane" class="tab-pane">
      
      <!-- S1 -->
      <div class="question-card" id="q_sos_1">
        <div class="q-header">
          <span class="q-badge">Soru 1 • Sorumluluk ve Roller</span>
          <span class="q-points">10 Puan</span>
        </div>
        <div class="q-text">
          Bu sorumlulukların yerine getirilmesini isteyen rollerin adlarını yazınız:<br>
          1. "Öğrencilerle ilgilenmek, görev ve sorumluluklarını onlara hatırlatmak." ➔ Bu rol: ...<br>
          2. "Ev işlerinde çocukların yardımcı olmasını istemek." ➔ Bu rol: ...
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="1. Rol: ... , 2. Rol: ..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('sosyal_q1.mp3', 'q_sos_1')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_sos_1')">✅ Çözümü Gör</button>
        </div>
        <div class="solution-box">
          <h5>✅ Resmi Çözüm:</h5>
          <div class="solution-content">
            1. <strong>Öğretmen</strong><br>
            2. <strong>Anne / Baba</strong> (Ebeveyn)
          </div>
        </div>
        <div class="self-grading">
          <span>Puanın:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_sos_1', 10, 10, this)">10 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_sos_1', 10, 5, this)">5 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_sos_1', 10, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- S2 -->
      <div class="question-card" id="q_sos_2">
        <div class="q-header">
          <span class="q-badge">Soru 2 • Osman Furkan'ın Rolleri</span>
          <span class="q-points">20 Puan</span>
        </div>
        <div class="q-text">
          <em>Metin: "Osman Furkan evde anne baba ve küçük kardeşiyle birlikte yaşamaktadır. Yeşilyurt Ortaokulu 5. sınıfta okumaktadır. Okulun futbol takımında takım lideri olarak oynamaktadır."</em><br><br>
          Metne göre Osman Furkan'ın içinde bulunduğu gruplardaki 4 farklı rolünü yazınız.
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="1: ... , 2: ... , 3: ... , 4: ..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('sosyal_q2.mp3', 'q_sos_2')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_sos_2')">✅ Çözümü Gör</button>
        </div>
        <div class="solution-box">
          <h5>✅ Resmi Çözüm (Tam Puan Kriteri):</h5>
          <div class="solution-content">
            1. Anne babasına göre: <strong>Evlat (Çocuk)</strong><br>
            2. Küçük kardeşine göre: <strong>Ağabey (Abi)</strong><br>
            3. Yeşilyurt Ortaokulunda: <strong>Öğrenci</strong><br>
            4. Futbol takımında: <strong>Takım Kaptanı (Lideri / Sporcu)</strong>
          </div>
        </div>
        <div class="self-grading">
          <span>Puanın:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_sos_2', 20, 20, this)">20 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_sos_2', 20, 10, this)">10 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_sos_2', 20, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- S5 -->
      <div class="question-card" id="q_sos_5">
        <div class="q-header">
          <span class="q-badge">Soru 5 • Sadaka Taşı Uygulaması</span>
          <span class="q-points">20 Puan</span>
        </div>
        <div class="q-text">
          <em>"Selçuklu ve Osmanlı Dönemi'nde meydanlara, cami ve çeşme yanlarına yardımlaşma amaçlı konurdu. İhtiyaç sahiplerine yardım etmek isteyenler bu taşın içine para bırakırdı. Böylece ihtiyaç sahibi kişiler gecenin geç saatlerini bekler, kimseye görünmeden ihtiyacı kadar olan parayı bu taşın içinden alırdı."</em><br><br>
          Metinde bahsedilen uygulamanın adı nedir ve hangi amaçla yapılmıştır?
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="Uygulamanın adı: ... Yapılış amacı: ..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('sosyal_q5.mp3', 'q_sos_5')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_sos_5')">✅ Çözümü Gör</button>
        </div>
        <div class="solution-box">
          <h5>✅ Resmi Çözüm:</h5>
          <div class="solution-content">
            • <strong>Uygulamanın Adı:</strong> Sadaka Taşı<br>
            • <strong>Amacı:</strong> İhtiyaç sahiplerini incitmeden, mahcup etmeden gizlice yardım etmek ve toplumda birlik, beraberlik ve yardımlaşmayı güçlendirmek.
          </div>
        </div>
        <div class="self-grading">
          <span>Puanın:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_sos_5', 20, 20, this)">20 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_sos_5', 20, 10, this)">10 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_sos_5', 20, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- Sınavı Bitir Butonu -->
      <div style="text-align: center; margin: 36px 0;">
        <button class="btn-start" style="padding: 16px 32px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 Sosyal Bilgiler Notumu Hesapla
        </button>
      </div>

    </div>

    <!-- TAB 3: ORIGINAL PDF VIEWER -->
    <div id="pdf-pane" class="tab-pane">
      <div style="background: white; border-radius: 12px; padding: 16px; margin-bottom: 20px; border: 1px solid #e2e8f0;">
        <p><strong>📄 5. Sınıf Sosyal Bilgiler 1. Dönem 1. Yazılı Orijinal Sınav Kağıdı</strong></p>
        <p style="font-size: 0.88rem; color: #64748b;">Sayfa 1 ve 2: Orijinal Soru Kağıdı • Sayfa 3 ve 4: Resmi Çözümler</p>
      </div>

      <div class="pdf-pages-grid">
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 1 (Sorular)</span><span>Sosyal Bilgiler</span></div>
          <img src="assets/img/sosyal_p1.png" alt="Sosyal Sayfa 1" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 2 (Sorular)</span><span>Sosyal Bilgiler</span></div>
          <img src="assets/img/sosyal_p2.png" alt="Sosyal Sayfa 2" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 3 (Çözümler)</span><span>Resmi Cevaplar</span></div>
          <img src="assets/img/sosyal_p3.png" alt="Sosyal Sayfa 3" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 4 (Çözümler)</span><span>Resmi Cevaplar</span></div>
          <img src="assets/img/sosyal_p4.png" alt="Sosyal Sayfa 4" loading="lazy">
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
</html>"""
    return html

with open(os.path.join(OUTPUT_DIR, "sosyal-bilgiler.html"), "w", encoding="utf-8") as f:
    f.write(build_sosyal())
print("sosyal-bilgiler.html created.")

# -------------------------------------------------------------
# 6. DİN KÜLTÜRÜ VE AHLAK BİLGİSİ SAYFASI
# -------------------------------------------------------------
def build_din():
    html = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>5. Sınıf Din Kültürü 1. Dönem 1. Yazılı Hazırlık</title>
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body class="theme-din">
  {get_header('din')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>🕌</span> Din Kültürü ve Ahlak Bilgisi 1. Dönem 1. Yazılı</h1>
        <p>Evrendeki Mükemmel Düzen • Esmâ-i Hüsnâ (Alîm, Semî, Basîr, Kadîr) • İhlas Suresi ve Meali</p>
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
          <strong style="display:block; font-size:0.95rem;">Sesli Din Kültürü Asistanı</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır (Dinlemek için ses butonlarına tıklayın)</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.playAudio('din_summary.mp3')">📢 Din Kültürü Özetini Dinle</button>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="summary-pane">💡 Sınavda Çıkacak Hap Bilgiler</button>
      <button class="tab-btn" data-tab="questions-pane">📝 İnteraktif Soru Bankası</button>
      <button class="tab-btn" data-tab="pdf-pane">📄 Orijinal Sınav Kağıdı & Çözümleri</button>
    </div>

    <!-- TAB 1: SUMMARY -->
    <div id="summary-pane" class="tab-pane active">
      <div id="dinSummaryArea" class="summary-cards">
        <div class="summary-card">
          <h4>🌌 1. Evrendeki Mükemmel Düzen</h4>
          <ul>
            <li>Evrendeki her şey bir ölçü, denge ve nizam içerisinde yaratılmıştır.</li>
            <li><strong>Örnekler:</strong> Gece ve gündüzün ardı ardına gelmesi, mevsimlerin döngüsü, suyun buharlaşıp yağmur olarak yağması, Güneş ile Dünya arasındaki kusursuz mesafe.</li>
            <li>Eğer birden fazla ilah olsaydı bu düzen bozulur, evrende kaos çıkardı.</li>
          </ul>
        </div>

        <div class="summary-card">
          <h4>✨ 2. Allah'ın Güzel İsimleri (Esmâ-i Hüsnâ)</h4>
          <ul>
            <li><strong>Esmâ-i Hüsnâ:</strong> Allah'ın Kur'an-ı Kerim ve hadislerde bildirilen 99 güzel ismidir.</li>
            <li><strong>Alîm:</strong> Her şeyi, gizliyi ve açığı, geçmişi ve geleceği hakkıyla bilen.</li>
            <li><strong>Semî:</strong> Fısıltıları dahi her şeyi hakkıyla işiten.</li>
            <li><strong>Basîr:</strong> Karanlıkta bir karıncanın yürüyüşünü dahi her şeyi gören.</li>
            <li><strong>Kadîr:</strong> Sonsuz güç sahibi olan, her şeye gücü yeten.</li>
            <li><strong>Rahmân & Rahîm:</strong> Dünyada ve ahirette sınırsız merhamet ve şefkat gösteren.</li>
          </ul>
        </div>

        <div class="summary-card">
          <h4>📖 3. İhlas Suresi ve Tevhit İnancı</h4>
          <ul>
            <li><strong>Tevhit:</strong> Allah'ın bir ve tek olduğuna, eşi ve benzeri bulunmadığına inanmaktır.</li>
            <li><strong>İhlas:</strong> Samimiyet, içtenlik, kalbi batıl inançlardan arındırmak demektir.</li>
            <li><strong>Okunuşu:</strong> Bismillâhirrahmânirrahîm. 1. Kul hüvellâhü ehad. 2. Allâhü's-samed. 3. Lem yelid ve lem yûled. 4. Ve lem yekün lehû küfüven ehad.</li>
            <li><strong>Samed İsmi:</strong> Herkes ve her şey O'na muhtaç iken, O'nun hiçbir şeye muhtaç olmamasıdır.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- TAB 2: QUESTIONS -->
    <div id="questions-pane" class="tab-pane">
      
      <!-- S1 -->
      <div class="question-card" id="q_din_1">
        <div class="q-header">
          <span class="q-badge">Bölüm A • Evrendeki Denge ve Düzen</span>
          <span class="q-points">15 Puan</span>
        </div>
        <div class="q-text">
          Allah'ın evreni bir denge ve düzen içinde yaratmasına 3 örnek yazınız. (3 x 5 = 15 Puan)
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="1. Örnek: ... 2. Örnek: ... 3. Örnek: ..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('din_q1.mp3', 'q_din_1')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_din_1')">✅ Çözümü Gör</button>
        </div>
        <div class="solution-box">
          <h5>✅ Resmi Çözüm:</h5>
          <div class="solution-content">
            1. Gece ve gündüzün düzenli olarak birbirini izlemesi.<br>
            2. Mevsimlerin belli bir düzen ve sırayla değişmesi.<br>
            3. Yağmur döngüsüyle birlikte bitkilerin büyüyüp besin üretmesi.
          </div>
        </div>
        <div class="self-grading">
          <span>Puanın:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_din_1', 15, 15, this)">15 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_din_1', 15, 10, this)">10 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_din_1', 15, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- S2 -->
      <div class="question-card" id="q_din_2">
        <div class="q-header">
          <span class="q-badge">Bölüm B • Esmâ-i Hüsnâ Eşleştirme</span>
          <span class="q-points">30 Puan</span>
        </div>
        <div class="q-text">
          Aşağıdaki ayet meallerinin Allah'ın hangi güzel ismine işaret ettiğini yazınız:<br><br>
          • 1: <em>"… O, göklerde ve yerde olan her şeyi bilir."</em> ➔ İsim: ...<br>
          • 2: <em>"Allah her şeyi hakkıyla işitmekte ve her şeyi görmektedir."</em> ➔ İsimler: ...<br>
          • 3: <em>"O, her şeye hakkıyla gücü yetendir."</em> ➔ İsim: ...
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="1. ... , 2. ... , 3. ..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('din_q2.mp3', 'q_din_2')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_din_2')">✅ Çözümü Gör</button>
        </div>
        <div class="solution-box">
          <h5>✅ Resmi Çözüm:</h5>
          <div class="solution-content">
            • 1. Bilen ➔ <strong>Alîm</strong><br>
            • 2. İşiten ve Gören ➔ <strong>Semî</strong> ve <strong>Basîr</strong><br>
            • 3. Gücü yeten ➔ <strong>Kadîr</strong>
          </div>
        </div>
        <div class="self-grading">
          <span>Puanın:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_din_2', 30, 30, this)">30 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_din_2', 30, 15, this)">15 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_din_2', 30, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- S4 & S5 -->
      <div class="question-card" id="q_din_4">
        <div class="q-header">
          <span class="q-badge">Bölüm D & E • İhlas Suresi & Doğru-Yanlış</span>
          <span class="q-points">45 Puan</span>
        </div>
        <div class="q-text">
          <strong>I. İhlas Suresi Boşluklarını Tamamlayınız:</strong><br>
          1. Kul huvallahu ...........<br>
          2. .................... samed<br>
          3. Lem ........... ve lem ...........<br>
          4. .................... yeküllehu küfüven ehad<br><br>
          <strong>II. Doğru / Yanlış İfadeleri:</strong><br>
          • Tevhit inancı İslam'ın özünü oluşturan esaslardan biridir. (D/Y?)<br>
          • Samed ismi; herkesin Allah'a muhtaç olduğunu, O'nun hiçbir şeye muhtaç olmadığını ifade eder. (D/Y?)<br>
          • Eğer evrende birden fazla yaratıcı olsaydı daha iyi bir düzen olurdu. (D/Y?)
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="İhlas suresi tamamlaması ve D/Y cevapları..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('din_q4.mp3', 'q_din_4')">🔊 Soruyu Dinle</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_din_4')">✅ Çözümü Gör</button>
        </div>
        <div class="solution-box">
          <h5>✅ Resmi Çözüm:</h5>
          <div class="solution-content">
            <strong>İhlas Suresi:</strong><br>
            1. Kul huvallahu <strong>ehad</strong><br>
            2. <strong>Allahu's</strong> samed<br>
            3. Lem <strong>yelid</strong> ve lem <strong>yûled</strong><br>
            4. <strong>Ve lem</strong> yeküllehu küfüven ehad<br><br>
            <strong>Doğru / Yanlış:</strong><br>
            • Tevhit inancı öz esastır ➔ <strong>DOĞRU</strong><br>
            • Samed muhtaç olmamaktır ➔ <strong>DOĞRU</strong><br>
            • Birden fazla yaratıcı olsaydı düzen olurdu ➔ <strong>YANLIŞ</strong> (Düzen bozulurdu)
          </div>
        </div>
        <div class="self-grading">
          <span>Puanın:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_din_4', 45, 45, this)">45 Puan</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_din_4', 45, 25, this)">25 Puan</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_din_4', 45, 0, this)">0 Puan</button>
        </div>
      </div>

      <!-- Sınavı Bitir Butonu -->
      <div style="text-align: center; margin: 36px 0;">
        <button class="btn-start" style="padding: 16px 32px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 Din Kültürü Notumu Hesapla
        </button>
      </div>

    </div>

    <!-- TAB 3: ORIGINAL PDF VIEWER -->
    <div id="pdf-pane" class="tab-pane">
      <div style="background: white; border-radius: 12px; padding: 16px; margin-bottom: 20px; border: 1px solid #e2e8f0;">
        <p><strong>📄 5. Sınıf Din Kültürü 1. Dönem 1. Yazılı Orijinal Sınav Kağıdı</strong></p>
        <p style="font-size: 0.88rem; color: #64748b;">AV Yayınları 5. Sınıf Yazılı Çalışma Fasikülü ve Çözümleri</p>
      </div>

      <div class="pdf-pages-grid">
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 1 (Konu Özeti)</span><span>Din Kültürü</span></div>
          <img src="assets/img/din_p1.png" alt="Din Sayfa 1" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 2 (Sorular)</span><span>Din Kültürü</span></div>
          <img src="assets/img/din_p2.png" alt="Din Sayfa 2" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 3 (Sorular)</span><span>Din Kültürü</span></div>
          <img src="assets/img/din_p3.png" alt="Din Sayfa 3" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 4 (Çözümler)</span><span>Resmi Cevaplar</span></div>
          <img src="assets/img/din_p4.png" alt="Din Sayfa 4" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Sayfa 5 (Çözümler)</span><span>Resmi Cevaplar</span></div>
          <img src="assets/img/din_p5.png" alt="Din Sayfa 5" loading="lazy">
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
</html>"""
    return html

with open(os.path.join(OUTPUT_DIR, "din-kulturu.html"), "w", encoding="utf-8") as f:
    f.write(build_din())
print("din-kulturu.html created.")

# -------------------------------------------------------------
# 7. İNGİLİZCE SAYFASI (English with en-US TTS)
# -------------------------------------------------------------
def build_ingilizce():
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>5th Grade English 1st Term 1st Exam Practice</title>
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body class="theme-ingilizce">
  {get_header('ingilizce')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>🇬🇧</span> 5. Sınıf İngilizce 1. Dönem 1. Yazılı</h1>
        <p>School Life • Telling the Time • Mia's Daily Routine • Must & Mustn't</p>
      </div>
      <div class="score-box">
        <div class="score-val" id="currentScoreVal">0</div>
        <div class="score-lbl">Score / 100</div>
      </div>
    </div>

    <!-- Master Audio Bar -->
    <div class="audio-bar">
      <div class="audio-bar-info">
        <div class="audio-icon-pulse">🔊</div>
        <div>
          <strong style="display:block; font-size:0.95rem;">English Voice Assistant (Native Audio)</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Ready (Click audio buttons to hear native pronunciation)</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Pause / Resume</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Stop</button>
        <button class="btn-audio primary" onclick="portalApp.playAudio('ingilizce_summary.mp3')">📢 Listen All Grammar Notes</button>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="summary-pane">💡 Grammar Cheat-Sheet & Notes</button>
      <button class="tab-btn" data-tab="questions-pane">📝 Interactive Exam Questions</button>
      <button class="tab-btn" data-tab="pdf-pane">📄 Original Exam Sheets & Keys</button>
    </div>

    <!-- TAB 1: SUMMARY -->
    <div id="summary-pane" class="tab-pane active">
      <div id="engSummaryArea" class="summary-cards">
        <div class="summary-card">
          <h4>⏰ 1. Telling the Time (Saatler)</h4>
          <ul>
            <li><strong>Tam Saatler:</strong> It is ... o'clock. (Örn: <em>It is two o'clock.</em>)</li>
            <li><strong>Geçiyor (Past):</strong> It is ... past ... (Örn: <em>It is ten past three.</em> / <em>It is quarter past four.</em>)</li>
            <li><strong>Buçuk (Half past):</strong> It is half past ... (Örn: <em>It is half past six.</em>)</li>
            <li><strong>Kala (To):</strong> It is ... to ... (Örn: <em>It is quarter to ten.</em>)</li>
          </ul>
        </div>

        <div class="summary-card">
          <h4>🔤 2. Articles (a / an / the)</h4>
          <ul>
            <li><strong>a:</strong> Sessiz harfle başlayan isimlerin önüne gelir: <em>a book, a cat, a university student</em>.</li>
            <li><strong>an:</strong> Sesli harfle okunan isimlerin önüne gelir: <em>an apple, an elephant, an hour</em>.</li>
            <li><strong>the:</strong> Belirli, önceden bilinen varlıklar için kullanılır: <em>Open the door, look at the sun</em>.</li>
          </ul>
        </div>

        <div class="summary-card">
          <h4>📅 3. Daily Routine & Present Simple</h4>
          <ul>
            <li>He / She / It öznelerinde fiile <strong>-s, -es, -ies</strong> takısı gelir: <em>like - likes, brush - brushes, study - studies</em>.</li>
            <li>Zaman zarfları: <em>in the morning, at noon, at night, on Monday, every day</em>.</li>
          </ul>
        </div>

        <div class="summary-card">
          <h4>🚦 4. Must / Mustn't (Zorunluluk & Yasaklar)</h4>
          <ul>
            <li><strong>Must:</strong> Yapılması zorunlu ve gerekli kurallar için kullanılır: <em>You must follow the school rules.</em></li>
            <li><strong>Mustn't:</strong> Yapılması kesinlikle yasak kurallar için: <em>You mustn't use your phone in the library.</em></li>
          </ul>
        </div>
      </div>
    </div>

    <!-- TAB 2: QUESTIONS -->
    <div id="questions-pane" class="tab-pane">
      
      <!-- S1 -->
      <div class="question-card" id="q_eng_1">
        <div class="q-header">
          <span class="q-badge">Part A • Fred's Timetable</span>
          <span class="q-points">30 Points</span>
        </div>
        <div class="q-text">
          Look at Fred's weekly timetable and answer the 3 questions:<br><br>
          <em>"Hi! I'm Fred. This is my weekly schedule. On Monday: Maths, Maths, PE, Social studies. On Tuesday: History, History, English, English. On Wednesday: Art, Art, Science, Science. On Thursday: Science, Maths, English, PE. On Friday: Turkish, Turkish, Music, ICT."</em><br><br>
          1. How many classes does Fred have in a week?<br>
          2. Which classes does he have on Friday?<br>
          3. When does Fred have English class?
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="1. He has ... classes. 2. He has ... on Friday. 3. He has English on ..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('ingilizce_q1.mp3', 'q_eng_1')">🔊 Listen Question (English)</button>
          <button class="btn-q btn-q-hint" onclick="portalApp.toggleHint('q_eng_1')">💡 Hint</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_eng_1')">✅ Show Official Answer</button>
        </div>
        <div class="hint-box">
          <strong>Hint:</strong> 4 lessons per day × 5 days = 20 lessons total. Look at Friday: Turkish, Music, ICT.
        </div>
        <div class="solution-box">
          <h5>✅ Official Model Answers:</h5>
          <div class="solution-content">
            1. <strong>He has twenty (20) classes in a week.</strong><br>
            2. <strong>He has Turkish, Music and ICT on Friday.</strong><br>
            3. <strong>He has English class on Tuesday and Thursday.</strong>
          </div>
        </div>
        <div class="self-grading">
          <span>Award points:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_eng_1', 30, 30, this)">30 Points</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_eng_1', 30, 15, this)">15 Points</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_eng_1', 30, 0, this)">0 Points</button>
        </div>
      </div>

      <!-- S2 -->
      <div class="question-card" id="q_eng_2">
        <div class="q-header">
          <span class="q-badge">Part B • Telling the Time</span>
          <span class="q-points">20 Points</span>
        </div>
        <div class="q-text">
          Write down the time in words:<br>
          • 1. <strong>11:00</strong> ➔ ...<br>
          • 2. <strong>07:15</strong> ➔ ...<br>
          • 3. <strong>09:45</strong> ➔ ...<br>
          • 4. <strong>07:30</strong> ➔ ...
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="1: It's ... , 2: It's ... , 3: It's ... , 4: It's ..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('ingilizce_q2.mp3', 'q_eng_2')">🔊 Listen Question</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_eng_2')">✅ Show Answers</button>
        </div>
        <div class="solution-box">
          <h5>✅ Official Model Answers:</h5>
          <div class="solution-content">
            1. <strong>It's eleven o'clock.</strong><br>
            2. <strong>It's quarter past seven.</strong><br>
            3. <strong>It's quarter to ten.</strong><br>
            4. <strong>It's half past seven.</strong>
          </div>
        </div>
        <div class="self-grading">
          <span>Award points:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_eng_2', 20, 20, this)">20 Points</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_eng_2', 20, 10, this)">10 Points</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_eng_2', 20, 0, this)">0 Points</button>
        </div>
      </div>

      <!-- S3 -->
      <div class="question-card" id="q_eng_3">
        <div class="q-header">
          <span class="q-badge">Part C • Mia's Daily Routine Reading Text</span>
          <span class="q-points">40 Points</span>
        </div>
        <div class="q-text">
          <em>"Hi, I’m Mia! I’m 12 years old and I go to middle school. I wake up at 6:30 a.m. every morning. First, I brush my teeth and get dressed. Then, I have breakfast with my family at 7:00 a.m. After breakfast, I leave home and walk to school because it’s very close to my house. My school starts at 8:00 a.m. and finishes at 3:00 p.m. After school, I do my homework and read a book for an hour. At 5:00 p.m., I play volleyball with my friends in the park. In the evening, I have dinner with my family at 7:00 p.m., and then we watch TV together. Finally, I go to bed at 9:30 p.m."</em><br><br>
          Answer the questions:<br>
          1. What time does Mia wake up?<br>
          2. Does Mia walk to school?<br>
          3. What does Mia do at 5:00 p.m.?<br>
          4. Does Mia have dinner at 6:00 p.m.?<br>
          5. Who does Mia play volleyball with?
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="1: ... 2: ... 3: ... 4: ... 5: ..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('ingilizce_q3.mp3', 'q_eng_3')">🔊 Listen Story & Questions</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_eng_3')">✅ Show Official Answers</button>
        </div>
        <div class="solution-box">
          <h5>✅ Official Answers:</h5>
          <div class="solution-content">
            1. <strong>She wakes up at 6:30 a.m.</strong><br>
            2. <strong>Yes, she does.</strong> (Because it is close to her house)<br>
            3. <strong>She plays volleyball in the park.</strong><br>
            4. <strong>No, she does not.</strong> (She has dinner at 7:00 p.m.)<br>
            5. <strong>She plays volleyball with her friends.</strong>
          </div>
        </div>
        <div class="self-grading">
          <span>Award points:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_eng_3', 40, 40, this)">40 Points</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_eng_3', 40, 20, this)">20 Points</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_eng_3', 40, 0, this)">0 Points</button>
        </div>
      </div>

      <!-- S4 & S5 -->
      <div class="question-card" id="q_eng_5">
        <div class="q-header">
          <span class="q-badge">Part D & E • Numbers & Must / Mustn't</span>
          <span class="q-points">10 Points</span>
        </div>
        <div class="q-text">
          <strong>Write the numbers in words:</strong><br>
          • 92 = ... | 100 = ... | 65 = ...<br><br>
          <strong>Complete the sentences with must or mustn't:</strong><br>
          1. You ......... follow the rules at school.<br>
          2. You ......... use your mobile phones in the library.<br>
          3. You ......... be kind to your classmates.<br>
          4. You ......... eat or drink in the lab.
        </div>
        <div class="q-interactive-area">
          <textarea class="text-answer-input" placeholder="Numbers: ... Rules: 1: ..., 2: ..., 3: ..., 4: ..."></textarea>
        </div>
        <div class="q-actions">
          <button class="btn-q btn-q-audio" onclick="portalApp.playAudio('ingilizce_q5.mp3', 'q_eng_5')">🔊 Listen Questions</button>
          <button class="btn-q btn-q-solution" onclick="portalApp.toggleSolution('q_eng_5')">✅ Show Answers</button>
        </div>
        <div class="solution-box">
          <h5>✅ Official Answers:</h5>
          <div class="solution-content">
            <strong>Numbers:</strong> 92 = ninety-two, 100 = one hundred, 65 = sixty-five.<br><br>
            <strong>Must / Mustn't:</strong><br>
            1. You <strong>must</strong> follow the rules at school.<br>
            2. You <strong>mustn't</strong> use your mobile phones in the library.<br>
            3. You <strong>must</strong> be kind to your classmates.<br>
            4. You <strong>mustn't</strong> eat or drink in the lab.
          </div>
        </div>
        <div class="self-grading">
          <span>Award points:</span>
          <button class="grade-btn full" onclick="portalApp.gradeQuestion('q_eng_5', 10, 10, this)">10 Points</button>
          <button class="grade-btn half" onclick="portalApp.gradeQuestion('q_eng_5', 10, 5, this)">5 Points</button>
          <button class="grade-btn zero" onclick="portalApp.gradeQuestion('q_eng_5', 10, 0, this)">0 Points</button>
        </div>
      </div>

      <!-- Sınavı Bitir Butonu -->
      <div style="text-align: center; margin: 36px 0;">
        <button class="btn-start" style="padding: 16px 32px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 Finish Exam & Calculate Score
        </button>
      </div>

    </div>

    <!-- TAB 3: ORIGINAL PDF VIEWER -->
    <div id="pdf-pane" class="tab-pane">
      <div style="background: white; border-radius: 12px; padding: 16px; margin-bottom: 20px; border: 1px solid #e2e8f0;">
        <p><strong>📄 5th Grade English 1st Term 1st Exam Original Sheets</strong></p>
        <p style="font-size: 0.88rem; color: #64748b;">AV Yayınları 5. Sınıf İngilizce Çalışma Fasikülü (7 Pages)</p>
      </div>

      <div class="pdf-pages-grid">
        <div class="pdf-page-card">
          <div class="page-head"><span>Page 1 (Study Topics)</span><span>Grammar</span></div>
          <img src="assets/img/ingilizce_p1.png" alt="English Page 1" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Page 2 (Articles & Present Simple)</span><span>Grammar</span></div>
          <img src="assets/img/ingilizce_p2.png" alt="English Page 2" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Page 3 (Telling the Time)</span><span>Grammar</span></div>
          <img src="assets/img/ingilizce_p3.png" alt="English Page 3" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Page 4 (Questions Part A & B)</span><span>Exam</span></div>
          <img src="assets/img/ingilizce_p4.png" alt="English Page 4" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Page 5 (Questions Part C, D, E)</span><span>Exam</span></div>
          <img src="assets/img/ingilizce_p5.png" alt="English Page 5" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Page 6 (Answer Key Part A & B)</span><span>Key</span></div>
          <img src="assets/img/ingilizce_p6.png" alt="English Page 6" loading="lazy">
        </div>
        <div class="pdf-page-card">
          <div class="page-head"><span>Page 7 (Answer Key Part C, D, E)</span><span>Key</span></div>
          <img src="assets/img/ingilizce_p7.png" alt="English Page 7" loading="lazy">
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
</html>"""
    return html

with open(os.path.join(OUTPUT_DIR, "ingilizce.html"), "w", encoding="utf-8") as f:
    f.write(build_ingilizce())
print("ingilizce.html created.")
