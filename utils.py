import os
import sys
from constants import BOLD, RESET, RED

def validate_file_exists(path):
    if not os.path.exists(path):
        print(f"{BOLD}{RED}ERROR{RESET}: Inventory file not found: {path}")
        sys.exit(1)

def set_suppress_env():
    os.environ["ANSIBLE_STDOUT_CALLBACK"] = "minimal"
    os.environ["ANSIBLE_DISPLAY_OK_HOSTS"] = "no"
    os.environ["ANSIBLE_DISPLAY_SKIPPED_HOSTS"] = "no"
    os.environ["ANSIBLE_DISPLAY_FAILED_HOSTS"] = "no"
    os.environ["ANSIBLE_DISPLAY_CHANGED"] = "no"
