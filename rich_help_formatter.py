from argparse import ArgumentParser
from rich.console import Console

console = Console()

def print_rich_help(parser: ArgumentParser):

    if parser.description:
        desc = parser.description.replace(
            "mgr-ansible-ssh", "[bold green]mgr-ansible-ssh[/bold green]"
        )
        console.print(desc)

    usage = parser.format_usage().replace("usage: ", "")
    console.print(f"\n[bold green]Usage:[/bold green] {usage}")

    required = []
    run_or_playbook = []
    optional = []

    for a in parser._actions:
        dest = a.dest

        if dest == "inventory":
            required.append(a)
        elif dest in ("run", "playbook"):
            run_or_playbook.append(a)
        else:
            optional.append(a)

    def build_option_string(action):
        return ", ".join(action.option_strings) if action.option_strings else action.dest

    all_actions = required + run_or_playbook + optional
    max_width = max(len(build_option_string(a)) for a in all_actions)

    if required:
        console.print("\n[bold green]Required Arguments[/bold green]")
        for a in required:
            opt = build_option_string(a)
            console.print(f"[bold white]{opt.ljust(max_width)}[/bold white]  {a.help}")

    if run_or_playbook:
        console.print("\n[bold green]Any One of the Arguments Is Required[/bold green]")
        for a in run_or_playbook:
            opt = build_option_string(a)
            console.print(f"[bold white]{opt.ljust(max_width)}[/bold white]  {a.help}")

    if optional:
        console.print("\n[bold green]Optional Arguments[/bold green]")
        for a in optional:
            opt = build_option_string(a)
            helptext = a.help or ""
            console.print(f"[bold white]{opt.ljust(max_width)}[/bold white]  {helptext}")
