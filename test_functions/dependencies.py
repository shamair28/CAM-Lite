import subprocess
import sys

def install_package(package_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

def check_and_install_dependencies():
    dependencies = ["pypandoc", "tiktoken", "openai"]

    print("here")

    for package in dependencies:
        try:
            __import__(package)
        except ImportError:
            print(f"{package} not found. Installing...")
            install_package(package)

