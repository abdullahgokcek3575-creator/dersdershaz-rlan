import sys, os
sys.stdout.reconfigure(encoding='utf-8')
import pdfplumber

folder = r'C:\Users\User\Downloads\2026-2027\5'

pdfs = {
    'turkce': '5.sınıf Türkçe 1.Dönem 1.Yazılı.pdf',
    'matematik': '5.Sınıf Matematik  1.dönem 1.yazılı.pdf',
    'fen': '5.Sınıf Fen Bilimleri 1.Dönem 1.Yazılı.pdf',
    'sosyal': '5.sınıf 1.dönem 1. yazılı sosyal bilgiler.pdf',
    'din': 'AV Yayınları Din kültürü 5. sınıf.pdf',
    'ingilizce': 'AV Yayınları İngilizce 5. sınıf.pdf',
}

for key, fname in pdfs.items():
    p = os.path.join(folder, fname)
    print(f'=== {key} ===')
    with pdfplumber.open(p) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text() or ''
            lines = [l.strip() for l in text.split('\n') if l.strip()]
            print(f'  Page {i+1} ({len(lines)} lines):')
            for l in lines[:20]:
                print(f'    {l}')
            if len(lines) > 20:
                print(f'    ... ({len(lines)-20} more lines)')
    print()
