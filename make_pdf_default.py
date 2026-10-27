import os

files = ['turkce.html', 'matematik.html', 'fen-bilimleri.html', 'sosyal-bilgiler.html', 'din-kulturu.html', 'ingilizce.html']
folder = r'd:\gpt\5_sinif_calisma_portali'

for fname in files:
    path = os.path.join(folder, fname)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Make PDF the first active tab
    html = html.replace('class="tab-btn active" data-tab="summary-pane"', 'class="tab-btn" data-tab="summary-pane"')
    html = html.replace('class="tab-btn" data-tab="pdf-pane"', 'class="tab-btn active" data-tab="pdf-pane"')
    html = html.replace('id="summary-pane" class="tab-pane active"', 'id="summary-pane" class="tab-pane"')
    html = html.replace('id="pdf-pane" class="tab-pane"', 'id="pdf-pane" class="tab-pane active"')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {fname}")
