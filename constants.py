import uuid
import os
from datetime import datetime

VERSION = "1.0.0"

BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"
RED = "\033[31m"
INDENT = "    "

DATE = datetime.now().strftime("%Y%m%d")
RUN_ID = str(uuid.uuid4())
RUNNER_DIR = f"/var/log/mgr-ansible-ssh/{DATE}/{RUN_ID}"
os.makedirs(RUNNER_DIR, exist_ok=True)

os.environ["ANSIBLE_SSH_TRANSFER_METHOD"] = "piped"
os.environ["ANSIBLE_INVENTORY_UNPARSED_WARNING"] = "False"
os.environ["ANSIBLE_SSH_RETRIES"] = "1"
