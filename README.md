# webui-user-selector.bat
Select command line arguments upon starting the sd-webui

For more information on command line arguments that can be used in this .bat file, please refer to this wiki page.
[https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Command-Line-Arguments-and-Settings](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Command-Line-Arguments-and-Settings#all-command-line-arguments)

# How to Edit/Add/Remove Options

**Understanding the .bat File**

In the provided .bat file, there are several options (1-4) that a user can select. Each option corresponds to a different set of commands that will be executed.

**Editing an Option**

To edit an option, you need to change the commands that are executed when that option is selected. For example, if you want to change what happens when option 1 is selected, you would edit the following section:

```bat
) else if errorlevel 1 (
    echo Starting...
    set COMMANDLINE_ARGS= --xformers --autolaunch
)
```
You can replace --xformers --autolaunch with any other command you want to execute.
__________

**Adding an Option**

To add an option, you need to add another ```else if errorlevel``` block. For example, if you want to add an option 5, you would add the following section:
```
) else if errorlevel 5 (
    echo Starting new option...
    set COMMANDLINE_ARGS= --new-option
)
```
__________

**Removing an Option**

To remove an option, simply delete the corresponding ```else if errorlevel``` block.
__________

**Important Note**

Whenever you add or remove an option, remember to update the ```choice /C 1234 /N /M "Choice (1-4): "``` line. The ```/C``` parameter should include all possible choices. For example, if you have 5 options, it should be ```choice /C 12345 /N /M "Choice (1-5): "```.

You can find all possible arguments here: 
