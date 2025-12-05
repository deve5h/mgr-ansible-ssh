import ansible_runner
from constants import RUNNER_DIR, BOLD, RESET, RED
from utils import validate_file_exists, set_suppress_env
from output import extract_host_output, print_execution_summary, print_individual_output

def run_shell_command(inventory, command, forks, limit, suppress_output):

    validate_file_exists(inventory)

    if suppress_output:
        set_suppress_env()

    cmdline = f"--connection=ssh --forks {forks}"
    if limit:
        cmdline += f" --limit {limit}"

    runner = ansible_runner.run(
        private_data_dir=RUNNER_DIR,
        inventory=inventory,
        host_pattern='all',
        module='ansible.builtin.shell',
        module_args=command,
        extravars={"ansible_become": True, "ansible_python_interpreter": "/usr/bin/python3.6"},
        cmdline=cmdline,
        quiet=suppress_output,
    )

    print_execution_summary(runner.stats)

    if runner.rc != 0:
        print(f"\n {BOLD}{RED}ERROR{RESET}: Command failed with return code {runner.rc}")

    host_output = extract_host_output(runner)

    if not host_output:
        print("\n No output returned from hosts.")
        return

    print_individual_output(host_output)
