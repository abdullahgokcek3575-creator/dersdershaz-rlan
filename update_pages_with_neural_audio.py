# -*- coding: utf-8 -*-
"""
Updates build_portal.py with playAudio calls and regenerates all HTML pages.
"""

import os, re, shutil

BUILD_SCRIPT = r"d:\gpt\5_sinif_calisma_portali\build_portal.py"

with open(BUILD_SCRIPT, "r", encoding="utf-8") as f:
    content = f.read()

# Replacements mapping
replacements = [
    # Fen
    ("speakSummary('fenSummaryArea')", "playAudio('fen_summary.mp3')"),
    ("speakQuestion('q_fen_1')", "playAudio('fen_q1.mp3', 'q_fen_1')"),
    ("speakSolution('q_fen_1')", "playAudio('fen_sol1.mp3', 'q_fen_1')"),
    ("speakQuestion('q_fen_2')", "playAudio('fen_q2.mp3', 'q_fen_2')"),
    ("speakSolution('q_fen_2')", "playAudio('fen_sol2.mp3', 'q_fen_2')"),
    ("speakQuestion('q_fen_3')", "playAudio('fen_q3.mp3', 'q_fen_3')"),
    ("speakSolution('q_fen_3')", "playAudio('fen_sol3.mp3', 'q_fen_3')"),
    ("speakQuestion('q_fen_4')", "playAudio('fen_q4.mp3', 'q_fen_4')"),
    ("speakSolution('q_fen_4')", "playAudio('fen_sol4.mp3', 'q_fen_4')"),
    ("speakQuestion('q_fen_6')", "playAudio('fen_q6.mp3', 'q_fen_6')"),
    ("speakSolution('q_fen_6')", "playAudio('fen_sol6.mp3', 'q_fen_6')"),
    ("speakQuestion('q_fen_7')", "playAudio('fen_q7.mp3', 'q_fen_7')"),
    ("speakSolution('q_fen_7')", "playAudio('fen_sol7.mp3', 'q_fen_7')"),

    # Mat
    ("speakSummary('matSummaryArea')", "playAudio('mat_summary.mp3')"),
    ("speakQuestion('q_mat_1')", "playAudio('mat_q1.mp3', 'q_mat_1')"),
    ("speakSolution('q_mat_1')", "playAudio('mat_sol1.mp3', 'q_mat_1')"),
    ("speakQuestion('q_mat_2')", "playAudio('mat_q2.mp3', 'q_mat_2')"),
    ("speakSolution('q_mat_2')", "playAudio('mat_sol2.mp3', 'q_mat_2')"),
    ("speakQuestion('q_mat_3')", "playAudio('mat_q3.mp3', 'q_mat_3')"),
    ("speakSolution('q_mat_3')", "playAudio('mat_sol3.mp3', 'q_mat_3')"),
    ("speakQuestion('q_mat_4')", "playAudio('mat_q4.mp3', 'q_mat_4')"),
    ("speakSolution('q_mat_4')", "playAudio('mat_sol4.mp3', 'q_mat_4')"),
    ("speakQuestion('q_mat_9')", "playAudio('mat_q9.mp3', 'q_mat_9')"),
    ("speakSolution('q_mat_9')", "playAudio('mat_sol9.mp3', 'q_mat_9')"),

    # Türkçe
    ("speakSummary('turkceSummaryArea')", "playAudio('turkce_summary.mp3')"),
    ("speakQuestion('q_tr_1')", "playAudio('turkce_q1.mp3', 'q_tr_1')"),
    ("speakSolution('q_tr_1')", "playAudio('turkce_sol1.mp3', 'q_tr_1')"),
    ("speakQuestion('q_tr_2')", "playAudio('turkce_q2.mp3', 'q_tr_2')"),
    ("speakSolution('q_tr_2')", "playAudio('turkce_sol2.mp3', 'q_tr_2')"),
    ("speakQuestion('q_tr_4')", "playAudio('turkce_q4.mp3', 'q_tr_4')"),
    ("speakSolution('q_tr_4')", "playAudio('turkce_sol4.mp3', 'q_tr_4')"),
    ("speakQuestion('q_tr_5')", "playAudio('turkce_q5.mp3', 'q_tr_5')"),
    ("speakSolution('q_tr_5')", "playAudio('turkce_sol5.mp3', 'q_tr_5')"),

    # Sosyal
    ("speakSummary('sosyalSummaryArea')", "playAudio('sosyal_summary.mp3')"),
    ("speakQuestion('q_sos_1')", "playAudio('sosyal_q1.mp3', 'q_sos_1')"),
    ("speakSolution('q_sos_1')", "playAudio('sosyal_sol1.mp3', 'q_sos_1')"),
    ("speakQuestion('q_sos_2')", "playAudio('sosyal_q2.mp3', 'q_sos_2')"),
    ("speakSolution('q_sos_2')", "playAudio('sosyal_sol2.mp3', 'q_sos_2')"),
    ("speakQuestion('q_sos_5')", "playAudio('sosyal_q5.mp3', 'q_sos_5')"),
    ("speakSolution('q_sos_5')", "playAudio('sosyal_sol5.mp3', 'q_sos_5')"),

    # Din
    ("speakSummary('dinSummaryArea')", "playAudio('din_summary.mp3')"),
    ("speakQuestion('q_din_1')", "playAudio('din_q1.mp3', 'q_din_1')"),
    ("speakSolution('q_din_1')", "playAudio('din_sol1.mp3', 'q_din_1')"),
    ("speakQuestion('q_din_2')", "playAudio('din_q2.mp3', 'q_din_2')"),
    ("speakSolution('q_din_2')", "playAudio('din_sol2.mp3', 'q_din_2')"),
    ("speakQuestion('q_din_4')", "playAudio('din_q4.mp3', 'q_din_4')"),
    ("speakSolution('q_din_4')", "playAudio('din_sol4.mp3', 'q_din_4')"),

    # İngilizce
    ("speakSummary('engSummaryArea')", "playAudio('ingilizce_summary.mp3')"),
    ("speakQuestion('q_eng_1')", "playAudio('ingilizce_q1.mp3', 'q_eng_1')"),
    ("speakSolution('q_eng_1')", "playAudio('ingilizce_sol1.mp3', 'q_eng_1')"),
    ("speakQuestion('q_eng_2')", "playAudio('ingilizce_q2.mp3', 'q_eng_2')"),
    ("speakSolution('q_eng_2')", "playAudio('ingilizce_sol2.mp3', 'q_eng_2')"),
    ("speakQuestion('q_eng_3')", "playAudio('ingilizce_q3.mp3', 'q_eng_3')"),
    ("speakSolution('q_eng_3')", "playAudio('ingilizce_sol3.mp3', 'q_eng_3')"),
    ("speakQuestion('q_eng_5')", "playAudio('ingilizce_q5.mp3', 'q_eng_5')"),
    ("speakSolution('q_eng_5')", "playAudio('ingilizce_sol5.mp3', 'q_eng_5')"),
]

for old, new in replacements:
    content = content.replace(old, new)

with open(BUILD_SCRIPT, "w", encoding="utf-8") as f:
    f.write(content)

print("build_portal.py successfully updated with playAudio calls.")
