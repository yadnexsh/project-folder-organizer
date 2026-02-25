


import os
import shutil
import sys
from datetime import datetime
from tqdm import tqdm
from colorama import Fore, Style, init

init(autoreset=True)

# ------------------------------------------

def help():
    help_text = """
PHOTO / FOLDER ORGANIZER – HELP
----------------------------------

USAGE:
    python main.py <directory_path> [flags]

EXAMPLES:
    python main.py ./photos --organize
    python main.py ./photos --organize --dry-run
    python main.py ./photos --ls
    python main.py ./photos --help

AVAILABLE FLAGS:
    --help        Show this help menu
    --ls          List all files and folders inside the given directory
    --organize    Organize folders based on 'Main - Sub' naming pattern
    --dry-run     Preview what would happen without making any changes
----------------------------------
"""
    print(help_text)
    
input_directory = r"H:\Gamut\Projects\project-folder-organizer\test_input"

# -----  FOLDER PATHS ------
def get_folder_paths():
    """
    Prints full paths of all files and folders inside `input_directory`.
    Exits the program if the directory does not exist.
    """
    if not os.path.exists(input_directory):
        print(Fore.RED + f"'{input_directory}' not found.")
        sys.exit(0)
        
    for folders in os.listdir(input_directory):
        path = os.path.join(input_directory, folders)
        if os.path.isdir(path):
            print(path)
        
    return path
folder_paths = get_folder_paths()
        

# ---- LOGGING SYSTEM ------

def logs(log_file, log):
    """
    Appends the given log message to the specified log file.
    Prints the exception if writing fails.
    """
    try:
        with open(log_file, "a") as file:
            file.write(log)
    except Exception as e:
        print(f"{e}")

def verbose(verbose_log_file, verbose_log):
    """
    Appends detailed (verbose) log content to the specified file.
    Prints the exception if writing fails.
    """
    try:
        with open(verbose_log_file, "a") as file:
            file.write(verbose_log)
    except Exception as e:
        print(f"{e}")
        
# ------- UNIQUE FOLDER NAME -------

# def get_folder_components():
#     prefix = []
#     suffix = []
    
#     print(f"NEW - {folder_paths}")
    
# get_folder_components()