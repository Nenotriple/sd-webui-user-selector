@echo off

set PYTHON=
set GIT=
set VENV_DIR=

echo Please select an option:

echo 1) xformers (Fastest)
echo 2) xformers + medvram (Slower)
echo 3) xformers + lowvram (Slowest)
echo 4) Update (git pull, reinstall xformers, reinstall torch)

choice /C 1234 /N /M "Choice (1-4): "

if errorlevel 4 (
    echo Starting...
    set COMMANDLINE_ARGS= --reinstall-xformers --reinstall-torch --xformers
    call git pull
) else if errorlevel 3 (
    echo Starting...
    set COMMANDLINE_ARGS= --xformers --lowvram
) else if errorlevel 2 (
    echo Starting...
    set COMMANDLINE_ARGS= --xformers --medvram
) else if errorlevel 1 (
    echo Starting...
    set COMMANDLINE_ARGS= --xformers
)

call webui.bat
