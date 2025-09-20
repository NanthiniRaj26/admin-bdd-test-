from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('the Django admin login page is open')
def step_open_login(context):
    context.driver = webdriver.Edge()
    context.driver.get("http://127.0.0.1:8000/admin/")
    time.sleep(2)

@when('the user logs in with "{username}" and "{password}"')
def step_login(context, username, password):
    context.driver.find_element(By.NAME, "username").send_keys(username)
    context.driver.find_element(By.NAME, "password").send_keys(password)
    context.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    time.sleep(2)

@when('the user clicks on "Audit reports"')
def step_click_audit(context):
    context.driver.find_element(By.LINK_TEXT, "Audit reports").click()
    time.sleep(2)

@then('the audit report list should be displayed')
def step_verify_list(context):
    assert "Select audit report to change" in context.driver.page_source
    context.driver.save_screenshot("audit_report_list.png")
    context.driver.quit()