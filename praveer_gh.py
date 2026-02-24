def run_agent(machine_id):
    driver = None
    try:
        log(f"MACHINE {machine_id} - Starting Cycle")
        driver = setup_driver()
        
        target_url = os.getenv('GROUP_URL')
        session_id = os.getenv('SESSION_ID')
        
        # 1. Open the domain first (you can't add cookies to a blank page)
        driver.get(target_url)
        time.sleep(5)

        # 2. Inject your Session Cookie
        # Note: 'name' might be 'session_id', 'sid', or 'token' depending on the site.
        log("Injecting session cookie...")
        driver.add_cookie({
            'name': 'session_id', # Adjust this name if you know the site's cookie name
            'value': session_id,
            'path': '/',
        })
        
        # 3. Refresh to apply the cookie
        driver.refresh()
        log("Page refreshed with session. Waiting for load...")
        time.sleep(15) 

        # 4. Find the box (Try a more aggressive search)
        log("Searching for message input field...")
        # This searches for anything that looks like an input or text box
        selectors = [
            "//div[@contenteditable='true']",
            "//textarea",
            "//input[@type='text']",
            "//*[contains(@class, 'input')]",
            "//*[contains(@class, 'message')]"
        ]
        
        message_box = None
        for selector in selectors:
            try:
                message_box = driver.find_element(By.XPATH, selector)
                if message_box.is_displayed():
                    log(f"Found input using: {selector}")
                    break
            except:
                continue

        if message_box:
            content = f"Matrix Agent {machine_id} online. Status: Active. ID: {random.randint(100, 999)}"
            message_box.send_keys(content)
            time.sleep(2)
            message_box.send_keys(u'\ue007') 
            log("✅ Message sent!")
        else:
            log("❌ Could not find the message box. Saving screenshot...")
            driver.save_screenshot(f"debug_m{machine_id}.png")
            
    except Exception as e:
        log(f"❌ Error: {e}")
    finally:
        if driver:
            driver.quit()
