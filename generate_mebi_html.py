# -*- coding: utf-8 -*-
"""
Generate 7th Grade MEBİ Subject Showcase Page:
Displays all 6 MEBİ Exam Papers (Türkçe, Matematik, Fen, Sosyal, Din, İngilizce)
with direct page viewing, questions, and official solutions.
"""

from generate_mat_fen import get_header, get_footer, get_score_modal

def generate_mebi_page():
    subjects = [
        ("turkce_mebi", "Türkçe (MEBİ)", "9 Sayfa", "Hürkuş, İkilemeler, Yazım Kuralları, Şerife Bacı, Forsa Metni"),
        ("matematik_mebi", "Matematik (MEBİ)", "28 Sayfa", "Tam Sayılar, Rasyonel Sayılar, Sayı Doğrusu, İşlem Önceliği"),
        ("fen_mebi", "Fen Bilimleri (MEBİ)", "11 Sayfa", "Uzay Teknolojileri, Yıldızların Yaşamı, Fiziksel İş ve Enerji"),
        ("sosyal_mebi", "Sosyal Bilgiler (MEBİ)", "4 Sayfa", "Empati ve İletişim, Ben Dili, Milli Mücadele, Küreselleşme"),
        ("din_mebi", "Din Kültürü (MEBİ)", "8 Sayfa", "Melek ve Ahiret İnancı, Varlıklar Alemi, Ahlaki Tutumlar"),
        ("ingilizce_mebi", "İngilizce (MEBİ)", "6 Sayfa", "Appearances and Personalities, Sports, Routines and Comparisons"),
    ]

    cards_html = ""
    for folder_key, title, page_cnt, desc in subjects:
        cards_html += f"""
        <div class="subject-card theme-{folder_key.split('_')[0]}">
          <div class="card-top">
            <span class="card-badge" style="background:#e0e7ff; color:#3730a3; font-weight:800;">7. SINIF MEBİ</span>
            <span style="font-size:0.82rem; font-weight:700; color:#64748b;">{page_cnt}</span>
          </div>
          <h3 style="margin-top:10px;">{title}</h3>
          <p style="font-size:0.9rem; color:#475569; margin:10px 0 16px;">{desc}</p>
          <button class="btn-start" onclick="showMebiSubject('{folder_key}', '{title}')">
            📖 Sınavı & Çözümleri Aç ➔
          </button>
        </div>
        """

    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>7. Sınıf MEBİ Yazılıya Hazırlık Soruları & Çözümleri</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    .mebi-viewer-modal {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(6px);
      z-index: 1000;
      padding: 20px;
      overflow-y: auto;
    }}
    .mebi-viewer-modal.show {{ display: block; }}
    .mebi-viewer-content {{
      background: white;
      border-radius: 20px;
      max-width: 1000px;
      margin: 20px auto;
      padding: 24px;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    }}
  </style>
</head>
<body>
  {get_header('mebi')}

  <main class="container">
    <section class="hero" style="background: linear-gradient(135deg, #0f766e 0%, #0d9488 50%, #14b8a6 100%);">
      <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(255,255,255,0.22); padding: 6px 14px; border-radius: 20px; font-size: 0.88rem; font-weight: 700; margin-bottom: 14px;">
        <span>⭐</span> MEBİ ÖRNEK SORULAR VE RESMİ ÇÖZÜMLER
      </div>
      <h1>7. Sınıf 1. Dönem 1. Yazılıya Hazırlık Kitapçıkları</h1>
      <p>Yüklediğiniz tüm MEBİ PDF'leri (Türkçe, Matematik, Fen, Sosyal, Din, İngilizce) sisteme yüksek çözünürlükle entegre edildi. Soru soru inceleyebilir ve öğretmen model cevaplarını görebilirsiniz.</p>
    </section>

    <h2 style="font-size: 1.5rem; margin-bottom: 24px; color: #0f172a; font-weight: 800;">
      📚 Ders Seçimi Yaparak MEBİ Sorularını İncele
    </h2>

    <div class="subject-grid">
      {cards_html}
    </div>

    <!-- Viewer Modal -->
    <div id="mebiModal" class="mebi-viewer-modal">
      <div class="mebi-viewer-content">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #e2e8f0; padding-bottom:14px; margin-bottom:20px;">
          <h2 id="mebiModalTitle" style="font-size:1.4rem; color:#0f172a;">MEBİ Sınav Kitapçığı</h2>
          <button onclick="closeMebiModal()" style="background:#ef4444; color:white; border:none; padding:8px 16px; border-radius:8px; font-weight:700; cursor:pointer;">✕ Kapat</button>
        </div>
        <div id="mebiPagesContainer" style="display:flex; flex-direction:column; gap:24px;"></div>
      </div>
    </div>

  </main>

  {get_footer()}

  <script src="assets/js/app.js"></script>
  <script>
    const mebiCounts = {{
      'turkce_mebi': 9,
      'matematik_mebi': 28,
      'fen_mebi': 11,
      'sosyal_mebi': 4,
      'din_mebi': 8,
      'ingilizce_mebi': 6
    }};

    function showMebiSubject(key, title) {{
      document.getElementById('mebiModalTitle').textContent = title + ' - Soru & Çözüm Sayfaları';
      const container = document.getElementById('mebiPagesContainer');
      container.innerHTML = '';
      
      const count = mebiCounts[key] || 4;
      for (let i = 1; i <= count; i++) {{
        const pageDiv = document.createElement('div');
        pageDiv.style.cssText = 'background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; overflow:hidden; box-shadow:0 4px 12px rgba(0,0,0,0.05);';
        
        const header = document.createElement('div');
        header.style.cssText = 'background:#1e293b; color:white; padding:10px 16px; font-weight:700; font-size:0.9rem; display:flex; justify-content:space-between;';
        header.innerHTML = '<span>📄 Sayfa ' + i + ' / ' + count + '</span><span>MEBİ 1. Dönem 1. Yazılı</span>';
        
        const img = document.createElement('img');
        img.src = 'assets/pdf_pages/' + key + '/page_' + i + '.png';
        img.alt = title + ' Sayfa ' + i;
        img.style.cssText = 'width:100%; height:auto; display:block;';
        img.loading = i <= 2 ? 'eager' : 'lazy';

        pageDiv.appendChild(header);
        pageDiv.appendChild(img);
        container.appendChild(pageDiv);
      }}

      document.getElementById('mebiModal').classList.add('show');
    }}

    function closeMebiModal() {{
      document.getElementById('mebiModal').classList.remove('show');
    }}
  </script>
</body>
</html>
"""

with open(r'd:\gpt\5_sinif_calisma_portali\mebi-sorulari.html', 'w', encoding='utf-8') as f:
    f.write(generate_mebi_page())

print("mebi-sorulari.html created successfully!")
