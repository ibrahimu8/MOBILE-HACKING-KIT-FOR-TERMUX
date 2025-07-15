import os, socket, time, subprocess

SESSION_LOG = "session.log"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def log_event(evt):
    with open(SESSION_LOG, 'a') as f:
        f.write(f"{time.ctime()} - {evt}\\n")

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]; s.close()
        return ip
    except:
        return "127.0.0.1"

def run_cmd(cmd_list, check=False):
    """Run a command safely via subprocess."""
    return subprocess.run(cmd_list, capture_output=True, text=True, check=check)

def check_root():
    if os.name != 'nt' and os.geteuid() != 0:
        print("\\033[1;31m[!] Warning: root is recommended.\\033[0m")
