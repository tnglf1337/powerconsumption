@echo off
REM Strom.bat - Eine Batch-Datei zum Steuern des Python-Skripts
REM Diese Datei ermöglicht es, Python-Skripte mit Argumenten auszuführen, z.B. strom run, strom set, etc.

REM Python-Skript ausführen mit den übergebenen Argumenten
if /i "%1"=="run" (
    python C:\cstmscripts\stromtarif\main.py run
) else if /i "%1"=="stop" (
    python C:\cstmscripts\stromtarif\main.py stop
) else if /i "%1"=="all" (
    python C:\cstmscripts\stromtarif\main.py all
) else if /i "%1"=="set" (
    REM Den Tarif aus dem zweiten Argument extrahieren
    python C:\cstmscripts\stromtarif\main.py set --tarif=%2
) else if /i "%1"=="help" (
    python C:\cstmscripts\stromtarif\main.py help
) else if /i "%1"=="info" (
    python C:\cstmscripts\stromtarif\main.py info
)

REM Ende der Batch-Datei
exit /b