@echo off
echo Starting node1 server...
start cmd /k python -m nodes.node1

timeout /t 2

echo Starting node2 server...
start cmd /k python -m nodes.node2

timeout /t 2

echo Running demo client...
python -W ignore -m demo.demo_app

pause