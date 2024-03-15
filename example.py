from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Replace with your ChromeDriver path
driver_path = "<chromedriver.exe path>"

# Initialize WebDriver
service = Service(driver_path)  # Path to ChromeDriver
driver = webdriver.Chrome(service=service)

# Open a webpage
url = "https://www.google.com/"
driver.get(url)

# Maximize window (optional)
driver.maximize_window()

# Find element by ID (search box)
search_box = driver.find_element(By.ID, "APjFqb")

# Send keys (enter text)
search_box.send_keys("Selenium Python Tutorial" + Keys.ENTER)  # Combine text entry with pressing Enter

# # Find element by link text (e.g., "About")
# about_link = driver.find_element(By.LINK_TEXT, "Google")

# # Click the link
# about_link.click()

# Get current URL
current_url = driver.current_url
print("Current URL:", current_url)

# Get page title
page_title = driver.title
print("Page Title:", page_title)

# Find element by name (e.g., search form)
search_form = driver.find_element(By.NAME, "q")  # Replace with actual name attribute

# Clear the search box (optional)
search_form.clear()

# # Find element by XPath (assuming a specific element)
# xpath_element = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/a[1]")  # Replace with your valid XPath

# # Click the element
# xpath_element.click()

# Wait for element to be visible (using WebDriverWait)
wait = WebDriverWait(driver, 10)  # 10 seconds timeout
element = wait.until(EC.presence_of_element_located((By.ID, "APjFqb")))

# Navigate back
driver.back()

# Navigate forward
driver.forward()

# Close browser window
driver.close()

# Quit WebDriver (recommended to release resources)
driver.quit()

print("Finished!")
