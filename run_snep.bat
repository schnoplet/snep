@echo off
title SNEP Demo Launcher
setlocal

echo Starting node1 server...
start "Node1" cmd /k python -W ignore nodes\node1.py

echo Starting node2 server...
start "Node2" cmd /k python -W ignore nodes\node2.py

REM wait for servers to initialize
timeout /t 4 /nobreak >nul

echo Running demo client...
python -W ignore demo\demo_app.py

echo Demo finished.
pause