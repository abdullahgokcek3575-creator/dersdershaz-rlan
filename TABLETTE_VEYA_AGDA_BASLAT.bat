@echo off
chcp 65001 > nul
title 5. Sinif Calisma Portali - Agda Yayinlama Sunucusu
cls
echo ====================================================================
echo       5. SINIF 1. DONEM 1. YAZILI CALISMA PORTALI YAYINI
echo ====================================================================
echo.
echo Bu bilgisayar ag uzerinde bir web sunucusu olarak baslatildi!
echo.
echo TABLET, TELEFON veya DIGER BILGISAYARLAR ICIN:
echo Cihazinizin ayni Wi-Fi agina bagli oldugundan emin olun.
echo Ardindan tarayiciniza (Chrome, Safari vb.) su adresi yaziniz:
echo.
echo   ------------------------------------------------------
echo      LINK:  http://192.168.1.113:8000
echo   ------------------------------------------------------
echo.
echo (Kapatmak istediginizde bu siyah komut penceresini kapatabilirsiniz.)
echo ====================================================================
echo.
python -m http.server 8000
pause
