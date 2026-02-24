import os
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth

def setup_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    # Change user-agent to look like a real browser
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    driver = webdriver.Chrome(options=options)
    
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True)
    
    driver.set_page_load_timeout(60)
    return driver

def run_logic(machine_id):
    driver = None
    try:
        print(f"--- Machine {machine_id}: Starting Browser Session ---")
        driver = setup_driver()
        
        # YOUR CORE LOGIC HERE
        # Example: driver.get(os.getenv('GROUP_URL'))
        print(f"Machine {machine_id}: Navigated to target. Performing actions...")
        
        # Simulate work
        time.sleep(random.randint(10, 20))
        
    except Exception as e:
        print(f"Error in Machine {machine_id}: {e}")
    finally:
        if driver:
            driver.quit()
            print(f"--- Machine {machine_id}: Browser Closed ---")

if __name__ == "__main__":
    m_id = os.getenv('MACHINE_ID', '1')
    start_time = time.time()
    # Run for 5 hours and 30 mins (19800 seconds)
    max_duration = 5.5 * 60 * 60 

    while (time.time() - start_time) < max_duration:
        run_logic(m_id)
        # Wait between cycles to avoid detection
        wait = random.randint(60, 180)
        print(f"Waiting {wait}s before next cycle...")
        time.sleep(wait)
