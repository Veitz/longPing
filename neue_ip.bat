@echo off
echo IP-Adresse wird freigegeben...
ipconfig /release
echo.
echo Neue IP-Adresse wird angefordert...
ipconfig /renew
echo.
echo Vorgang abgeschlossen.
ipconfig /all | findstr "IPv4"
pause
