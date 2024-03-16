from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager


# Replace with your ChromeDriver path
driver_path = "chromedriver.exe"

# Initialize WebDriver
service = Service(driver_path)  # Path to ChromeDriver
driver = webdriver.Chrome(service=service)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title
print(f"Title = {title}")
driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text
print(f"Text = {text}")

driver.close()

driver.quit()

print("Finished!")
