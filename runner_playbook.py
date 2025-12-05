import os
import ansible_runner
from utils import validate_file_exists
from constants import BOLD, RESET, UNDERLINE, RED

def run_playbook(inventory, playbook, dry_run, forks, limit, suppress_output):

    validate_file_exists(inventory)
    validate_file_exists(playbook)

    if suppress_output:
        os.environ["ANSIBLE_STDOUT_CALLBACK"] = "no_output"
        os.environ["ANSIBLE_CALLBACK_PLUGINS"] = "/root/salttoansible/mgr-ansible-ssh/callback-plugins"

    cmdline = f"--connection=ssh --forks {forks}"
    if limit:
        cmdline += f" --limit {limit}"
    if dry_run:
        cmdline += " --check"

    runner = ansible_runner.run(
        private_data_dir="/var/tmp/mgr-ansible-ssh",
        inventory=inventory,
        playbook=playbook,
        extravars={"ansible_become": True, "ansible_python_interpreter": "/usr/bin/python3.6"},
        cmdline=cmdline,
    )

    print(BOLD + UNDERLINE + "\nPLAY SUMMARY\n" + RESET)
    print(runner.stats)

    if runner.rc != 0:
        print(f"\n {BOLD}{RED}ERROR{RESET}: Playbook failed with return code {runner.rc}")
