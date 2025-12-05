import argparse
import sys
import os
from constants import VERSION, BOLD, RESET, RED
from runner_shell import run_shell_command
from runner_playbook import run_playbook
from rich_help_formatter import print_rich_help

def cli():
    parser = argparse.ArgumentParser(description="mgr-ansible-ssh: Remote command execution wrapper using Ansible Runner", add_help=False)
    parser.add_argument("--help", "-h", action="store_true", help="Show the help message and exit")
    parser.add_argument("--version", "-v", action="store_true", help="Show the version and exit")
    parser.add_argument("--inventory", "-i", help="Path to Ansible inventory file to use")
    parser.add_argument("--run", "-r", help="Execute the specified shell command on target hosts")
    parser.add_argument("--playbook", "-p", help="Execute the specified Ansible playbook on target hosts")
    parser.add_argument("--limit", "-l", help="Limit execution to specific hosts or groups")
    parser.add_argument("--forks", "-f", type=int, default=15, help="Number of parallel Ansible forks")
    parser.add_argument("--dry-run", action="store_true", help="Run in Ansible check mode (requires -p or --playbook)")
    parser.add_argument("--no-ansible-output", action="store_true", help="Suppress Ansible stdout output")

    args = parser.parse_args()

    if args.help:
        print_rich_help(parser)
        sys.exit(0)

    if args.version:
        print(f"mgr-ansible-ssh version: {VERSION}")
        sys.exit(0)

    if not args.inventory:
        print(f"{BOLD}{RED}ERROR{RESET}: the '--inventory/-i' argument is required\n")
        print_rich_help(parser)
        sys.exit(1)

    inventory = os.path.abspath(args.inventory)

    if args.run and args.dry_run:
        print(f"{BOLD}{RED}ERROR{RESET}: '--dry-run' is only for playbooks, not for ad-hoc shell commands.\n")
        print_rich_help(parser)
        sys.exit(1)

    if args.run:
        run_shell_command(inventory, args.run, args.forks, args.limit, args.no_ansible_output)
    elif args.playbook:
        run_playbook(inventory, args.playbook, args.dry_run, args.forks, args.limit, args.no_ansible_output)
    else:
        print(f"{BOLD}{RED}ERROR{RESET}: You must provide '--run,-r' or '--playbook,-p'.\n")
        print_rich_help(parser)
        sys.exit(1)
