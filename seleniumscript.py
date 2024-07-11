from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Path to your WebDriver
webdriver_path = 'path/to/chromedriver'

# URL to check
url = "https://ultramusicfestival.com/tickets/miami/"

# Configure Selenium WebDriver
options = Options()
options.add_argument("--headless")  # Run in headless mode (without opening a browser window)
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service, options=options)

# Function to check availability
def check_ticket_availability():
    driver.get(url)

    # Find the section containing the ticket information
    try:
        # Locate the elements using the correct XPath or CSS selectors
        sub_type = driver.find_element(By.XPATH, "//p[@class='sub_type color' and contains(text(), 'Tier 2')]")
        title = driver.find_element(By.XPATH, "//p[@class='title' and contains(text(), 'GA 3-Day Ticket')]")
        date = driver.find_element(By.XPATH, "//p[@class='date color' and contains(text(), 'March 28, 29, 30 – 2025')]")
        
        # Check if the 'COMING SOON' button is replaced with something else (e.g., 'BUY NOW')
        button = driver.find_element(By.XPATH, "//a[contains(@class, 'tix soon regbtn')]")
        
        if button and 'Coming Soon' not in button.text:
            print("Tickets are available!")
            return True
        else:
            print("Tickets are not available yet.")
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Ticket section not found.")
    
    return False

# Main loop to periodically check the availability
def main():
    while True:
        if check_ticket_availability():
            # Send a notification or take further action if tickets are available
            break
        # Wait for some time before checking again
        time.sleep(300)  # Check every 5 minutes

    driver.quit()

if __name__ == "__main__":
    main()
