import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# configure the logging settings
logging.basicConfig(filename="test_log.log", level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

#screenshot_file_path = "E:\\Offline_Batch_17\\Projects\\TestAutomationPnT17\\screenshots"
screenshot_file_path = "E:\\QA\\Browsers\\screenshorts"

def login_testCase1_valid():

    logging.info('login_testCase1_valid Execution Start....')
    # Step 1: Launch Browser
    driver = webdriver.Firefox()
    logging.info('Firefox Launch Successful.')
    driver.maximize_window()
    driver.implicitly_wait(5)

    # Step 2: Open URL
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
    register.info('register page open Successful.')

    # Step 3: Enter firstname
    firstname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "input-firstname")))
    firstname_field_enable_state = firstname_field.is_enabled()

    # verify firstname field is enabled or nor
    if firstname_field_enable_state:
        firstname_field.clear()
        firstname_field.send_keys("saad")
        register.info('Type firstname Successful.')
    else:
        logging.error("firstname field is not enabled.Test Failed.")

    # Step 4: Enter Lastname
    lastname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "input-lastname")))
    lastname_field_enable_state = lastname_field.is_enabled()

    # verify lastname field is enabled or nor
    if lastnamee_field_enable_state:
        lastname_field.clear()
        lastname_field.send_keys("chy")
        register.info('Type lastname Successful.')
    else:
        logging.error("lastname field is not enabled.Test Failed.")

    # Step 5: Enter email
    email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "input-email")))
    email_field_enable_state = email_field.is_enabled()

    # verify email field is enabled or nor
    if email_field_enable_state:
        email_field.clear()
        email_field.send_keys("saadchy@test.com")
        register.info('Type email Successful.')
    else:
        logging.error("email field is not enabled.Test Failed.")

    # Step 6: Enter Phone
    telephone_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "input-telephone")))
    telephone_field_enable_state = telephone_field.is_enabled()

    # verify telephone field is enabled or nor
    if telephone_field_enable_state:
        telephone_field.clear()
        telephone_field.send_keys("Admin")
        register.info('Type telephone Successful.')
    else:
        logging.error("telephone field is not enabled.Test Failed.")

    # Step 7: Enter Password
    password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "input-password")))
    password_field_enable_state = password_field.is_enabled()

    # verify password field is enabled or not
    if password_field_enable_state:
        password_field.clear()
        password_field.send_keys("admin123")
        logging.info('Type Password Successful.')
    else:
        logging.error("Password field is not enabled.Test Failed")

    # Step 8: Enter Password
    confirm_password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "input-confirm")))
    confirm_ password_field_enable_state = confirm_ password_field.is_enabled()

    # verify password field is enabled or not
    if confirm_password_field_enable_state:
        confirm_password_field.clear()
        confirm_password_field.send_keys("admin123")
        logging.info('Type Password Successful.')
    else:
        logging.error("Password field is not enabled.Test Failed")

    # Step 5: Click radio button
    login_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-horizontal .radio-inline:nth-of-type(2) [type]")))
    login_button.click()
    logging.info('Login Button clicked Successful.')
    time.sleep(5)

    # verify login or not by check URL
    expected_url = "https://tutorialsninja.com/demo/index.php?route=account/success"
    actual_url = driver.current_url

    if expected_url == actual_url:
        logging.info('Test Passed. Login successful.')
        # capture screenshot
        driver.get_screenshot_as_file(screenshot_file_path+"\\login_passed_test_passed.png")
    else:
        logging.error("Test Failed. Login failed.")
        # capture screenshot
        driver.get_screenshot_as_file(screenshot_file_path+"\\login_failed_test_failed.png")

    driver.close()
    logging.info('login_testCase1_valid execution completed..')


def login_testCase2_invalid():
    logging.info('login_testCase2_invalid Execution Start....')
    # Step 1: Launch Browser
    driver = webdriver.Firefox()
    logging.info('Firefox Launch Successful.')
    driver.maximize_window()

    # Step 2: Open URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


    # Step 3: Enter Username
    username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
    username_field_enable_state = username_field.is_enabled()

    # verify that username field is enabled or not
    if username_field_enable_state:
        username_field.clear()
        username_field.send_keys("Admin123")
        logging.info('Type Username Successful.')
    else:
        logging.error("Username field is not enabled.Test Failed.")

    # Step 4: Enter Password
    password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
    password_field_enable_state = password_field.is_enabled()

    # verify that password field is enabled or not
    if password_field_enable_state:
        password_field.clear()
        password_field.send_keys("admin123")
        logging.info('Type Password Successful.')
    else:
        logging.error("Password field is not enabled.Test Failed")

    # Step 5: Click Login button
    login_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".orangehrm-login-button")))
    login_button.click()
    logging.info('Login Button clicked Successful.')
    time.sleep(4)

    # verify login or not by check error message
    error_message = driver.find_element(By.CSS_SELECTOR, ".oxd-alert-content-text")
    actual_error_message_text = error_message.text

    expected_error_message = "Invalid credentials"

    if expected_error_message == actual_error_message_text:
        logging.info("Test Passed. Login failed.Error message: " + expected_error_message)
        # capture screenshot
        driver.get_screenshot_as_file(screenshot_file_path + "\\test_passed_login_failed.png")
    else:
        logging.error("Test Failed. Did not get expected error message: " + expected_error_message)
        driver.get_screenshot_as_file(screenshot_file_path + "\\test_failed_login_passed.png")

    driver.close()
    logging.info('login_testCase2_invalid execution completed..')


login_testCase1_valid()
# login_testCase2_invalid()