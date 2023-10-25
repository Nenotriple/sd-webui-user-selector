# webui-user-selector.bat
Select command-line arguments when starting AUTOMATIC1111's sd-webui

![webui-user-selector_example](https://github.com/Nenotriple/webui-user-selector/assets/70049990/6a82b5fa-529e-4570-baf2-135b3368818d)

For more information on command-line arguments that can be used in this .bat file, please refer to this wiki page.

[AUTOMATIC1111 sd-webui - Command-Line Arguments and Settings](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Command-Line-Arguments-and-Settings#all-command-line-arguments)

# How to use

Simply place the webui-user-selector.bat file in the "stable-diffusion-webui" folder and double-click it.

*(There's no need to replace the original webui-user.bat file)*

# 🍰 _EASY WAY:_ Edit/Add/Remove Options

1. Download the included Python script `webui-user-selector_EDITOR.py`, and run it once to create the settings template.

2. Edit the `webui-user-selector_settings.txt` file with the options you want.
   - Follow the provided pattern (it's easy).
   - You can simply copy the `Option` blocks or delete them; just make sure they're numbered correctly.
   - Use `AND` to run another command, like `call git pull`.

3. When you're done, run the Python script again to create/edit the `webui-user-selector.bat` file.


# ⛰️ _HARD WAY:_ Edit/Add/Remove Options

**Understanding the .bat File**

In the provided .bat file, there are several options (1-4) that a user can select. Each option corresponds to a different set of commands that will be executed.

_Here is the full example batch script:_
```
@echo off

set PYTHON=
set GIT=
set VENV_DIR=

echo Please select an option:

echo 1) xformers                        (Fastest)
echo 2) xformers + medvram              (Slower)
echo 3) xformers + lowvram              (Slowest)
echo 4) Update                          (git pull, reinstall xformers, reinstall torch)

choice /C 1234 /N /M "Choice (1-4): "

if errorlevel 4 (
    echo Updating...
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
```

**Editing an Option**

Right click the .bat file and select Edit.

To edit an option, you need to change the commands that are executed when that option is selected. For example, if you want to change what happens when option 1 is selected, you would edit the following section:

```bat
) else if errorlevel 1 (
    echo Starting...
    set COMMANDLINE_ARGS= --xformers
)
```

You can replace --xformers with any other command you want to execute, or add additional commands.

After editing the  `else if errorlevel` block you should update the `echo` line that corresponds to the option name.
__________

**Adding an Option**

To add an option, you need to add another `else if errorlevel` block. For example, if you want to add an option 5, you would add the following section:

```
) else if errorlevel 5 (
    echo Starting...
    set COMMANDLINE_ARGS= --new-option
)
```

After adding a new option you should update/add the `echo` line that corresponds to the option name.
__________

**Removing an Option**

To remove an option, simply delete the corresponding `else if errorlevel` block. Then update the appropriate `echo` and `choice` lines.
__________

**Important Note**

Whenever you add or remove an option, remember to update the `choice /C 1234 /N /M "Choice (1-4): "` line. The `/C` parameter should include all possible choices. For example, if you have 5 options, it should be `choice /C 12345 /N /M "Choice (1-5): "`.
