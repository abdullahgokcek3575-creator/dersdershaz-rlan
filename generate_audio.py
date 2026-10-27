# -*- coding: utf-8 -*-
"""
Studio-Grade Neural TTS Audio Generator for 5th Grade Study Portal
Uses Azure Neural Voices via edge-tts (tr-TR-EmelNeural & en-US-JennyNeural).
"""

import os, sys, ssl, asyncio
import edge_tts
import edge_tts.communicate as comm

# SSL bypass for environments with custom certificates
ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE
comm._SSL_CTX = ssl_ctx

AUDIO_DIR = r"d:\gpt\5_sinif_calisma_portali\assets\audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

VOICE_TR = "tr-TR-EmelNeural"
VOICE_EN = "en-US-JennyNeural"

# All audio items: (filename, text, voice)
AUDIO_ITEMS = [
    # ------------------ FEN BİLİMLERİ ------------------
    (
        "fen_summary.mp3",
        "5. Sınıf Fen Bilimleri 1. Dönem 1. Yazılı Konu Özeti. "
        "Bir: Güneş'in Özellikleri. Güneş küresel şekildedir, sıcak hidrojen ve helyum gazlarından oluşur. Dünyamızın temel ısı ve ışık kaynağıdır. Kendi ekseni etrafında saat yönünün tersine döner ve bu dönüş yaklaşık 25 gün sürer. "
        "İki: Ay'ın Yapısı. Ay'ın atmosferi yok denecek kadar incedir. Bu nedenle hava olayları görülmez, gece ile gündüz sıcaklık farkı aşırı fazladır ve ses iletilmez. "
        "Üç: Ay'ın Evreleri. Ay hem kendi etrafında döner hem de Dünya etrafında dolanır. İki hareket de yaklaşık 27 gün 8 saat sürer. Bu yüzden Dünya'dan Ay'ın hep aynı yüzü görülür. Dört ana evresi: Yeni Ay, İlk Dördün, Dolunay ve Son Dördündür. "
        "Dört: Dinamometre. Kuvvetin birimi Newton'dur. Dinamometredeki yayın uzama miktarı, cisme uygulanan kuvvetle doğru orantılıdır.",
        VOICE_TR
    ),
    (
        "fen_q1.mp3",
        "Soru 1. Aşağıda Dünyamıza en yakın yıldız olan Güneş'e ait görseller incelendiğinde; Güneş'in özelliklerinden 5 tanesini maddeler halinde yazınız.",
        VOICE_TR
    ),
    (
        "fen_sol1.mp3",
        "Soru 1'in çözümü. Öğretmen model cevabı: Bir: Şekli küreseldir. İki: Sıcak gazlardan, yani hidrojen ve helyumdan oluşur. Üç: Dünyamızın temel ısı ve ışık kaynağıdır. Dört: Dünyamıza en yakın yıldızdır. Beş: Kendi ekseni etrafında saat yönünün tersine, yani batıdan doğuya döner.",
        VOICE_TR
    ),
    (
        "fen_q2.mp3",
        "Soru 2. Pepee'nin ninesi şu soruları soruyor: A: Ay'da atmosfer yok denecek kadar az olduğu için Dünyada meydana gelen olaylardan hangileri Ay'da meydana gelmez? 3 örnek veriniz. B: Ay'da yaşayabilmek için Dünyadan götürülmesi gereken şeylere 3 örnek veriniz.",
        VOICE_TR
    ),
    (
        "fen_sol2.mp3",
        "Soru 2'nin çözümü. A şıkkı: Ay'da atmosfer olmadığı için yağmur, rüzgâr gibi hava olayları görülmez, ses iletilmediği için sesler duyulamaz ve gece gündüz sıcaklık farkı yüzlerce derecedir. B şıkkı: Götürülmesi gerekenler; oksijen tüpü, özel korumalı uzay giysisi, su ve dayanıklı besin maddeleridir.",
        VOICE_TR
    ),
    (
        "fen_q3.mp3",
        "Soru 3. Ay'ın hareketleri ile ilgili soruları cevaplayınız: A: Ay, Dünya etrafındaki dolanma hareketini hangi yönde yapar? B: Ay, Dünya etrafındaki dolanma hareketini ne kadar sürede tamamlar? C: Ay kendi ekseni etrafındaki dönme hareketini ne kadar sürede tamamlar?",
        VOICE_TR
    ),
    (
        "fen_sol3.mp3",
        "Soru 3'ün çözümü. A: Saat yönünün tersine, yani batıdan doğuya. B: Yaklaşık 27 gün 8 saatte tamamlar. C: Kendi ekseni etrafındaki dönüşünü de yaklaşık 27 gün 8 saatte tamamlar. Bu iki süre eşit olduğu için Dünyadan bakıldığında Ay'ın hep aynı yüzünü görürüz.",
        VOICE_TR
    ),
    (
        "fen_q4.mp3",
        "Soru 4 ve 5. Ay'ın Dünya etrafındaki dolanımı sırasında oluşan evrelerle ilgili: Ay'ın dört ana evresini sırasıyla yazınız. Ay'ın ara evrelerini yazınız. Ve Konum 1 ile Konum 5'te Ay'ın Dünyadan görünümünü belirtiniz.",
        VOICE_TR
    ),
    (
        "fen_sol4.mp3",
        "Soru 4 ve 5'in çözümü. Dört ana evre: Yeni Ay, İlk Dördün, Dolunay ve Son Dördün. İki ara evre: Hilal ve Şişkin Ay. Konum 1'de yani Yeni Ay evresinde Ay karanlıktır ve Dünyadan görünmez. Konum 5'te yani Dolunay evresinde ise Ay tamamen aydınlık bir daire şeklinde görünür.",
        VOICE_TR
    ),
    (
        "fen_q6.mp3",
        "Soru 6. Güneş, Dünya ve Ay'ın hareketlerinin bir tam turunu tamamlama sürelerini eşleştiriniz: K: Güneş'in kendi ekseni etrafında dönmesi. L: Dünya'nın Güneş etrafında dolanması. M: Ay'ın Dünya etrafında dolanması. N: Ay'ın kendi ekseni etrafında dönmesi. O: Dünya'nın kendi ekseni etrafında dönmesi.",
        VOICE_TR
    ),
    (
        "fen_sol6.mp3",
        "Soru 6'nın çözümü. K, Güneş'in dönmesi yaklaşık 25 gündür. L, Dünya'nın Güneş etrafında dolanması 365 gün 6 saat, yani bir yıldır. M, Ay'ın dolanması yaklaşık 27 gün 8 saattir. N, Ay'ın kendi etrafında dönmesi de yaklaşık 27 gün 8 saattir. O, Dünya'nın kendi ekseni etrafında dönmesi ise 24 saat, yani bir gündür.",
        VOICE_TR
    ),
    (
        "fen_q7.mp3",
        "Soru 7. Dinamometre ölçümleri: Özdeş dinamometrelere asılan K cisminin ağırlığı 72 Newton olarak ölçülmüş ve dinamometrenin 4 bölme uzadığı görülmüştür. Buna göre L, M, N, P ve R cisimlerinin ağırlıklarını hesaplayınız.",
        VOICE_TR
    ),
    (
        "fen_sol7.mp3",
        "Soru 7'nin adım adım çözümü. K cismi 72 Newton ağırlığındayken 4 bölme uzatmışsa; 72 bölü 4 eşittir 18 Newton eder. Yani her bir bölme 18 Newton'dur. L cismi 1 bölme uzattığı için 18 Newton. M cismi 2 bölme için 36 Newton. N cismi 3 bölme için 54 Newton. P cismi 5 bölme için 90 Newton. R cismi 6 bölme için 108 Newton ağırlığındadır.",
        VOICE_TR
    ),

    # ------------------ MATEMATİK ------------------
    (
        "mat_summary.mp3",
        "5. Sınıf Matematik 1. Dönem 1. Yazılı Konu Özeti. "
        "Çizim Araçları: Cetvel doğru çizgiler ve uzunluk ölçümü içindir. Gönye dik açıları yani 90 dereceyi çizmek içindir. Açıölçer veya iletki açı ölçmek içindir. Pergel ise çember çizmek içindir. "
        "Geometrik Semboller: Doğru parçası her iki ucu kapalı köşeli parantezle gösterilir: köşeli parantez A V. Işın ise başlangıç noktası kapalıdır. "
        "Açılar: Komşu tümler açıların ölçüleri toplamı 90 derecedir. Komşu bütünler açıların ölçüleri toplamı ise 180 derecedir. "
        "Çember: Çap, yarıçapın iki katıdır. Yani büyük R eşittir iki küçük r.",
        VOICE_TR
    ),
    (
        "mat_q1.mp3",
        "Soru 1. Aşağıdaki çizim araçlarının isimlerini yazınız: 1: Üçgen şeklindeki dik açı ölçüm aracı. 2: Düz çizgi çekme ve uzunluk ölçme aleti. 3: Yarım daire şeklindeki derece ölçme aleti. 4: İki kollu çember çizme aleti.",
        VOICE_TR
    ),
    (
        "mat_sol1.mp3",
        "Soru 1'in çözümü: Birinci araç gönye, ikinci araç cetvel, üçüncü araç açıölçer yani iletki, dördüncü araç ise pergeldir.",
        VOICE_TR
    ),
    (
        "mat_q2.mp3",
        "Soru 2. A ve V noktalarıyla verilen geometrik çizimleri sembolle gösteriniz: A: İki ucu da kapalı doğru parçası. B: A ucu kapalı, V ucu sonsuza giden ışın.",
        VOICE_TR
    ),
    (
        "mat_sol2.mp3",
        "Soru 2'nin çözümü: A şıkkı: Köşeli parantez A V veya köşeli parantez V A. Bu bir doğru parçasıdır. B şıkkı: A ucundan kapalı köşeli parantez A V. Bu bir ışındır.",
        VOICE_TR
    ),
    (
        "mat_q3.mp3",
        "Soru 3. Köşesi L olan, kolları K ve M noktalarından geçen bir açıyla ilgili istenen bilgileri yazınız: Açının kolları nedir? Açının köşesi neresidir? Sembolle üç farklı gösterimini yazınız.",
        VOICE_TR
    ),
    (
        "mat_sol3.mp3",
        "Soru 3'ün çözümü: Açının kolları L M ışını ve L K ışınıdır. Açının köşesi L noktasıdır. Sembolle gösterimi ise: K L M açısı, M L K açısı veya yalnızca L açısıdır. Köşe harfi daima ortada yazılır.",
        VOICE_TR
    ),
    (
        "mat_q4.mp3",
        "Soru 4 ve 5. Pergel kullanarak 3 santimetre yarıçaplı bir çemberin çizim adımlarını açıklayınız ve çemberin elemanları olan merkez, yarıçap ve çapı tanımlayınız.",
        VOICE_TR
    ),
    (
        "mat_sol4.mp3",
        "Soru 4 ve 5'in çözümü: Pergelin kollarının açıklığı cetvel üzerinde 3 santimetre olarak ayarlanır. İğneli sivri uç merkez noktasına batırılır ve kalemli uç 360 derece döndürülerek çember çizilir. Merkez çemberin tam ortasındaki noktadır. Yarıçap merkezden çembere olan 3 santimetrelik mesafedir. Çap ise merkezden geçen en uzun doğru parçasıdır ve 6 santimetredir.",
        VOICE_TR
    ),
    (
        "mat_q9.mp3",
        "Soru 9 ve 10. Aynı düzlemdeki iki doğrunun oluşturabileceği 4 durumu yazınız. Ve açı hesaplamalarını yapınız: 40 derecelik açının komşu tümleri kaç derecedir? 128 derecelik açının komşu bütünleri kaç derecedir?",
        VOICE_TR
    ),
    (
        "mat_sol9.mp3",
        "Soru 9 ve 10'un çözümü: İki doğru paralel olabilir, kesişebilir, dik kesişebilir veya çakışık olabilir. Açı hesaplaması: Tümler açıların toplamı 90 derece olduğu için 90 eksi 40 eşittir 50 derecedir. Bütünler açıların toplamı 180 derece olduğu için 180 eksi 128 eşittir 52 derecedir.",
        VOICE_TR
    ),

    # ------------------ TÜRKÇE ------------------
    (
        "turkce_summary.mp3",
        "5. Sınıf Türkçe 1. Dönem 1. Yazılı Konu Özeti. "
        "Sözcükte Anlam: Gerçek anlam aklımıza gelen ilk anlamdır. Mecaz anlam kelimenin gerçek anlamından tamamen uzaklaşmasıdır. Terim anlam ise bilim, sanat veya meslek alanına ait özel kavramlardır. "
        "Söz Sanatları: Kişileştirme yani teşhis; insana ait sevinmek, üzülmek, konuşmak gibi özelliklerin insan dışındaki varlıklara aktarılmasıdır. "
        "Yazım Kuralları: Belirli bir tarih bildiren ay ve gün adları büyük harfle başlar. Yer adlarında ilk isimden sonra gelen deniz, nehir, göl, dağ gibi ikinci tür isimleri büyük harfle başlar: Van Gölü, Ağrı Dağı gibi. Mahalle, cadde, sokak ve meydan kelimeleri büyük harfle yazılır.",
        VOICE_TR
    ),
    (
        "turkce_q1.mp3",
        "Soru 1. Pusula metninde anlamları verilen sözcükleri bulunuz: 1: Bilinen bilgilerden yararlanarak daha önce bilinmeyen yeni bir bulguya ulaşma, buluş. 2: Çoğu sularda ve ağaç taş üzerinde yetişen ilkel bitki. 3: Demiri ve bazı metalleri çeken demir oksit.",
        VOICE_TR
    ),
    (
        "turkce_sol1.mp3",
        "Soru 1'in çözümü: Birinci sözcük icat yani buluştur. İkinci sözcük yosundur. Üçüncü sözcük ise mıknatıstır.",
        VOICE_TR
    ),
    (
        "turkce_q2.mp3",
        "Soru 2. Yapay zekâ metnine göre: A: Yapay zekâ sunucularında neden yüksek miktarda su tüketilmektedir? B: Kullanıcıların sorularına eklediği gereksiz ifadeler su ve elektrik tüketimini nasıl etkilemektedir?",
        VOICE_TR
    ),
    (
        "turkce_sol2.mp3",
        "Soru 2'nin çözümü: A şıkkı: Devasa veri merkezlerindeki sunucuların soğutulması amacıyla yüksek miktarda su tüketilmektedir. B şıkkı: Sorulara eklenen gereksiz her ifade işlem süresini uzatmakta, bu da doğrudan enerji ve su tüketimini artırmaktadır.",
        VOICE_TR
    ),
    (
        "turkce_q4.mp3",
        "Soru 4. Söz sanatlarından kişileştirmeye uygun iki farklı örnek cümle yazınız.",
        VOICE_TR
    ),
    (
        "turkce_sol4.mp3",
        "Soru 4'ün çözümü. Öğretmen model cümleleri: Bir: Yorgun rüzgâr akşam olunca ağaçların dallarına yaslanıp dinlendi. İki: Sabah güneşi odamın penceresinden bana neşeyle gülümsedi.",
        VOICE_TR
    ),
    (
        "turkce_q5.mp3",
        "Soru 5. Aşağıdaki yazım kurallarını örnekleyen birer cümle yazınız: 1: Belirli bir tarih bildiren ay ve gün adları büyük harfle başlar. 2: Yer adlarında tür bildiren ikinci isimler büyük harfle başlar. 3: Mahalle, cadde ve sokak adları büyük harfle başlar.",
        VOICE_TR
    ),
    (
        "turkce_sol5.mp3",
        "Soru 5'in çözümü: 1. Cümle: Okulumuz 23 Nisan Pazartesi günü bayram kutlaması yapacak. 2. Cümle: Bu yaz Van Gölü ve Ağrı Dağı bölgesini ziyaret ettik. 3. Cümle: Evimiz Atatürk Caddesi, Menekşe Sokak üzerinde yer alıyor.",
        VOICE_TR
    ),

    # ------------------ SOSYAL BİLGİLER ------------------
    (
        "sosyal_summary.mp3",
        "5. Sınıf Sosyal Bilgiler 1. Dönem 1. Yazılı Konu Özeti. "
        "Rol ve Sorumluluk: Bir kimsenin grup veya kurumda üzerine düşen göreve rol denir. Bir kişi aynı anda birden fazla role sahip olabilir: evde evlat ve abi, okulda öğrenci, takımda kaptan olabiliriz. "
        "Sadaka Taşları: Selçuklu ve Osmanlı döneminde meydanlara ve cami yanlarına konulan oyuk taşlardır. Varlıklı kimseler gizlice para bırakır, ihtiyaç sahipleri geceleri yalnızca ihtiyacı kadarını alırdı. Böylece kimse mahcup edilmeden dayanışma sağlanırdı. "
        "Millî Mücadele: Mustafa Kemal Paşa'nın Tekâlif-i Milliye emirleriyle halkımız ordumuzla el ele vererek eşsiz bir dayanışma sergilemiştir.",
        VOICE_TR
    ),
    (
        "sosyal_q1.mp3",
        "Soru 1. Bu sorumlulukların yerine getirilmesini isteyen rollerin adlarını yazınız: 1: Öğrencilerle ilgilenmek, görev ve sorumluluklarını onlara hatırlatmak. 2: Ev işlerinde çocukların yardımcı olmasını istemek.",
        VOICE_TR
    ),
    (
        "sosyal_sol1.mp3",
        "Soru 1'in çözümü: Birinci rol öğretmen rolüdür. İkinci rol ise anne veya baba, yani ebeveyn rolüdür.",
        VOICE_TR
    ),
    (
        "sosyal_q2.mp3",
        "Soru 2. Osman Furkan evde anne baba ve küçük kardeşiyle birlikte yaşamakta, Yeşilyurt Ortaokulu 5. sınıfta okumakta ve okul futbol takımında kaptanlık yapmaktadır. Osman Furkan'ın 4 farklı rolünü yazınız.",
        VOICE_TR
    ),
    (
        "sosyal_sol2.mp3",
        "Soru 2'nin çözümü: Anne ve babasına göre evlat yani çocuktur. Küçük kardeşine göre ağabeydir. Okulda öğrencidir. Futbol takımında ise takım kaptanı ve sporcudur.",
        VOICE_TR
    ),
    (
        "sosyal_q5.mp3",
        "Soru 5. Selçuklu ve Osmanlı Dönemi'nde meydanlara konulan, zenginlerin gizlice para bıraktığı, ihtiyaç sahiplerinin kimseye görünmeden ihtiyacı kadarını aldığı uygulamanın adı nedir ve hangi amaçla yapılmıştır?",
        VOICE_TR
    ),
    (
        "sosyal_sol5.mp3",
        "Soru 5'in çözümü: Bu uygulamanın adı Sadaka Taşıdır. Amacı; ihtiyaç sahiplerini rencide etmeden, gururlarını incitmeden gizlice yardım etmek ve toplumda birlik, beraberlik ve yardımlaşmayı güçlendirmektir.",
        VOICE_TR
    ),

    # ------------------ DİN KÜLTÜRÜ ------------------
    (
        "din_summary.mp3",
        "5. Sınıf Din Kültürü ve Ahlak Bilgisi 1. Dönem 1. Yazılı Konu Özeti. "
        "Evrendeki Düzen: Evrende hiçbir şey tesadüf değildir; gece ile gündüzün birbirini izlemesi, mevsimlerin oluşumu ve su döngüsü bir ölçü ve dengenin göstergesidir. "
        "Esmâ-i Hüsnâ: Allah'ın en güzel isimleridir. Alîm; her şeyi hakkıyla bilen demektir. Semî; her şeyi işiten demektir. Basîr; her şeyi gören demektir. Kadîr; sonsuz güç sahibi, her şeye gücü yeten demektir. "
        "İhlas Suresi ve Tevhit: Tevhit inancı, Allah'ın bir ve tek olduğuna, eşi ve benzeri olmadığına inanmaktır. Samed ismi, her şeyin Allah'a muhtaç olduğu, Allah'ın ise hiçbir şeye muhtaç olmadığı anlamına gelir.",
        VOICE_TR
    ),
    (
        "din_q1.mp3",
        "Soru 1. Allah'ın evreni bir denge ve düzen içinde yaratmasına 3 örnek yazınız.",
        VOICE_TR
    ),
    (
        "din_sol1.mp3",
        "Soru 1'in çözümü: Bir: Gece ve gündüzün düzenli olarak birbirini izlemesi. İki: Mevsimlerin belli bir düzen içinde birbirini takip etmesi. Üç: Yağmur döngüsüyle yeryüzündeki canlıların su ve besin ihtiyacının karşılanması.",
        VOICE_TR
    ),
    (
        "din_q2.mp3",
        "Soru 2. Aşağıdaki ayet meallerinin Allah'ın hangi güzel ismine işaret ettiğini yazınız: 1: O, göklerde ve yerde olan her şeyi bilir. 2: Allah her şeyi hakkıyla işitmekte ve her şeyi görmektedir. 3: O, her şeye hakkıyla gücü yetendir.",
        VOICE_TR
    ),
    (
        "din_sol2.mp3",
        "Soru 2'nin çözümü: Birinci isim Alîm. İkinci isimler Semî ve Basîr. Üçüncü isim ise Kadîr ismidir.",
        VOICE_TR
    ),
    (
        "din_q4.mp3",
        "Soru 4. İhlas Suresi'nin okunuşundaki boşlukları tamamlayınız ve Tevhit ile Samed kavramlarının anlamını belirtiniz.",
        VOICE_TR
    ),
    (
        "din_sol4.mp3",
        "Soru 4'ün çözümü: İhlas Suresi: Kul hüvellâhü ehad. Allâhü's-samed. Lem yelid ve lem yûled. Ve lem yekün lehû küfüven ehad. Tevhit, Allah'ın bir ve tek olmasıdır. Samed ise herkesin O'na muhtaç olması, O'nun ise hiçbir şeye muhtaç olmaması demektir.",
        VOICE_TR
    ),

    # ------------------ İNGİLİZCE (NATIVE ENGLISH) ------------------
    (
        "ingilizce_summary.mp3",
        "5th Grade English First Term First Exam Study Notes. "
        "Topic 1: Telling the time. For sharp hours say: It is two o'clock. For past say: It is quarter past four, or It is ten past three. For half say: It is half past six. For to say: It is quarter to ten. "
        "Topic 2: Articles a, an, and the. Use a before consonant sounds, like a book, a cat. Use an before vowel sounds, like an apple, an elephant. Use the for specific things. "
        "Topic 3: School rules with must and mustn't. We use must for obligations, like: You must follow the rules. We use mustn't for prohibitions, like: You mustn't use your phone in the library.",
        VOICE_EN
    ),
    (
        "ingilizce_q1.mp3",
        "Part A. Look at Fred's weekly timetable and answer the questions: One: How many classes does Fred have in a week? Two: Which classes does he have on Friday? Three: When does Fred have English class?",
        VOICE_EN
    ),
    (
        "ingilizce_sol1.mp3",
        "Solution for Part A: Number 1: He has twenty classes in a week. Number 2: He has Turkish, Music and ICT on Friday. Number 3: He has English class on Tuesday and Thursday.",
        VOICE_EN
    ),
    (
        "ingilizce_q2.mp3",
        "Part B. Write down the time in words: Number 1: 11:00. Number 2: 07:15. Number 3: 09:45. Number 4: 07:30.",
        VOICE_EN
    ),
    (
        "ingilizce_sol2.mp3",
        "Solution for Part B: 1: It's eleven o'clock. 2: It's quarter past seven. 3: It's quarter to ten. 4: It's half past seven.",
        VOICE_EN
    ),
    (
        "ingilizce_q3.mp3",
        "Part C. Read Mia's story and answer the questions: What time does Mia wake up? Does Mia walk to school? What does Mia do at 5:00 p.m.? Does Mia have dinner at 6:00 p.m.? Who does Mia play volleyball with?",
        VOICE_EN
    ),
    (
        "ingilizce_sol3.mp3",
        "Solution for Part C: 1: She wakes up at 6:30 a.m. 2: Yes, she does. 3: She plays volleyball with her friends in the park. 4: No, she does not, she has dinner at 7:00 p.m. 5: She plays with her friends.",
        VOICE_EN
    ),
    (
        "ingilizce_q5.mp3",
        "Part D and E. Write the numbers in words for 92, 100, and 65. And complete the rules with must or mustn't.",
        VOICE_EN
    ),
    (
        "ingilizce_sol5.mp3",
        "Solution for Part D and E: Numbers: 92 is ninety-two, 100 is one hundred, 65 is sixty-five. Rules: 1: You must follow the rules. 2: You mustn't use your phone in the library. 3: You must be kind to your classmates. 4: You mustn't eat or drink in the lab.",
        VOICE_EN
    )
]

async def generate_all_audio():
    print(f"Total audio files to generate: {len(AUDIO_ITEMS)}")
    for filename, text, voice in AUDIO_ITEMS:
        out_path = os.path.join(AUDIO_DIR, filename)
        if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
            print(f"Skipping existing: {filename}")
            continue
        print(f"Generating {filename} with voice {voice}...")
        try:
            comm_obj = edge_tts.Communicate(text, voice)
            await comm_obj.save(out_path)
            print(f"  Saved: {filename} ({os.path.getsize(out_path)} bytes)")
        except Exception as e:
            print(f"  Error on {filename}: {e}")
    print("All audio files generated successfully!")

if __name__ == "__main__":
    asyncio.run(generate_all_audio())
