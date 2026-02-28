@echo off
setlocal

echo Starting node1 server...
start "Node1" cmd /k "python nodes\node1.py"

echo Starting node2 server...
start "Node2" cmd /k "python nodes\node2.py"

timeout /t 3 /nobreak >nul

echo Running demo client...
python demo\demo_app.py

echo Demo finished.
pause