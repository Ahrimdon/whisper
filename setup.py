import os
import subprocess
import venv

def create_venv():
    venv.create('venv', with_pip=True)
    # Create activation scripts
    with open("venv.ps1", "w") as f:
        f.write("venv\\Scripts\\Activate.ps1")

    with open("venv.bat", "w") as f:
        f.write("venv\\Scripts\\activate.bat")

def create_uninstall_scripts():
    # Create uninstall scripts for PowerShell and Batch
    with open("uninstall.ps1", "w") as f:
        f.write("Remove-Item -Recurse -Force venv\n")
        f.write("Remove-Item venv.ps1\n")
        f.write("Remove-Item venv.bat\n")

    with open("uninstall.bat", "w") as f:
        f.write("rd /s /q venv\n")
        f.write("del venv.bat\n")
        f.write("del venv.ps1\n")

def update_pip():
    subprocess.check_call([os.path.join('venv', 'Scripts', 'python'), '-m', 'pip', 'install', '--upgrade', 'pip'])

def install_requirements_in_venv():
    subprocess.check_call([os.path.join('venv', 'Scripts', 'pip'), 'install', '-r', 'requirements.txt'])

def build_whisper():
    subprocess.check_call([os.path.join('venv', 'Scripts', 'python'), 'setup_whisper.py', 'build'])

def setup_whisper():
    subprocess.check_call([os.path.join('venv', 'Scripts', 'python'), 'setup_whisper.py', 'install'])

if __name__ == "__main__":
    create_venv()
    update_pip()
    install_requirements_in_venv()
    build_whisper()
    setup_whisper()
    create_uninstall_scripts()