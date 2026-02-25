# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (STICKY-VISIBLE V36)
# 📅 STATUS: DOM-DOMINATION | 4-AGENT TOTAL | AWS-CPU-LOCK

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- 4 AGENTS TOTAL CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.1, 0.4)    # 🔥 Fast but avoids server shadow-ban
REST_AFTER_STRIKES = 150   
REST_DURATION = 4          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_sticky_payload():
    """Generates a high-authority visible payload that saturates the DOM tree."""
    u_id = random.randint(1000, 9999)
    # \u2060 = Word Joiner | \u2068 = First Strong Isolate
    glue, iso, pop = "\u2060", "\u2068", "\u2069"
    
    # 👑 BRANDING SATURATION
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [LOCK_ID:{u_id}]"
    
    body = []
    # 390 lines to hit the 10,000 character limit
    # This creates a 'Wall of Text' that physically scrolls the opponent off-screen
    for i in range(390):
        # We wrap the visible name in invisible isolates to prevent 'Skip Rendering'
        # The Moon emoji triggers the fallback-font scan on the AWS machine
        line = f"{iso}PRAVEER PAPA ON TOP 🌙 {i}{pop}{glue*15}"
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

def run_life_cycle(agent_id, cookie, target):
    while True:
        driver = get_driver(agent_id)
        try:
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie.strip(), 'path': '/', 'domain': '.instagram.com'})
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(12) 
            
            while True:
                payload = get_sticky_payload()
                try:
                    box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                    # Direct JS injection ensures your bot doesn't lag itself out
                    driver.execute_script("arguments[0].focus(); document.execCommand('insertText', false, arguments[1]);", box, payload)
                    box.send_keys(Keys.ENTER)
                    
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Sticky Strike ({GLOBAL_SENT})")
                except:
                    break # Restart browser if DOM reloads

                time.sleep(random.uniform(*BURST_SPEED))
        except: pass
        finally:
            if driver: driver.quit()
            time.sleep(3)

def main():
    cookie = os.environ.get("INSTA_COOKIE", "").strip()
    target = os.environ.get("TARGET_THREAD_ID", "").strip()
    with ThreadPoolExecutor(max_workers=AGENTS_PER_MACHINE) as executor:
        for i in range(AGENTS_PER_MACHINE):
            executor.submit(run_life_cycle, i+1, cookie, target)

if __name__ == "__main__":
    main()
