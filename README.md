# mgr-ansible-ssh

<p align="center">
  <img src="https://github.com/deve5h/mgr-ansible-ssh/blob/git/image/mgr-ansible-ssh.jpeg" alt="mgr-ansible-ssh" width="500"/>
  <br>
  <b>mgr-ansible-ssh</b>
</p>

**Version:** v1.0.1

---

## Project Overview

**mgr-ansible-ssh** is a unified CLI wrapper/tool designed to execute both ad-hoc shell commands and Ansible playbooks across multiple remote hosts, providing a consistent and CI-friendly experience. Unlike standard Ansible, which prints raw stdout directly to the terminal, this tool focuses on delivering **structured, colored, and precise output** while maintaining execution artifacts. Each run generates unique logs under `/var/log/<date>/<UUID>`, enabling multiple users to execute commands simultaneously on the same VM without conflicts.

### Key Features / Differentiators

- **Unified Interface:** Same command syntax for ad-hoc shell commands and playbooks.  
- **Smart Artifact Management:** Automatic creation of per-run directories for logs and outputs.  
- **Seamless SSH Usage:** Leverages existing key-based authentication; no extra keys needed (unlike `mgr-salt-ssh`).  
- **Selective Host Execution:** Supports regex-based host filtering (`--limit`) and parallel execution (`--forks`), speeding up tasks by up to 5x compared to similar tools.  
- **Enhanced Usability:** Optional flags like `--dry-run` and `--no-ansible-output` improve usability for automation.  
- **Reduced Dependencies:** No reliance on taskomatic or other external schedulers (unlike `mgr-salt-ssh`).  

> In summary, **mgr-ansible-ssh** does not replace Ansible—it enhances it. It simplifies execution, enforces standards, and provides a cleaner, more reliable experience for multi-host operations.

---

## Requirements / Installation

This tool has been tested on Python v3.6.15. Clone the repository and run 'pip install -r requirements.txt' to insall dependecies and get started.

## Usage Examples

- ./mgr-ansible-ssh -i inventory_file -r 'df -hT' -f 25 -l '*-VM' --no-ansible-output
- ./mgr-ansible-ssh -i inventory_file -p playbook.yml --dry-run -f 40
