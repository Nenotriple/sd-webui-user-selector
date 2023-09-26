@echo off

set PYTHON=
set GIT=
set VENV_DIR=

echo Please select an option:

echo 1) xformers                        (Fastest)
echo 2) xformers + medvram              (Slower, upscale larger images)
echo 3) xformers + lowvram              (Slowest, least limited)
echo 4) Update                          (git pull, reinstall xformers, reinstall torch)

choice /C 1234 /N /M "Choice (1-4): "

if errorlevel 4 (
    echo Updating...
    set COMMANDLINE_ARGS= --reinstall-xformers --reinstall-torch --xformers --autolaunch
    call git pull
) else if errorlevel 3 (
    echo Starting...
    set COMMANDLINE_ARGS= --xformers --autolaunch --lowvram
) else if errorlevel 2 (
    echo Starting...
    set COMMANDLINE_ARGS= --xformers --autolaunch --medvram
) else if errorlevel 1 (
    echo Starting...
    set COMMANDLINE_ARGS= --xformers --autolaunch
)

call webui.bat
