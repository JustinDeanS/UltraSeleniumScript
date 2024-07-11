from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Path to your WebDriver
webdriver_path = './chromedriver'

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

    try:
        # Locate the specific button for the GA Tier 2 ticket
        button = driver.find_element(By.XPATH, "//a[@id='general-admission-ga-3-day-ticket-24-2-2-link']")
        
        # Print button text for debugging
        button_text = button.text.strip()
        print(f"Button text: {button_text}")
        
        if button_text.lower() != 'coming soon'.lower():
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
            break
        # Wait for some time before checking again
        time.sleep(300)  # Check every 5 minutes

    driver.quit()

if __name__ == "__main__":
    main()
