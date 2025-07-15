#!/usr/bin/env python3
import os, sys, time, random
from phishing import start_phishing
from wireless import run_wireless
from exploit import run_exploits
from utils import clear, log_event, check_root

CREDS_FILE = "creds.json"
SESSION_FILE = "session.log"

def matrix_effect(lines=15, duration=2):
    charset = "01█▓▒░"
    columns = os.get_terminal_size().columns
    end_time = time.time() + duration
    while time.time() < end_time:
        line = "".join(random.choice(charset) for _ in range(columns))
        print(f"\033[1;32m{line}\033[0m")
        time.sleep(0.05)
    clear()

def banner():
    print("""\033[1;32m
███╗   ███╗ ██████╗ ██████╗ ███████╗████████╗
████╗ ████║██╔═══██╗██╔══██╗██╔════╝╚══██╔══╝
██╔████╔██║██║   ██║██████╔╝███████╗   ██║   
██║╚██╔╝██║██║   ██║██╔══██╗╚════██║   ██║   
██║ ╚═╝ ██║╚██████╔╝██║  ██║███████║   ██║   
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝

        \033[1;33mMOBILE OFFENSIVE BATTLEGROUND v4.0
            -- MOBSET TOOLKIT --
    [!] Educational Use ONLY [!]
\033[0m""")

def main_menu():
    clear()
    banner()
    print("""
\033[1;36m[1] Phishing Attacks
[2] Wireless Attacks
[3] Exploit Framework
[4] View Captured Credentials
[5] View Session Logs
[6] Update Toolkit
[0] Exit\033[0m
""")
    return input("mobSET> ")

def view_file(file, label):
    if os.path.isfile(file):
        print(f"\n\033[1;32m{label}:\033[0m\n")
        os.system(f"cat {file}")
    else:
        print(f"\033[1;31m[!] No {label.lower()} found.\033[0m")
    input("\nPress Enter to return...")

def update_toolkit():
    print("\033[1;32m[+] Checking for updates...\033[0m")
    os.system("git pull && pip install -r requirements.txt")
    log_event("Toolkit updated via git pull")
    print("\033[1;32m[+] Toolkit updated!\033[0m")
    time.sleep(2)

def main():
    check_root()
    matrix_effect(lines=15, duration=3)
    log_event("mobSET session started")

    while True:
        try:
            choice = main_menu()
            if choice == "1":
                start_phishing()
            elif choice == "2":
                run_wireless()
            elif choice == "3":
                run_exploits()
            elif choice == "4":
                view_file(CREDS_FILE, "Captured Credentials")
            elif choice == "5":
                view_file(SESSION_FILE, "Session Logs")
            elif choice == "6":
                update_toolkit()
            elif choice == "0":
                log_event("mobSET exited normally")
                print("\033[1;33m[!] Exiting MOBSET Toolkit. Stay ethical.\033[0m")
                sys.exit(0)
            else:
                print("\033[1;31m[!] Invalid choice.\033[0m")
        except KeyboardInterrupt:
            print("\n\033[1;33m[!] Interrupted. Exiting safely.\033[0m")
            log_event("Session interrupted")
            sys.exit(0)

if __name__ == "__main__":
    main()
