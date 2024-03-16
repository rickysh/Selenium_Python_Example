from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service 


# Replace with your ChromeDriver path
driver_path = "chromedriver.exe"

# Initialize WebDriver
service = Service(driver_path)  # Path to ChromeDriver
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com")
driver.implicitly_wait(1)
element = driver.find_element(by=By.NAME, value="search_query")
element.send_keys("Selenium automation")
element.send_keys(Keys.RETURN)
driver.implicitly_wait(5)
driver.close()
driver.quit()
print("Finished!")
