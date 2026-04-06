@echo off
echo ==========================================
echo  DAMICH Backend — Instalacion y arranque
echo ==========================================
echo.

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no encontrado. Instala Python 3.11+ desde python.org
    pause
    exit /b 1
)

REM Crear entorno virtual si no existe
if not exist ".venv" (
    echo Creando entorno virtual...
    python -m venv .venv
)

REM Activar entorno
call .venv\Scripts\activate.bat

REM Instalar dependencias
echo Instalando dependencias...
pip install -r requirements.txt --quiet

echo.
echo ==========================================
echo  Servidor corriendo en: http://localhost:8001
echo  Documentacion en:      http://localhost:8001/docs
echo  Presiona Ctrl+C para detener
echo ==========================================
echo.

python main.py
pause
