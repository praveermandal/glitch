# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (GH-ACTIONS EDITION)
# 📅 STATUS: BYPASS ENABLED | SCRIPT BY PRAVEER

import os, sys, asyncio, json, time, random
from playwright.async_api import async_playwright

# --- CONFIG FROM SECRETS ---
SID = os.getenv("SESSION_ID")
URL = os.getenv("GROUP_URL")
TARGET = os.getenv("TARGET_NAME")
CREDITS = "SCRIPT BY PRAVEER"

def get_random_payload(target):
    bloat_chars = ["‎", "‏", "‌", "‍", "‎"]
    bloat = "".join(random.choice(bloat_chars) for _ in range(random.randint(400, 700)))
    zalgo = "p̸r̸a̸v̸e̸e̸r̸" * random.randint(5, 12)
    return f"({target}) {bloat}\n{zalgo}\n" + "🛑" * random.randint(10, 20)

async def worker(context, agent_id):
    page = await context.new_page()
    try:
        await page.goto(URL, wait_until='domcontentloaded', timeout=60000)
        msg_input = page.locator('div[aria-label="Message"][role="textbox"]')
        await msg_input.wait_for(timeout=30000)

        for i in range(50): # Send 50 blocks per cycle
            payload = get_random_payload(TARGET)
            await msg_input.evaluate(f'(el, text) => {{ el.innerText = text; el.dispatchEvent(new Event("input", {{ bubbles: true }})); }}', payload)
            await page.keyboard.press("Enter")
            print(f"Agent {agent_id} | Sent: {i+1} | {CREDITS}")
            await asyncio.sleep(random.uniform(0.4, 0.7))
    except Exception as e:
        print(f"Agent {agent_id} stopped: {e}")

async def main():
    if not SID or not URL:
        print("Missing Secrets! Add SESSION_ID and GROUP_URL to GitHub.")
        return

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=['--no-sandbox'])
        context = await browser.new_context()
        await context.add_cookies([{"name": "sessionid", "value": SID, "domain": ".instagram.com", "path": "/", "secure": True}])

        # GH Actions works best with 3-5 concurrent agents
        tasks = [worker(context, i+1) for i in range(5)]
        await asyncio.gather(*tasks)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
