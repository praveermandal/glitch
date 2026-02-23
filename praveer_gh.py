# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (GH-FIXED)
# 📅 STATUS: URL VALIDATED | SCRIPT BY PRAVEER

import os, sys, asyncio, json, time, random
from playwright.async_api import async_playwright

# --- CONFIG FROM SECRETS ---
SID = os.getenv("SESSION_ID")
URL = os.getenv("GROUP_URL")
TARGET = os.getenv("TARGET_NAME", "Target")
CREDITS = "SCRIPT BY PRAVEER"

def get_random_payload(target):
    bloat_chars = ["‎", "‏", "‌", "‍"]
    bloat = "".join(random.choice(bloat_chars) for _ in range(random.randint(300, 600)))
    zalgo = "p̸r̸a̸v̸e̸e̸r̸" * random.randint(5, 10)
    return f"({target}) {bloat}\n{zalgo}\n" + "🛑" * random.randint(5, 10)

async def worker(context, agent_id):
    page = await context.new_page()
    try:
        # Check if URL is valid before moving
        if not URL or not URL.startswith("http"):
            print(f"Agent {agent_id} Error: GROUP_URL is empty or invalid!")
            return

        print(f"Agent {agent_id} | Connecting to Chat...")
        # Using 'commit' instead of 'domcontentloaded' to avoid GH Action timeouts
        await page.goto(URL, wait_until='commit', timeout=90000)
        
        msg_input = page.locator('div[aria-label="Message"][role="textbox"]')
        await msg_input.wait_for(timeout=45000)

        for i in range(50):
            payload = get_random_payload(TARGET)
            await msg_input.evaluate(f'(el, text) => {{ el.innerText = text; el.dispatchEvent(new Event("input", {{ bubbles: true }})); }}', payload)
            await page.keyboard.press("Enter")
            
            # Print to GH Logs
            if (i + 1) % 5 == 0:
                print(f"Agent {agent_id} | Progress: {i+1}/50 | {CREDITS}")
            
            await asyncio.sleep(random.uniform(0.5, 1.0))
    except Exception as e:
        print(f"Agent {agent_id} Exception: {str(e)}")

async def main():
    if not SID:
        print("❌ ERROR: SESSION_ID secret is missing!")
        return
    if not URL:
        print("❌ ERROR: GROUP_URL secret is missing!")
        return

    async with async_playwright() as p:
        # Launching with specific GH Runner flags
        browser = await p.chromium.launch(headless=True, args=[
            '--no-sandbox', 
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage'
        ])
        context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
        
        await context.add_cookies([{"name": "sessionid", "value": SID, "domain": ".instagram.com", "path": "/", "secure": True}])

        # 3 Agents are safer for GitHub's limited CPU
        tasks = [worker(context, i+1) for i in range(3)]
        await asyncio.gather(*tasks)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
