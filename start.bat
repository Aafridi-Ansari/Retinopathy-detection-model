@echo off
title RetinaXAI - Explainable AI for Diabetic Retinopathy
echo ========================================================
echo Launching RetinaXAI Rural Eye Screening Application...
echo ========================================================
python server.py
if errorlevel 1 (
    echo Python not found, opening index.html directly in your default browser...
    start index.html
)
pause
