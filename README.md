# webui-user-selector.bat
Select command line arguments upon starting the sd-webui

For more information on command line arguments that can be used in this .bat file, please refer to this wiki page.
[https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Command-Line-Arguments-and-Settings](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Command-Line-Arguments-and-Settings#all-command-line-arguments)

# How to use

Simply place the webui-user-selector.bat file in the "stable-diffusion-webui" folder and double click it.

*(There's no need to replace the original webui-user.bat file)*

# Edit/Add/Remove Options

**Understanding the .bat File**

In the provided .bat file, there are several options (1-4) that a user can select. Each option corresponds to a different set of commands that will be executed.

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

After editing the  ```else if errorlevel``` block you should update the ```echo``` line that corresponds to the option name.
__________

**Adding an Option**

To add an option, you need to add another ```else if errorlevel``` block. For example, if you want to add an option 5, you would add the following section:
```
) else if errorlevel 5 (
    echo Starting new option...
    set COMMANDLINE_ARGS= --new-option
)
```
After adding a new option you should update/add the ```echo``` line that corresponds to the option name.
__________

**Removing an Option**

To remove an option, simply delete the corresponding ```else if errorlevel``` block. Then update the appropriate ```echo``` and ```choice``` lines
__________

**Important Note**

Whenever you add or remove an option, remember to update the ```choice /C 1234 /N /M "Choice (1-4): "``` line. The ```/C``` parameter should include all possible choices. For example, if you have 5 options, it should be ```choice /C 12345 /N /M "Choice (1-5): "```.
