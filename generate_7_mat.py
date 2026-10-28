# -*- coding: utf-8 -*-
"""
Generate 7th Grade MEBİ Mathematics with all 22 questions fully solved.
"""

import os
from generate_7_part1 import get_header, get_footer, get_score_modal, build_q_strip

def generate_7_matematik():
    # 22 Questions
    q1 = build_q_strip(1, "Kutup Hayvanları Sıcaklık Aralıkları Tablosu", 5, "mat7_q1.mp3", "mat7_sol1.mp3",
        "Soru 1. Tablodaki sıcaklıkların hangi hayvanların yaşadığı aralıklarda olduğunu belirleyiniz.",
        "Soru 1 çözümü. -45 kutup tilkisi. -30 her üçü. -10 her üçü. 0 her üçü. 7 kutup tavşanı ve ren geyiği. 12 sadece ren geyiği.",
        "• <strong>-45 °C:</strong> Sadece <strong>Kutup Tilkisi</strong> (-50 ile +5 arası)<br>• <strong>-30 °C:</strong> <strong>Kutup Tavşanı ✓, Kutup Tilkisi ✓, Ren Geyiği ✓</strong> (Üçünde de var)<br>• <strong>-10 °C:</strong> <strong>Kutup Tavşanı ✓, Kutup Tilkisi ✓, Ren Geyiği ✓</strong><br>• <strong>0 °C:</strong> <strong>Kutup Tavşanı ✓, Kutup Tilkisi ✓, Ren Geyiği ✓</strong><br>• <strong>7 °C:</strong> <strong>Kutup Tavşanı ✓, Ren Geyiği ✓</strong> (Kutup tilkisi en fazla +5 °C)<br>• <strong>12 °C:</strong> Sadece <strong>Ren Geyiği ✓</strong> (-35 ile +15 arası)",
        "-45: Kutup tilkisi...\n-30: Üçü de...")

    q2 = build_q_strip(2, "Gerçek Yaşam Durumlarını Tam Sayılarla İfade Etme", 5, "mat7_q2.mp3", "mat7_sol2.mp3",
        "Soru 2. Ağrı Dağı, Mariana Çukuru, Erzurum kış sıcaklığı ve Çamlıca Kulesi değerlerini tam sayıyla gösteriniz.",
        "Soru 2 çözümü. Ağrı dağı artı 5137. Mariana çukuru eksi 10935. Erzurum eksi 25. Çamlıca kulesi artı 369.",
        "• Ağrı Dağı zirvesi (deniz seviyesinin 5137 m üzeri): <strong>+5137</strong><br>• Mariana Çukuru (deniz seviyesinin 10.935 m altı): <strong>-10 935</strong><br>• Erzurum sıfırın altında 25 °C: <strong>-25</strong><br>• Çamlıca Kulesi zeminden 369 m yükseklik: <strong>+369</strong>",
        "+5137, -10935, -25, +369...")

    q3 = build_q_strip(3, "Devirli Ondalık Sayıyı Rasyonele Çevirme", 5, "mat7_q3.mp3", "mat7_sol3.mp3",
        "Soru 3. 1,23 devirli sayısında bölünen ve bölen doğal sayıların toplamı en az kaçtır?",
        "Soru 3 çözümü. Sayı 123 eksi 12 bölü 90 eşittir 111 bölü 90. 3 ile sadeleştirirsek 37 bölü 30. Toplam en az 37 artı 30 eşittir 67.",
        "<strong>İşlemler:</strong><br>1,23̄ = (123 - 12) ÷ 90 = <strong>111 / 90</strong><br>En sade hâli için pay ve payda 3 ile sadeleştirilir:<br>111 ÷ 3 = <strong>37</strong> (Bölünen en az)<br>90 ÷ 3 = <strong>30</strong> (Bölen en az)<br><strong>Toplam: 37 + 30 = 67</strong>",
        "1,23̄ = 111/90 = 37/30 → 37 + 30 = 67")

    q4 = build_q_strip(4, "Hedef Kütle ve Hata Miktarı (Mutlak Değer)", 5, "mat7_q4.mp3", "mat7_sol4.mp3",
        "Soru 4. Çay fabrikasında hedef kütleyi bulunuz, tabloyu doldurunuz ve hata miktarı en az olan makineleri belirleyiniz.",
        "Soru 4 çözümü. a: Hedef kütle 496 artı 4 eşittir 500 gram. b: Hatalar sırasıyla 4, 2, 1, 7, 1 gram. c: Hata miktarı en az olan 3. ve 5. makinelerdir, hata 1 gramdır.",
        "<strong>a) Hedef Kütle:</strong> 496 + 4 = <strong>500 g</strong><br><br><strong>b) Hata Miktarları:</strong><br>• 2. Makine (502 g): 2 g fazla → |+2| = <strong>2</strong><br>• 3. Makine (499 g): 1 g eksik → |-1| = <strong>1</strong><br>• 4. Makine (493 g): 7 g eksik → |-7| = <strong>7</strong><br>• 5. Makine (501 g): 1 g fazla → |+1| = <strong>1</strong><br><br><strong>c) En Az Hata:</strong> <strong>3. ve 5. makinelerdir</strong> (Hata miktarı 1 gramdır).",
        "a) 500 g, b) Hatalar: 2, 1, 7, 1, c) 3 ve 5. makineler...")

    q5 = build_q_strip(5, "Sonlu ve Devirli Ondalık Gösterim Kriteri", 5, "mat7_q5.mp3", "mat7_sol5.mp3",
        "Soru 5. Rasyonel sayıların en sade hâllerinin paydalarını inceleyerek ondalık gösterimlerinin sonlu mu devirli mi olduğunu açıklayınız.",
        "Soru 5 çözümü. Paydada 2 ve 5 dışında asal çarpan yoksa sonlu, varsa devirlidir. 7/20 sonlu. -11/18 devirli. 15/24 yani 5/8 sonlu. 9/35 devirlidir.",
        "• <strong>7/20:</strong> Payda 20 = 2² × 5 (sadece 2 ve 5 var) → <strong>SONLU</strong> (0,35)<br>• <strong>-11/18:</strong> Payda 18 = 2 × 3² (3 çarpanı var) → <strong>DEVİRLİ</strong><br>• <strong>15/24:</strong> Sadeleşince 5/8 olur. Payda 8 = 2³ → <strong>SONLU</strong> (0,625)<br>• <strong>9/35:</strong> Payda 35 = 5 × 7 (7 çarpanı var) → <strong>DEVİRLİ</strong>",
        "7/20 sonlu, -11/18 devirli, 15/24 sonlu, 9/35 devirli...")

    q6 = build_q_strip(6, "Doğal, Tam ve Rasyonel Sayı Sınıflandırma", 5, "mat7_q6.mp3", "mat7_sol6.mp3",
        "Soru 6. Verilen sayıların doğal, tam veya rasyonel sayı olup olmadığını işaretleyiniz.",
        "Soru 6 çözümü. 21/4 sadece rasyonel. -5 tam ve rasyonel. -1,8 sadece rasyonel. 12/4 yani 3 doğal, tam, rasyonel. 0/9 yani 0 doğal, tam, rasyonel. -7/7 yani -1 tam ve rasyonel. 3/0 tanımsızdır.",
        "• <strong>21/4:</strong> Rasyonel sayı ✓<br>• <strong>-5:</strong> Tam sayı ✓, Rasyonel sayı ✓<br>• <strong>-1,8:</strong> Rasyonel sayı ✓<br>• <strong>12/4 (= 3):</strong> Doğal sayı ✓, Tam sayı ✓, Rasyonel sayı ✓<br>• <strong>0/9 (= 0):</strong> Doğal sayı ✓, Tam sayı ✓, Rasyonel sayı ✓<br>• <strong>-7/7 (= -1):</strong> Tam sayı ✓, Rasyonel sayı ✓<br>• <strong>3/0:</strong> Paydası 0 olduğu için <strong>TANIMSIZDIR</strong> (Hiçbir kutucuk işaretlenmez).",
        "Doğal sayılar: 12/4, 0/9. Tam sayılar: -5, 12/4, 0/9, -7/7...")

    q7 = build_q_strip(7, "? / 35 Kesrinin Sonlu Ondalık Olma Şartı", 5, "mat7_q7.mp3", "mat7_sol7.mp3",
        "Soru 7. ? / 35 rasyonel sayısının sonlu olması için soru işareti yerine yazılabilecek sayıların ortak özelliği nedir?",
        "Soru 7 çözümü. 35 eşittir 5 çarpı 7dir. Sonlu olması için paydadaki 7 asal çarpanının sadeleşmesi gerekir. Bu yüzden soru işareti 7nin katı olan bir tam sayı olmalıdır.",
        "<strong>Çözüm:</strong><br>35 = 5 × 7'dir. Sonlu ondalık gösterim için paydada yalnızca 2 ve 5 çarpanları kalmalıdır. Paydadaki 7 çarpanını sadeleştirmek için <strong>? yerine 7'nin katı olan tam sayılar yazılmalıdır</strong> (Örn: 7, 14, 21, -7 vb.).",
        "? yerine 7'nin katı olan sayılar gelmelidir...")

    q8 = build_q_strip(8, "Sayı Doğrusunda A Noktası ve Denk Kesirler", 5, "mat7_q8.mp3", "mat7_sol8.mp3",
        "Soru 8. Sayı doğrusundaki A noktasını Kerem, Zeynep ve Arda bulmuştur. Hangileri doğrudur?",
        "Soru 8 çözümü. Üç öğrenci de doğrudur. Kerem eksi 1 tam 3 bölü 4 eşittir eksi 7 bölü 4. Zeynep eksi 14 bölü 8 sadeleşince eksi 7 bölü 4. Arda eksi 21 bölü 12 sadeleşince eksi 7 bölü 4 bulmuştur.",
        "<strong>Öğrencilerin Tamamı Doğrudur!</strong><br>A noktası: -1 ile -2 arası 4 parçaya bölünmüş, 3. parçada → <strong>-1 tam 3/4 = -7/4</strong>'tür.<br>• Kerem: <strong>-1 tam 3/4 = -7/4</strong> ✓<br>• Zeynep: <strong>-14/8</strong> (2 ile sadeleşirse -7/4) ✓<br>• Arda: <strong>-21/12</strong> (3 ile sadeleşirse -7/4) ✓",
        "Kerem, Zeynep ve Arda'nın üçü de doğrudur...")

    q9 = build_q_strip(9, "Mutlak Değeri 11 Olan Sayılar Arası Mesafe", 5, "mat7_q9.mp3", "mat7_sol9.mp3",
        "Soru 9. Mutlak değeri 11 olan tam sayıları yazınız ve aralarındaki uzaklığı bulunuz.",
        "Soru 9 çözümü. a: -11 ve +11. b: Uzaklık 11 artı 11 eşittir 22 birimdir.",
        "<strong>a) Tam Sayılar:</strong> <strong>-11 ve +11</strong> (|-11| = 11, |+11| = 11)<br><br><strong>b) Aralarındaki Uzaklık:</strong><br>|+11 - (-11)| = 11 + 11 = <strong>22 birim</strong>dir.",
        "a) -11 ve +11, b) 11 + 11 = 22 birim...")

    q10 = build_q_strip(10, "Negatif Rasyonel Sayılarda Sıralama Hatası", 5, "mat7_q10.mp3", "mat7_sol10.mp3",
        "Soru 10. Efe'nin sıralamasında ilk hata hangi adımdadır ve doğru sıralama nedir?",
        "Soru 10 çözümü. Efe ilk hatayı 3. adımda yapmıştır. Negatif sayılarda payı büyük olan daha küçüktür. Doğru sıralama eksi 7 bölü 3 küçüktür eksi 5 bölü 6 küçüktür eksi 2 bölü 3 küçüktür 1 bölü 2.",
        "• <strong>İlk Hata:</strong> <strong>3. Adımda</strong> yapılmıştır.<br>Paydaları eşit (6) olan negatif sayılarda payı küçük olan sayı sıfıra daha yakın olduğu için daha büyüktür. Efe pozitif gibi sıralamıştır.<br><br>• <strong>Doğru Sıralama:</strong><br><strong>-7/3 < -5/6 < -2/3 < 1/2</strong> (-14/6 < -5/6 < -4/6 < 3/6)",
        "İlk hata: 3. adımda. Doğru sıralama: -7/3 < -5/6 < -2/3 < 1/2...")

    q11 = build_q_strip(11, "Bileşik Kesirlerde Negatif Sıralama", 5, "mat7_q11.mp3", "mat7_sol11.mp3",
        "Soru 11. Tahtadaki -45/44, -39/38, -50/49 sayılarını öğrencinin sıralaması doğru mudur?",
        "Soru 11 çözümü. Öğrencinin sıralaması yanlıştır. Tam kısımları -1 tamdır. Payları eşit pozitif kesirlerde paydası küçük olan büyüktür. Negatifte ise mutlak değeri büyük olan küçüktür. Doğru sıralama -39/38 küçüktür -45/44 küçüktür -50/49.",
        "<strong>Öğrencinin Sıralaması YANLIŞTIR!</strong><br>Tam sayılı kesre çevirirsek: -1 tam 1/44, -1 tam 1/38, -1 tam 1/49.<br>Pozitifte 1/38 > 1/44 > 1/49'dur.<br>Negatif sayılarda mutlak değeri büyük olan daha küçük olduğundan doğru sıralama:<br><strong>-39/38 < -45/44 < -50/49</strong>",
        "Yanlıştır. Doğru sıralama: -39/38 < -45/44 < -50/49...")

    q12 = build_q_strip(12, "Gerçek Yaşam Durumları Sayı Cümlesi", 5, "mat7_q12.mp3", "mat7_sol12.mp3",
        "Soru 12. Arşimet ve Harizmi, yarışma puanı, banka borcu ve metro basımı sayı cümleleri ve sonuçları.",
        "Soru 12 çözümü. 1 Arşimet Harizmi: +780 eksi -287 eşittir 1067 yıl. 2 Yarışma: -104 bölü -8 eşittir 13 soru. 3 Banka: -1000 artı 1500 eşittir +500 TL. 4 Metro: +4 çarpı -12 eşittir -48 TL.",
        "• <strong>Arşimet - Harizmi:</strong> (+780) - (-287) = 780 + 287 = <strong>+1067 yıl</strong><br>• <strong>Yarışma Soruları:</strong> (-104) ÷ (-8) = <strong>+13 soru</strong><br>• <strong>Banka Bakiyesi:</strong> (-1000) + (+1500) = <strong>+500 TL</strong><br>• <strong>Metro Bakiyesi Değişimi:</strong> (+4) × (-12) = <strong>-48 TL</strong>",
        "1: 1067, 2: 13, 3: +500 TL, 4: -48 TL...")

    q13 = build_q_strip(13, "Mauna Kea Dağı Taban-Zirve Yüksekliği", 5, "mat7_q13.mp3", "mat7_sol13.mp3",
        "Soru 13. Zirvesi +4207 metrede, tabanı -6000 metrede olan Mauna Kea dağının toplam yüksekliği kaç metredir?",
        "Soru 13 çözümü. (+4207) eksi (-6000) eşittir 4207 artı 6000 eşittir 10207 metredir.",
        "<strong>İşlem:</strong><br>(+4207) - (-6000) = 4207 + 6000 = <strong>10 207 metre</strong>",
        "4207 - (-6000) = 10207 metre...")

    q14 = build_q_strip(14, "Soğuk Hava Deposu Süre Problemi", 5, "mat7_q14.mp3", "mat7_sol14.mp3",
        "Soru 14. +14 dereceden -4 dereceye dakikada 3 derece düşen sistem kaç dakikada hedefe ulaşır?",
        "Soru 14 çözümü. Sıcaklık değişimi (-4) eksi (+14) eşittir -18 derece. Dakikada 3 derece düştüğü için -18 bölü -3 eşittir 6 dakika.",
        "<strong>İşlemler:</strong><br>Toplam Sıcaklık Değişimi: (-4) - (+14) = <strong>-18 °C</strong><br>Dakikalık Düşüş: -3 °C<br>Geçen Süre: (-18) ÷ (-3) = <strong>6 dakika</strong>",
        "-4 - 14 = -18 → -18 / -3 = 6 dakika...")

    q15 = build_q_strip(15, "Rukiye'nin Sınav Puanı Hesabı", 5, "mat7_q15.mp3", "mat7_sol15.mp3",
        "Soru 15. Rukiye 4 doğru, 4 yanlış ve 2 boş ile sınavdan kaç puan almıştır?",
        "Soru 15 çözümü. Doğrulardan 4 çarpı 10 eşittir 40 puan. Yanlışlardan 4 çarpı -5 eşittir -20 puan. Toplam 40 eksi 20 eşittir 20 puan almıştır.",
        "• Doğru Cevaplar (2, 4, 5, 6): 4 × (+10) = <strong>+40 puan</strong><br>• Yanlış Cevaplar (1, 3, 7, 10): 4 × (-5) = <strong>-20 puan</strong><br>• Boş Bırakılanlar (8, 9): 2 × 0 = <strong>0 puan</strong><br><strong>Toplam Puan: 40 + (-20) = 20 puan</strong>",
        "4x10 = 40, 4x(-5) = -20 → 40 - 20 = 20 puan...")

    q16 = build_q_strip(16, "Kalemin Cetvelle Ölçümü ve Kalan Boy", 5, "mat7_q16.mp3", "mat7_sol16.mp3",
        "Soru 16. Kalemin boyu 6,5 cm olup 2 tam 1/4 cm kısalırsa kalan boy 4 cm'den uzun mudur?",
        "Soru 16 çözümü. 6,5 cm yani 13/2 cm. 2 tam 1/4 cm yani 9/4 cm. 26/4 eksi 9/4 eşittir 17/4 cm yani 4,25 cm. 4,25 cm 4 cmden büyük olduğu için kalem kullanılabilir.",
        "<strong>İşlemler:</strong><br>İlk Boy: 6,5 cm = 6 tam 1/2 = <strong>13/2 = 26/4 cm</strong><br>Kısalan Kısım: 2 tam 1/4 = <strong>9/4 cm</strong><br>Kalan Boy: 26/4 - 9/4 = <strong>17/4 cm = 4,25 cm</strong><br>4,25 cm > 4 cm olduğundan <strong>KALEM KULLANILABİLİR DURUMDADIR ✓</strong>",
        "6,5 - 2,25 = 4,25 cm > 4 cm → Kullanılabilir...")

    q17 = build_q_strip(17, "Robotun Hareketi ve Toplama Özellikleri", 5, "mat7_q17.mp3", "mat7_sol17.mp3",
        "Soru 17. Robotun hareketlerinde rasyonel sayılarda ters eleman özelliğini kullanarak son konumunu bulunuz.",
        "Soru 17 çözümü. -3/4 ile +3/4 birbirinin toplama işlemine göre tersidir, toplamları 0 olur. Geriye +2/5 kalır. Robot başlangıç noktasının 2/5 metre ilerisindedir.",
        "<strong>İşlem Özellikleri:</strong><br>İşlem: [(-3/4) + (+2/5)] + (+3/4)<br>1. <strong>Değişme ve Birleşme Özelliği:</strong> (+2/5) + [(-3/4) + (+3/4)]<br>2. <strong>Ters Eleman Özelliği:</strong> (-3/4) + (+3/4) = <strong>0</strong><br>3. <strong>Etkisiz Eleman:</strong> (+2/5) + 0 = <strong>+2/5 metre</strong><br><strong>Sonuç: Robot başlangıç noktasının 2/5 m ilerisindedir.</strong>",
        "Ters elemanla -3/4 + 3/4 = 0 olur, sonuç +2/5 m ileridedir...")

    q18 = build_q_strip(18, "Kartların Arka Yüzündeki Sayıların Çarpımı", 5, "mat7_q18.mp3", "mat7_sol18.mp3",
        "Soru 18. Çarpmaya göre tersi olan 5 sayının çarpımını işlem özellikleriyle bulunuz.",
        "Soru 18 çözümü. Arka yüzdeki sayılar: -3/2, 5/4, -2/3, 4/5, -1/7. Birbirini 1 yapanlar çarpılırsa 1 çarpı 1 çarpı -1/7 eşittir -1/7.",
        "• Arka Yüzdeki Sayılar: <strong>-3/2, 5/4, -2/3, 4/5, -1/7</strong><br>• Değişme ve Birleşme ile Gruplama:<br>[(-3/2) × (-2/3)] × [(5/4) × (4/5)] × (-1/7)<br>• Ters Eleman ile Çarpımlar 1 olur:<br>1 × 1 × (-1/7) = <strong>-1/7</strong>",
        "Ters elemanlar çarpımı 1 yapar: 1 x 1 x (-1/7) = -1/7...")

    q19 = build_q_strip(19, "Negatif Sayıların Kuvvetleri ve (-3)^18", 5, "mat7_q19.mp3", "mat7_sol19.mp3",
        "Soru 19. (-3)^18 ifadesinin pozitif mi negatif mi olduğunu açıklayınız.",
        "Soru 19 çözümü. Negatif tam sayıların çift kuvvetleri pozitif, tek kuvvetleri negatiftir. 18 bir çift sayı olduğu için sonuç pozitiftir.",
        "<strong>Kural:</strong> Negatif sayıların çift kuvvetleri pozitif, tek kuvvetleri negatif olur.<br>(-3)¹⁸ ifadesinde 18 <strong>çift bir sayı</strong> olduğundan sonuç <strong>POZİTİFTİR (+)</strong>.",
        "18 çift sayı olduğu için sonuç pozitiftir (+)...")

    q20 = build_q_strip(20, "Ekmek Dilimleme Problemi", 5, "mat7_q20.mp3", "mat7_sol20.mp3",
        "Soru 20. 18 tam 3/4 cm ekmek 6 eş dilime ayrılırsa bir dilimin kalınlığı kaç cm olur?",
        "Soru 20 çözümü. 18 tam 3/4 eşittir 75/4. 6ya bölersek 75/4 çarpı 1/6 eşittir 75/24, 3 ile sadeleşirse 25/8 yani 3 tam 1/8 cm.",
        "<strong>İşlemler:</strong><br>18 tam 3/4 = <strong>75/4 cm</strong><br>75/4 ÷ 6 = (75/4) × (1/6) = 75/24<br>3 ile sadeleştirirsek: <strong>25/8 = 3 tam 1/8 cm (veya 3,125 cm)</strong>",
        "75/4 / 6 = 25/8 = 3 tam 1/8 cm...")

    q21 = build_q_strip(21, "İşlem Önceliği: Deniz mi Mert mi Haklı?", 5, "mat7_q21.mp3", "mat7_sol21.mp3",
        "Soru 21. 3 - 1/4 + 2/3 işleminde öncelik toplama mı çıkarmada mıdır ve işlemin sonucu kaçtır?",
        "Soru 21 çözümü. Mert haklıdır. Toplama ve çıkarma aynı önceliktedir, soldan sağa işlem yapılır. Önce çıkarma sonra toplama yapılır. Sonuç 41/12 yani 3 tam 5/12.",
        "• <strong>Mert Haklıdır!</strong> Toplama ve çıkarma aynı öncelik düzeyindedir. Aynı öncelikte işlemler <strong>soldan sağa</strong> sırayla yapılır (önce çıkarma, sonra toplama).<br><br>• <strong>İşlem Sonucu:</strong><br>3 - 1/4 = 12/4 - 1/4 = <strong>11/4</strong><br>11/4 + 2/3 = 33/12 + 8/12 = <strong>41/12 = 3 tam 5/12</strong>",
        "Mert haklıdır (soldan sağa). 3 - 1/4 + 2/3 = 41/12...")

    q22 = build_q_strip(22, "Çok Adımlı Rasyonel İşlemler", 5, "mat7_q22.mp3", "mat7_sol22.mp3",
        "Soru 22. a, b, c şıklarındaki çok adımlı merdivenli işlemlerin sonuçlarını bulunuz.",
        "Soru 22 çözümü. a: 0,9 devirli 1dir. 1 bölü (1 artı 3/4) eşittir 4/7. b: (1/2 eksi 1/3) bölü 3 eşittir 1/18. c: (2/3 bölü 4) eksi (2 bölü 3/4) eşittir 1/6 eksi 8/3 eşittir -15/6 yani -5/2.",
        "• <strong>a)</strong> 0,9̄ = 1'dir. Payda: 1 + 3/4 = 7/4. Sonuç: 1 ÷ (7/4) = <strong>4/7</strong><br><br>• <strong>b)</strong> Pay: 1/2 - 1/3 = 3/6 - 2/6 = 1/6. Sonuç: (1/6) ÷ 3 = <strong>1/18</strong><br><br>• <strong>c)</strong> Birinci bölme: (2/3) ÷ 4 = 2/12 = 1/6.<br>İkinci bölme: 2 ÷ (3/4) = 8/3 = 16/6.<br>Fark: 1/6 - 16/6 = -15/6 = <strong>-5/2 = -2 tam 1/2</strong>",
        "a) 4/7, b) 1/18, c) -5/2...")

    all_q_controls_p1 = f"{q1}<hr style='margin:14px 0;'>{q2}<hr style='margin:14px 0;'>{q3}"
    all_q_controls_p2 = f"{q4}<hr style='margin:14px 0;'>{q5}<hr style='margin:14px 0;'>{q6}"
    all_q_controls_p3 = f"{q7}<hr style='margin:14px 0;'>{q8}<hr style='margin:14px 0;'>{q9}"
    all_q_controls_p4 = f"{q10}<hr style='margin:14px 0;'>{q11}"
    all_q_controls_p5 = f"{q12}<hr style='margin:14px 0;'>{q13}<hr style='margin:14px 0;'>{q14}"
    all_q_controls_p6 = f"{q15}<hr style='margin:14px 0;'>{q16}"
    all_q_controls_p7 = f"{q17}<hr style='margin:14px 0;'>{q18}"
    all_q_controls_p8 = f"{q19}<hr style='margin:14px 0;'>{q20}<hr style='margin:14px 0;'>{q21}<hr style='margin:14px 0;'>{q22}"

    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>7. Sınıf Matematik 1. Dönem 1. Yazılı - MEBİ Soruları ve Çözümleri</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body class="theme-mat">
  {get_header('mat7')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>📐</span> 7. Sınıf Matematik 1. Dönem 1. Yazılı (MEBİ)</h1>
        <p>Tam Sayılar • Rasyonel Sayılar • Çok Adımlı İşlemler • 22 Sorunun Tamamı İnteraktif Çözümlü</p>
      </div>
      <div class="score-box">
        <div class="score-val" id="currentScoreVal">0</div>
        <div class="score-lbl">Mevcut Puan / 110</div>
      </div>
    </div>

    <!-- Audio Player Bar -->
    <div class="audio-bar">
      <div class="audio-bar-info">
        <div class="audio-icon-pulse">🔊</div>
        <div>
          <strong style="display:block; font-size:0.95rem;">Matematik MEBİ Sesli Rehber</strong>
          <span id="audioStatusText" style="font-size:0.8rem; color:#94a3b8;">Hazır — Dinlemek için ses butonlarına tıklayın</span>
        </div>
      </div>
      <div class="audio-controls">
        <button class="btn-audio" onclick="portalApp.pauseSpeech()">⏸️ Duraklat / Devam Et</button>
        <button class="btn-audio" onclick="portalApp.stopSpeech()">⏹️ Durdur</button>
        <button class="btn-audio primary" onclick="portalApp.speakText('7. Sınıf Matematik 1. Dönem 1. Yazılı MEBİ Konu Özeti. Tam sayılarla işlemler ve mutlak değer, devirli ondalık sayıları rasyonele çevirme, rasyonel sayılarda sıralama ve işlemler, üslü ifadeler ve çok adımlı merdivenli işlemler sınavın temel konularıdır.')">📢 Sınav Konu Özetini Dinle</button>
      </div>
    </div>

    <!-- Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="pdf-pane">📄 Orijinal MEBİ PDF'i Üzerinde 22 Soruyu Çöz</button>
      <button class="tab-btn" data-tab="answer-key-pane">🔑 Resmi Çözümler (Sayfa 17-28)</button>
    </div>

    <!-- TAB 1: WORKBENCH -->
    <div id="pdf-pane" class="tab-pane active">
      <div class="interactive-pdf-container">
        
        <!-- Sayfa 1 & 2 -->
        <div class="pdf-interactive-page">
          <div class="page-banner"><span>📄 MEBİ Soru Kitapçığı - Sayfa 1 & 2 (Soru 1, 2, 3)</span><span>15 Puan</span></div>
          <div class="pdf-image-wrap"><img src="assets/pdf_pages/matematik_mebi/page_1.png" alt="Matematik 1" loading="eager"></div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/matematik_mebi/page_2.png" alt="Matematik 2" loading="lazy"></div>
          <div class="pdf-question-controls">{all_q_controls_p1}</div>
        </div>

        <!-- Sayfa 3, 4, 5 -->
        <div class="pdf-interactive-page">
          <div class="page-banner"><span>📄 MEBİ Soru Kitapçığı - Sayfa 3, 4, 5 (Soru 4, 5, 6)</span><span>15 Puan</span></div>
          <div class="pdf-image-wrap"><img src="assets/pdf_pages/matematik_mebi/page_3.png" alt="Matematik 3" loading="lazy"></div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/matematik_mebi/page_4.png" alt="Matematik 4" loading="lazy"></div>
          <div class="pdf-question-controls">{all_q_controls_p2}</div>
        </div>

        <!-- Sayfa 5, 6 -->
        <div class="pdf-interactive-page">
          <div class="page-banner"><span>📄 MEBİ Soru Kitapçığı - Sayfa 5 & 6 (Soru 7, 8, 9)</span><span>15 Puan</span></div>
          <div class="pdf-image-wrap"><img src="assets/pdf_pages/matematik_mebi/page_5.png" alt="Matematik 5" loading="lazy"></div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/matematik_mebi/page_6.png" alt="Matematik 6" loading="lazy"></div>
          <div class="pdf-question-controls">{all_q_controls_p3}</div>
        </div>

        <!-- Sayfa 7 & 8 -->
        <div class="pdf-interactive-page">
          <div class="page-banner"><span>📄 MEBİ Soru Kitapçığı - Sayfa 7 & 8 (Soru 10, 11)</span><span>10 Puan</span></div>
          <div class="pdf-image-wrap"><img src="assets/pdf_pages/matematik_mebi/page_7.png" alt="Matematik 7" loading="lazy"></div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/matematik_mebi/page_8.png" alt="Matematik 8" loading="lazy"></div>
          <div class="pdf-question-controls">{all_q_controls_p4}</div>
        </div>

        <!-- Sayfa 9 & 10 -->
        <div class="pdf-interactive-page">
          <div class="page-banner"><span>📄 MEBİ Soru Kitapçığı - Sayfa 9 & 10 (Soru 12, 13, 14)</span><span>15 Puan</span></div>
          <div class="pdf-image-wrap"><img src="assets/pdf_pages/matematik_mebi/page_9.png" alt="Matematik 9" loading="lazy"></div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/matematik_mebi/page_10.png" alt="Matematik 10" loading="lazy"></div>
          <div class="pdf-question-controls">{all_q_controls_p5}</div>
        </div>

        <!-- Sayfa 11 -->
        <div class="pdf-interactive-page">
          <div class="page-banner"><span>📄 MEBİ Soru Kitapçığı - Sayfa 11 (Soru 15, 16)</span><span>10 Puan</span></div>
          <div class="pdf-image-wrap"><img src="assets/pdf_pages/matematik_mebi/page_11.png" alt="Matematik 11" loading="lazy"></div>
          <div class="pdf-question-controls">{all_q_controls_p6}</div>
        </div>

        <!-- Sayfa 12 & 13 -->
        <div class="pdf-interactive-page">
          <div class="page-banner"><span>📄 MEBİ Soru Kitapçığı - Sayfa 12 & 13 (Soru 17, 18)</span><span>10 Puan</span></div>
          <div class="pdf-image-wrap"><img src="assets/pdf_pages/matematik_mebi/page_12.png" alt="Matematik 12" loading="lazy"></div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/matematik_mebi/page_13.png" alt="Matematik 13" loading="lazy"></div>
          <div class="pdf-question-controls">{all_q_controls_p7}</div>
        </div>

        <!-- Sayfa 14 & 15 -->
        <div class="pdf-interactive-page">
          <div class="page-banner"><span>📄 MEBİ Soru Kitapçığı - Sayfa 14 & 15 (Soru 19, 20, 21, 22)</span><span>20 Puan</span></div>
          <div class="pdf-image-wrap"><img src="assets/pdf_pages/matematik_mebi/page_14.png" alt="Matematik 14" loading="lazy"></div>
          <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/matematik_mebi/page_15.png" alt="Matematik 15" loading="lazy"></div>
          <div class="pdf-question-controls">{all_q_controls_p8}</div>
        </div>

      </div>

      <div style="text-align: center; margin: 36px 0;">
        <button class="btn-start" style="padding: 18px 42px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 7. Sınıf Matematik Notumu Hesapla
        </button>
      </div>
    </div>

    <!-- TAB 2: OFFICIAL SOLUTIONS -->
    <div id="answer-key-pane" class="tab-pane">
      <div class="pdf-interactive-page">
        <div class="page-banner" style="background:#047857;">
          <span>📄 MEBİ Resmi Öğretmen Çözüm Anahtarı (Sayfa 17-28)</span>
          <span style="font-size:0.85rem; opacity:0.85;">Temel Eğitim Genel Müdürlüğü</span>
        </div>
        <div class="pdf-image-wrap"><img src="assets/pdf_pages/matematik_mebi/page_17.png" alt="Çözüm 17" loading="lazy"></div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/matematik_mebi/page_18.png" alt="Çözüm 18" loading="lazy"></div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/matematik_mebi/page_19.png" alt="Çözüm 19" loading="lazy"></div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/matematik_mebi/page_20.png" alt="Çözüm 20" loading="lazy"></div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/matematik_mebi/page_21.png" alt="Çözüm 21" loading="lazy"></div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/matematik_mebi/page_22.png" alt="Çözüm 22" loading="lazy"></div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/matematik_mebi/page_23.png" alt="Çözüm 23" loading="lazy"></div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/matematik_mebi/page_24.png" alt="Çözüm 24" loading="lazy"></div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/matematik_mebi/page_25.png" alt="Çözüm 25" loading="lazy"></div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/matematik_mebi/page_26.png" alt="Çözüm 26" loading="lazy"></div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/matematik_mebi/page_27.png" alt="Çözüm 27" loading="lazy"></div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/matematik_mebi/page_28.png" alt="Çözüm 28" loading="lazy"></div>
      </div>
    </div>

  </main>

  {get_score_modal()}
  {get_footer()}

  <script src="assets/js/app.js"></script>
  <script>
    initLesson('matematik_7', 'tr-TR');
  </script>
</body>
</html>
"""

out_dir = r"d:\gpt\5_sinif_calisma_portali"
with open(os.path.join(out_dir, "7-matematik.html"), "w", encoding="utf-8") as f:
    f.write(generate_7_matematik())
print("7-matematik.html created successfully!")
