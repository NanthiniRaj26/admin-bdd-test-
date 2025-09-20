from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start Edge browser
driver = webdriver.Edge()

# Open Django admin login page
driver.get("http://127.0.0.1:8000/admin/")
time.sleep(2)

# Login
driver.find_element(By.NAME, "username").send_keys("Nanz")
driver.find_element(By.NAME, "password").send_keys("Nanz@123")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(2)

# Click on "Audit reports" under Core
driver.find_element(By.LINK_TEXT, "Audit reports").click()
time.sleep(2)

# Take screenshot of the Audit Report list page
driver.save_screenshot("audit_reports_page.png")

# Print page title to confirm navigation
print("Page title after navigation:", driver.title)

# Close browser
driver.quit()