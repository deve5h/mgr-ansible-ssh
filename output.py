from constants import BOLD, UNDERLINE, RESET, INDENT

def extract_host_output(runner_obj):
    host_stdout = {}
    for event in runner_obj.events:
        if not isinstance(event, dict):
            continue

        data = event.get("event_data", {})
        host = data.get("host")
        res = data.get("res", {})
        if not host:
            continue

        output = (
            res.get("stdout") or
            res.get("stdout_lines") or
            res.get("msg")
        )
        if not output:
            continue

        host_stdout.setdefault(host, [])
        if isinstance(output, list):
            host_stdout[host].extend(output)
        else:
            host_stdout[host].append(output)

    return host_stdout

def print_execution_summary(stats):
    print(BOLD + UNDERLINE + "\nEXECUTION SUMMARY\n" + RESET)

    for section, hosts in (stats or {}).items():
        section_header = f"{BOLD}{section}{RESET}"

        if not hosts:
            print(f"{section_header}: NONE")
            continue

        print(f"{section_header}:")
        if isinstance(hosts, dict):
            for host, value in hosts.items():
                print(f"  - {host}: {value}")
        else:
            print(f"  {hosts}")


def print_individual_output(host_output):
    print(BOLD + UNDERLINE + "\nINDIVIDUAL HOST OUTPUT\n" + RESET)

    for host, outputs in host_output.items():
        print(f"- {BOLD}{host}{RESET}")
        for item in outputs:
            for line in item.splitlines():
                print(INDENT + line.lstrip())
        print()
