@echo off
echo ================================================
echo    Finans Pro - EXE Olusturucu
echo ================================================
echo.
echo PyInstaller ile tek dosya EXE olusturuluyor...
echo.

pyinstaller --onefile --windowed --name FinansPro --icon=icon.ico --clean main.py

echo.
echo ================================================
echo    Tamamlandi!
echo ================================================
echo.
echo EXE dosyasi: dist\FinansPro.exe
echo.
pause
