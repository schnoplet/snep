@echo off
setlocal

REM --- start node1 ---
start "" cmd /k "python nodes/node1.py 5000"

REM --- start node2 ---
start "" cmd /k "python nodes/node2.py 5001"

REM --- wait a few seconds for servers to start ---
timeout /t 3 /nobreak >nul

REM --- run demo client ---
python demo/demo_app.py

pause