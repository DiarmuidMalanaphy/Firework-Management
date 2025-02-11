@echo off
cd /d "%~dp0"

:: Run with python - I know Mairtin's got a confusing Python build so I'll try all the different versions of python.
python3 main.py
IF %ERRORLEVEL% NEQ 0 (
    echo python3 failed, trying py -m...
    py -m main
    IF %ERRORLEVEL% NEQ 0 (
        echo py -m failed, trying python...
        python main.py
        IF %ERRORLEVEL% NEQ 0 (
            echo All attempts failed. Make sure Python is installed and accessible.
            pause
            exit /b 1
        )
    )
)

pause

