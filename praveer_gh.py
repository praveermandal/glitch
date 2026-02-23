# -*- coding: utf-8 -*-
# 🚀 PROJECT: PRAVEER NC (ETERNAL BLAZE)
# 📅 STATUS: INFINITE | 2 AGENTS | 200ms | SCRIPT BY PRAVEER

import os, sys, asyncio, json, time, random
from playwright.async_api import async_playwright

# --- CONFIG FROM SECRETS ---
SID = os.getenv("SESSION_ID")
URL = os.getenv("GROUP_URL")
TARGET = os.getenv("TARGET_NAME", "Target")
CREDITS = "SCRIPT BY PRAVEER"

# Global counter for all agents
total_sent = 0
counter_lock = asyncio.Lock()

def get_random_payload(target):
    bloat_chars = ["‎", "‏", "‌", "‍"]
    bloat = "".join(random.choice(bloat_chars) for _ in range(random.randint(300, 600)))
    zalgo = "p̸r̸a̸v̸e̸e̸r̸" * random.randint(5, 10)
    return f"({target}) {bloat}\n{zalgo}\n" + "🛑" * random.randint(5, 10)

async def worker(context, agent_id, stop_event):
    global total_sent
    page = await context.new_page()
    try:
        print(f"Agent {agent_id} | 🚀 Connecting...")
        await page.goto(URL, wait_until='commit', timeout=90000)
        
        msg_input = page.locator('div[aria-label="Message"][role="textbox"]')
        await msg_input.wait_for(timeout=45000)

        # Loop until the 2-minute timer hits
        while not stop_event.is_set():
            payload = get_random_payload(TARGET)
            
            # 200ms Delay logic included in the interval
            await msg_input.evaluate(f'(el, text) => {{ el.innerText = text; el.dispatchEvent(new Event("input", {{ bubbles: true }})); }}', payload)
            await page.keyboard.press("Enter")
            
            async with counter_lock:
                total_sent += 1
                # Prints every message for live tracking
                print(f"[{total_sent}] Agent {agent_id} Sent | {CREDITS}")
            
            await asyncio.sleep(0.2) # 200ms Delay
            
    except Exception as e:
        print(f"Agent {agent_id} Exception: {str(e)}")

async def main():
    if not SID or not URL:
        print("❌ MISSING SECRETS!")
        return

    while True: # Infinite Process Loop
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True, args=['--no-sandbox', '--disable-dev-shm-usage'])
            context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
            await context.add_cookies([{"name": "sessionid", "value": SID, "domain": ".instagram.com", "path": "/", "secure": True}])

            stop_event = asyncio.Event()
            
            # Start 2 Agents
            tasks = [
                asyncio.create_task(worker(context, 1, stop_event)),
                asyncio.create_task(worker(context, 2, stop_event))
            ]

            print(f"\n♻️ NEW SESSION STARTED | Target: {TARGET}")
            
            # --- 2 MINUTE RELOAD TIMER ---
            await asyncio.sleep(120) 
            
            print(f"\n🕒 2 MINUTES REACHED | TOTAL SENT: {total_sent} | RELOADING BROWSER...")
            stop_event.set() # Tells workers to stop
            
            # Wait a moment for workers to finish current message
            await asyncio.gather(*tasks, return_exceptions=True)
            await browser.close()
            
            # Small breather for the GitHub IP before next session
            await asyncio.sleep(3)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n🛑 STOPPED | TOTAL SENT: {total_sent}")
