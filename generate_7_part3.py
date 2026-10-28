# -*- coding: utf-8 -*-
"""
Generate 7th Grade English (10 Questions) and Mathematics (22 Questions)
"""

import os
from generate_7_part1 import get_header, get_footer, get_score_modal, build_q_strip

# =========================================================================
# 5. 7. SINIF İNGİLİZCE (10 Soru - 100 Puan)
# =========================================================================
def generate_7_ingilizce():
    q1 = build_q_strip(1, "Personality Adjectives", 10, "ing7_q1.mp3", "ing7_sol1.mp3",
        "Question 1. Complete the sentences with the correct personality words: hardworking, punctual, selfish, outgoing, honest.",
        "Question 1 solution. 1 hardworking, 2 punctual, 3 selfish, 4 outgoing, 5 honest.",
        "1. Sally always does her homework and studies hard: She is <strong>hardworking</strong>.<br>2. Tom is never late for school, arrives on time: He is <strong>punctual</strong>.<br>3. My brother doesn't like sharing his things: He is <strong>selfish</strong>.<br>4. Helen likes meeting new people and has a lot of friends: She is <strong>outgoing</strong>.<br>5. Mike never tells lies, always tells the truth: He is <strong>honest</strong>.",
        "1: hardworking, 2: punctual, 3: selfish, 4: outgoing, 5: honest...")

    q2 = build_q_strip(2, "Match Descriptions with Pictures", 10, "ing7_q2.mp3", "ing7_sol2.mp3",
        "Question 2. Match the appearance descriptions with the numbers 1 to 5.",
        "Question 2 solution. 1 Daisy (ginger hair), 2 Tom (short wavy hair, thin), 3 Jack (plump, short brown hair), 4 Sarah (blonde hair, blue eyes), 5 Zack (curly brown hair, glasses).",
        "• <strong>1:</strong> <strong>Daisy</strong> (cute with wavy ginger hair, brown eyes)<br>• <strong>2:</strong> <strong>Tom</strong> (short wavy hair, thin)<br>• <strong>3:</strong> <strong>Jack</strong> (plump with short brown hair, brown eyes)<br>• <strong>4:</strong> <strong>Sarah</strong> (beautiful girl with blue eyes and blonde hair)<br>• <strong>5:</strong> <strong>Zack</strong> (curly brown hair, wears glasses)",
        "1: Daisy, 2: Tom, 3: Jack, 4: Sarah, 5: Zack...")

    q3 = build_q_strip(3, "Comparative Adjectives Table", 10, "ing7_q3.mp3", "ing7_sol3.mp3",
        "Question 3. Compare Sally (15 yrs, 1.71m, 45kg) and Helen (17 yrs, 1.65m, 50kg).",
        "Question 3 solution. 1 older, 2 younger, 3 shorter, 4 lighter or slimmer, 5 more generous.",
        "1. Helen is <strong>older</strong> than Sally. (17 > 15)<br>2. Sally is <strong>younger</strong> than Helen. (15 < 17)<br>3. Helen is <strong>shorter</strong> than Sally. (1.65m < 1.71m)<br>4. Sally is <strong>lighter / slimmer / thinner</strong> than Helen. (45kg < 50kg)<br>5. Sally is <strong>more generous</strong> than Helen. (5 stars vs 2 stars)",
        "1: older, 2: younger, 3: shorter, 4: slimmer, 5: more generous...")

    q4 = build_q_strip(4, "Correct the Mistakes in the Text", 10, "ing7_q4.mp3", "ing7_sol4.mp3",
        "Question 4. Read the text about Amy and Emma and rewrite the false sentences correctly.",
        "Question 4 solution. 1 Amy is older than Emma. 2 Emma is shorter than Amy. 3 Amy has straight blond hair. 4 Emma is more outgoing than Amy. 5 Amy doesn't change her mind easily.",
        "1. <em>Amy is younger than Emma.</em> → <strong>Amy is older than Emma.</strong> (16 > 12)<br>2. <em>Emma is taller than Amy.</em> → <strong>Emma is shorter than Amy.</strong> (160cm < 165cm)<br>3. <em>Amy has wavy blond hair and green eyes.</em> → <strong>Amy has straight blonde hair and brown eyes.</strong><br>4. <em>Amy is more outgoing than Emma.</em> → <strong>Emma is more outgoing than Amy.</strong><br>5. <em>Emma doesn't change her mind easily.</em> → <strong>Amy doesn't change her mind easily. (She is stubborn.)</strong>",
        "1. Amy is older... \n2. Emma is shorter... \n3. ...")

    q5 = build_q_strip(5, "Complete Table from Dialogue (Sam & Brian)", 10, "ing7_q5.mp3", "ing7_sol5.mp3",
        "Question 5. Complete the table for Sam and Brian: Appearance and Personality.",
        "Question 5 solution. Sam: tall, slim, dark hair; serious, hardworking. Brian: short, blond hair; funny, outgoing, social.",
        "• <strong>SAM:</strong><br>&nbsp;&nbsp;Appearance: <strong>tall, slim, dark hair</strong><br>&nbsp;&nbsp;Personality: <strong>serious and hardworking</strong><br><br>• <strong>BRIAN:</strong><br>&nbsp;&nbsp;Appearance: <strong>short, blond hair</strong><br>&nbsp;&nbsp;Personality: <strong>funny, outgoing (social)</strong>",
        "Sam: ... \nBrian: ...")

    q6 = build_q_strip(6, "Rose's Daily Routine Reading Questions", 10, "ing7_q6.mp3", "ing7_sol6.mp3",
        "Question 6. Answer the 4 questions according to the text about Rose's daily routine.",
        "Question 6 solution. 1 She plays volleyball with her friends. 2 She goes hiking twice a week. 3 She usually rides her bike. 4 Yes, she does.",
        "1. <strong>What does Rose do after school?</strong><br>→ <em>She plays volleyball with her friends.</em><br><br>2. <strong>How often does she go hiking?</strong><br>→ <em>She goes hiking twice a week (on Tuesdays and Thursdays).</em><br><br>3. <strong>What does Rose do on Sundays?</strong><br>→ <em>She usually rides her bike.</em><br><br>4. <strong>Does she go to bed early?</strong><br>→ <em>Yes, she does.</em>",
        "1: Volleyball... \n2: Twice a week... \n3: Rides bike... \n4: Yes, she does.")

    q7 = build_q_strip(7, "Adverbs of Frequency (100% to 0%)", 10, "ing7_q7.mp3", "ing7_sol7.mp3",
        "Question 7. Fill in the blanks with frequency adverbs: 100%, 0%, 70%, 90%, 50%.",
        "Question 7 solution. 1 always, 2 never, 3 often, 4 usually, 5 sometimes.",
        "1. I <strong>always</strong> do exercise in the morning to stay fit. (100%)<br>2. I <strong>never</strong> eat junk food. (0%)<br>3. I <strong>often</strong> play basketball in the school garden. (70%)<br>4. I <strong>usually</strong> go to the gym on weekdays. (90%)<br>5. I <strong>sometimes</strong> go swimming with my friends at the weekend. (50%)",
        "1: always, 2: never, 3: often, 4: usually, 5: sometimes...")

    q8 = build_q_strip(8, "Scott's Routine Reading Questions", 10, "ing7_q8.mp3", "ing7_sol8.mp3",
        "Question 8. Answer the 3 questions about Scott the football player.",
        "Question 8 solution. 1 He wakes up at seven in the morning. 2 He spends time with his family and watches movies. 3 Because he wants to be a successful football player.",
        "1. <strong>What time does Scott get up?</strong><br>→ <em>He always wakes up at seven (7:00) in the morning.</em><br><br>2. <strong>What does he do in the evenings?</strong><br>→ <em>He spends time with his family and they watch movies together.</em><br><br>3. <strong>Why does Scott train hard?</strong><br>→ <em>Because he wants to be a successful football player.</em>",
        "1: At 7:00 a.m. \n2: Watches movies with family... \n3: To be successful...")

    q9 = build_q_strip(9, "Identify Sports from Clues", 10, "ing7_q9.mp3", "ing7_sol9.mp3",
        "Question 9. Read the sentences and identify the 5 sports: a, b, c, d, e.",
        "Question 9 solution. a Football, b Tennis, c Volleyball, d Archery, e Hiking or Trekking.",
        "• <strong>a:</strong> <strong>Football (Soccer)</strong> (11 players, kick the ball into the goal)<br>• <strong>b:</strong> <strong>Tennis</strong> (racket, small yellow ball, over the net)<br>• <strong>c:</strong> <strong>Volleyball</strong> (net, ball, hit with hands or arms)<br>• <strong>d:</strong> <strong>Archery</strong> (bow, arrows, target center)<br>• <strong>e:</strong> <strong>Hiking / Trekking</strong> (sneakers, backpack, mountains or forests)",
        "a: Football, b: Tennis, c: Volleyball, d: Archery, e: Hiking...")

    q10 = build_q_strip(10, "Complete Sport Table (Jack & Sarah)", 10, "ing7_q10.mp3", "ing7_sol10.mp3",
        "Question 10. Complete the table: Sport, Equipment, Place, Frequency for Jack and Sarah.",
        "Question 10 solution. Jack: Basketball, ball and basket, basketball court, four times a week. Sarah: Tennis, racket and ball, tennis court, twice a week.",
        "• <strong>JACK:</strong><br>&nbsp;&nbsp;Sport: <strong>Basketball</strong><br>&nbsp;&nbsp;Equipment: <strong>Ball and basket</strong><br>&nbsp;&nbsp;Place: <strong>Basketball court</strong><br>&nbsp;&nbsp;Frequency: <strong>Four times a week</strong><br><br>• <strong>SARAH:</strong><br>&nbsp;&nbsp;Sport: <strong>Tennis</strong><br>&nbsp;&nbsp;Equipment: <strong>Racket and ball</strong><br>&nbsp;&nbsp;Place: <strong>Tennis court</strong><br>&nbsp;&nbsp;Frequency: <strong>Twice a week</strong>",
        "Jack: Basketball... \nSarah: Tennis...")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>7. Sınıf İngilizce 1. Dönem 1. Yazılı - MEBİ Soruları ve Çözümleri</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body class="theme-ingilizce">
  {get_header('ing7')}

  <main class="container">
    <div class="lesson-header">
      <div class="lesson-info">
        <h1><span>🇬🇧</span> 7. Sınıf İngilizce 1. Dönem 1. Yazılı (MEBİ)</h1>
        <p>Appearances & Personalities • Comparatives • Sports & Routines • 10 Sorunun Tamamı Çözümlü</p>
      </div>
      <div class="score-box">
        <div class="score-val" id="currentScoreVal">0</div>
        <div class="score-lbl">Score / 100</div>
      </div>
    </div>

    <!-- Audio Player Bar -->
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
        <button class="btn-audio primary" onclick="portalApp.speakText('7th Grade English 1st Term 1st Exam Revision. Describing physical appearance and personality, comparative adjectives older, taller, more generous, frequency adverbs always, usually, often, sometimes, never, sports equipments and reading comprehension.')">📢 Listen Revision Notes</button>
      </div>
    </div>

    <!-- Tabs -->
    <div class="tabs-nav">
      <button class="tab-btn active" data-tab="pdf-pane">📄 Orijinal MEBİ PDF'i Üzerinde Soruları Çöz</button>
      <button class="tab-btn" data-tab="answer-key-pane">🔑 Answer Key (Sayfa 5 & 6)</button>
    </div>

    <!-- TAB 1: WORKBENCH -->
    <div id="pdf-pane" class="tab-pane active">
      <div class="interactive-pdf-container">
        
        <!-- Sayfa 1 -->
        <div class="pdf-interactive-page">
          <div class="page-banner"><span>📄 Exam Paper Page 1 (Questions 1, 2, 3)</span><span>30 Points</span></div>
          <div class="pdf-image-wrap"><img src="assets/pdf_pages/ingilizce_mebi/page_1.png" alt="İngilizce Sayfa 1" loading="eager"></div>
          <div class="pdf-question-controls">{q1}<hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">{q2}<hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">{q3}</div>
        </div>

        <!-- Sayfa 2 -->
        <div class="pdf-interactive-page">
          <div class="page-banner"><span>📄 Exam Paper Page 2 (Questions 4, 5)</span><span>20 Points</span></div>
          <div class="pdf-image-wrap"><img src="assets/pdf_pages/ingilizce_mebi/page_2.png" alt="İngilizce Sayfa 2" loading="lazy"></div>
          <div class="pdf-question-controls">{q4}<hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">{q5}</div>
        </div>

        <!-- Sayfa 3 -->
        <div class="pdf-interactive-page">
          <div class="page-banner"><span>📄 Exam Paper Page 3 (Questions 6, 7, 8)</span><span>30 Points</span></div>
          <div class="pdf-image-wrap"><img src="assets/pdf_pages/ingilizce_mebi/page_3.png" alt="İngilizce Sayfa 3" loading="lazy"></div>
          <div class="pdf-question-controls">{q6}<hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">{q7}<hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">{q8}</div>
        </div>

        <!-- Sayfa 4 -->
        <div class="pdf-interactive-page">
          <div class="page-banner"><span>📄 Exam Paper Page 4 (Questions 9, 10)</span><span>20 Points</span></div>
          <div class="pdf-image-wrap"><img src="assets/pdf_pages/ingilizce_mebi/page_4.png" alt="İngilizce Sayfa 4" loading="lazy"></div>
          <div class="pdf-question-controls">{q9}<hr style="border:none; border-top:1px solid #e2e8f0; margin:14px 0;">{q10}</div>
        </div>

      </div>

      <div style="text-align: center; margin: 36px 0;">
        <button class="btn-start" style="padding: 18px 42px; font-size: 1.15rem; cursor: pointer;" onclick="portalApp.finishExam()">
          🏆 Calculate My 7th Grade English Score
        </button>
      </div>
    </div>

    <!-- TAB 2: OFFICIAL SOLUTIONS -->
    <div id="answer-key-pane" class="tab-pane">
      <div class="pdf-interactive-page">
        <div class="page-banner" style="background:#047857;">
          <span>📄 MEBİ Official Answer Key (Pages 5 & 6)</span>
          <span style="font-size:0.85rem; opacity:0.85;">Ministry of National Education</span>
        </div>
        <div class="pdf-image-wrap"><img src="assets/pdf_pages/ingilizce_mebi/page_5.png" alt="Cevap 5" loading="lazy"></div>
        <div class="pdf-image-wrap" style="border-top:2px solid #e2e8f0;"><img src="assets/pdf_pages/ingilizce_mebi/page_6.png" alt="Cevap 6" loading="lazy"></div>
      </div>
    </div>

  </main>

  {get_score_modal()}
  {get_footer()}

  <script src="assets/js/app.js"></script>
  <script>
    initLesson('ingilizce_7', 'en-US');
  </script>
</body>
</html>
"""

out_dir = r"d:\gpt\5_sinif_calisma_portali"
with open(os.path.join(out_dir, "7-ingilizce.html"), "w", encoding="utf-8") as f:
    f.write(generate_7_ingilizce())
print("7-ingilizce.html created!")
