import webview
import os
import sys
import json
from datetime import datetime

# --- CONFIGURATION ---
APP_TITLE = "Gemstones Editor Pro"
MAX_Runs = 1  # 1 Free Trial Run
CONTACT_EMAIL = "lakshaywalia132@gmail.com"

# --- HIDDEN CONFIG FILE PATH ---
# We hide the license file in the user's home folder so deleting the app folder won't reset it.
USER_HOME = os.path.expanduser("~")
CONFIG_FILE = os.path.join(USER_HOME, ".gem_sys_config.json")

# --- THE LOCK SCREEN HTML (Red Screen) ---
LOCK_SCREEN_HTML = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            background-color: #1a0505;
            color: white;
            font-family: 'Segoe UI', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            text-align: center;
        }}
        .container {{
            background: #2c0b0b;
            padding: 40px;
            border-radius: 12px;
            border: 2px solid #ff4444;
            box-shadow: 0 0 50px rgba(255, 0, 0, 0.2);
            max-width: 500px;
        }}
        h1 {{ color: #ff4444; font-size: 32px; margin-bottom: 10px; }}
        p {{ color: #cccccc; font-size: 16px; line-height: 1.6; }}
        .box {{
            background: rgba(0,0,0,0.3);
            padding: 15px;
            margin: 20px 0;
            border-radius: 8px;
            font-family: monospace;
            font-size: 14px;
            color: #ffaaaa;
        }}
        button {{
            background: #ff4444;
            color: white;
            border: none;
            padding: 12px 30px;
            font-size: 16px;
            border-radius: 6px;
            cursor: pointer;
            transition: 0.3s;
        }}
        button:hover {{ background: #ff2222; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>⛔ ACCESS DENIED</h1>
        <p>This application's trial license has expired.</p>
        
        <div class="box">
            STATUS: LOCKED<br>
            REASON: USAGE LIMIT REACHED ({MAX_Runs}/{MAX_Runs})
        </div>

        <p>To continue using this software professionally, please contact the developer for a full license key.</p>
        
        <p style="font-weight: bold; color: white;">
            Developer: Lakshay Walia<br>
            Email: {CONTACT_EMAIL}
        </p>

        <button onclick="window.pywebview.api.close_app()">Close Application</button>
    </div>
</body>
</html>
"""

class ConfigManager:
    """Handles the hidden license file securely."""
    
    @staticmethod
    def load_config():
        if not os.path.exists(CONFIG_FILE):
            return {"runs": 0, "installed_date": str(datetime.now())}
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except:
            return {"runs": 100} # Corrupted file = Lock immediately

    @staticmethod
    def save_config(data):
        try:
            with open(CONFIG_FILE, "w") as f:
                json.dump(data, f)
            # Make file hidden on Windows
            if os.name == 'nt':
                os.system(f'attrib +h "{CONFIG_FILE}"')
        except:
            pass

class Api:
    """Python functions callable from Javascript"""
    def close_app(self):
        sys.exit()

def get_html_path():
    """Finds the absolute path to index.html correctly."""
    if getattr(sys, 'frozen', False):
        base_dir = sys._MEIPASS
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_dir, 'assets', 'index.html')

def start_app():
    # 1. Load License Data
    config = ConfigManager.load_config()
    current_runs = config.get("runs", 0)

    # 2. Check Security Logic
    if current_runs >= MAX_Runs:
        # --- LOCKED STATE ---
        webview.create_window(
            "GemEditor Pro - LICENSE EXPIRED", 
            html=LOCK_SCREEN_HTML, 
            width=600, 
            height=500,
            resizable=False,
            js_api=Api()
        )
    else:
        # --- UNLOCKED STATE (Update run count) ---
        config["runs"] = current_runs + 1
        ConfigManager.save_config(config)

        # Find the real HTML file
        file_path = get_html_path()

        if not os.path.exists(file_path):
            webview.create_window("Error", html=f"<h1>Error: Could not find file!</h1><p>Path: {file_path}</p>")
        else:
            webview.create_window(APP_TITLE, url=file_path, width=1400, height=900)

    webview.start()

if __name__ == '__main__':
    start_app()