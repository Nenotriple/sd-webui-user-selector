
import os
settings_file = "webui-user-selector_settings.txt"
batch_file = "webui-user-selector.bat"
SETTINGS_TEMPLATE ='''# This is where you can easily add/remove/edit options within the "webui-user-selector.bat" file.
# It's important to keep the formatting exactly the same if adding/removing/editing this settings file.
# You can use AND to run a separate command. Like "call git pull" to update.

OPTION 1:
- NAME: xformers
- COMMANDLINE_ARGS: --xformers
- DESCRIPTION: Fastest

OPTION 2:
- NAME: xformers + medvram
- COMMANDLINE_ARGS: --xformers --medvram
- DESCRIPTION: Slower

OPTION 3:
- NAME: xformers + lowvram
- COMMANDLINE_ARGS: --xformers --lowvram
- DESCRIPTION: Slowest

OPTION 4:
- NAME: Update
- COMMANDLINE_ARGS: --reinstall-xformers --reinstall-torch --xformers
- DESCRIPTION: git pull, reinstall xformers, reinstall torch
- AND: call git pull
'''

# This function formats a batch script based on the settings provided in a file.
def format_batch_script(settings_file, batch_file):
    # Check if the settings file exists.
    if os.path.exists(settings_file):
        # Open the settings file and read its lines.
        with open(settings_file, 'r') as f:
            lines = f.readlines()
        print("webui-user-selector_settings.txt found!")
        print("\nSettings found:")
        option_number = 1
        # Loop through each line in the settings file.
        for line in lines:
            # Ignore comment lines.
            if line.startswith('#'):
                continue
            # If a line starts with '- NAME:', print it and increment the option number.
            if line.startswith('- NAME:'):
                print(f"{option_number}) NAME {line.split(': ')[1].strip()}")
                option_number += 1
            # If a line starts with '- COMMANDLINE_ARGS:', print it.
            elif line.startswith('- COMMANDLINE_ARGS:'):
                print(f"   COMMANDLINE_ARGS: {line.split(': ')[1].strip()}")
            # If a line starts with '- DESCRIPTION:', print it.
            elif line.startswith('- DESCRIPTION:'):
                print(f"   DESCRIPTION: {line.split(': ')[1].strip()}")
            # If a line starts with '- AND:', print it.
            elif line.startswith('- AND:'):
                print(f"   AND: {line.split(': ')[1].strip()}\n")
            # If a line starts with 'OPTION', print an empty line.
            elif line.startswith('OPTION'):
                print("")
    else:
        # If the settings file does not exist, create a new one with default template.
        print("webui-user-selector_settings.txt not found!")
        with open(settings_file, 'w') as f:
            f.write(SETTINGS_TEMPLATE)
        print("A new webui-user-selector_settings.txt file has been created with the default template.")
        print("Please edit this settings file with the options you want, and run 'webui-user-selector_EDITOR.py' again.")
        input('Press ENTER to exit')
        return

    # Ask the user if they want to alter the batch file with the settings provided in the settings file.
    user_input = input("Do you want to alter your 'webui-user-selector.bat' with the settings provided in the 'webui-user-selector_settings.txt' file? (Yes/No): ")
    if user_input.lower() not in ['yes', 'y']:
        print("No changes made.")
        return
    option_block = []
    option = {}
    for line in lines:
        # If a line starts with 'OPTION', append the current option to options and start a new option block.
        if line.startswith('OPTION'):
            if option:
                option_block.append(option)
            option = {}
        # If a line starts with '- NAME:', add it to the current option.
        elif line.startswith('- NAME:'):
            option['name'] = line.split(': ')[1].strip()
        # If a line starts with '- COMMANDLINE_ARGS:', add it to the current option.
        elif line.startswith('- COMMANDLINE_ARGS:'):
            option['args'] = line.split(': ')[1].strip()
        # If a line starts with '- DESCRIPTION:', add it to the current option.
        elif line.startswith('- DESCRIPTION:'):
            option['desc'] = line.split(': ')[1].strip()
        # If a line starts with '- AND:', add it to the current option.
        elif line.startswith('- AND:'):
            option['and'] = line.split(': ')[1].strip()
    if option:
        option_block.append(option)

    # Open the batch file for writing.
    with open(batch_file, 'w') as f:
        f.write('@echo off\n\n')
        f.write('set PYTHON=\n')
        f.write('set GIT=\n')
        f.write('set VENV_DIR=\n\n')
        f.write('echo Please select an option:\n\n')

        # Write each option to the batch file.
        for i, option in enumerate(option_block, start=1):
            f.write(f'echo {i}) {option["name"]} ({option["desc"]})\n')

        # Create a string of choices by joining the string representation of each option number.
        choices = ''.join(str(i) for i in range(1, len(option_block) + 1))
        # Write the choices to the batch file.
        f.write(f'\nchoice /C {choices} /N /M "Choice (1-{len(option_block)}): "\n\n')

        # Loop through each option in reverse order.
        for i, option in reversed(list(enumerate(option_block, start=1))):
            # If it's the last option, write 'if errorlevel {i} (' to the batch file.
            if i == len(option_block):
                f.write(f'if errorlevel {i} (\n')
            # Otherwise, write ') else if errorlevel {i} (' to the batch file.
            else:
                f.write(f') else if errorlevel {i} (\n')
            # Write 'echo Starting...' and 'set COMMANDLINE_ARGS= {option["args"]}' to the batch file.
            f.write(f'    echo Starting...\n')
            f.write(f'    set COMMANDLINE_ARGS= {option["args"]}\n')
            # If 'and' is in the option, write it to the batch file.
            if 'and' in option:
                f.write(f'    {option["and"]}\n')

        # Write ')', 'call webui.bat', and a newline to the batch file.
        f.write(')\n\ncall webui.bat\n')

        # Print a message indicating that the batch file has been formatted.
        print("webui-user-selector.bat formatted!")
        print('All Done!')
        input('Press ENTER to exit')

# Call the function with 'webui-user-selector_settings.txt' and 'webui-user-selector.bat' as arguments.
format_batch_script(settings_file, batch_file)