import subprocess


def run_wsl_command(command):
    command = command.strip()
    if command == "sudo reboot":
        print("To restart wsl please use windows power shell typing 'wsl --shutdown'")
        return
    try:
        subprocess.run(command, shell=True , check=True)
    except subprocess.CalledProcessError as e: 
        print(f"Command '{command}' failed with return code {e.returcode} ")


with open("commands.txt","r") as fh: 
    cmds = fh.readlines()
    for item in cmds:
        command = item.strip()
        if command: 
            run_wsl_command(command)
