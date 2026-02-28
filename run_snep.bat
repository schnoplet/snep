@echo off
setlocal

REM --- start node1 ---
start "" cmd /k "python -W ignore -m nodes.node1 5000"

REM --- start node2 ---
start "" cmd /k "python -W ignore -m nodes.node2 5001"

REM --- wait a few seconds for servers to start ---
timeout /t 3 /nobreak >nul

REM --- run demo client ---
python -W ignore -m demo.demo_app

pause