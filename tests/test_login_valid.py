"""
Verify that login is working with valid use.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_valid_user():
    # credentials
    username = 'UserTest1'
    password = 'PokecTestUser1'

    driver = webdriver.Firefox(executable_path="C:\\Users\\samue\\Desktop\\Private\\Files\\AA programming\\Automation"
                                               "\\drivers\\geckodriver.exe")
    driver.get("https://pokec.azet.sk/")
    driver.maximize_window()
    driver.delete_all_cookies()

    # accept cookies
    cookies_button = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]/p')
    cookies_button.click()

    # login
    username_input = driver.find_element_by_name('username')
    username_input.clear()
    username_input.send_keys(username)

    password_input = driver.find_element_by_name('password')
    password_input.clear()
    password_input.send_keys(password)

    login_button = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div/form/button')
    login_button.click()

    # verify successful login
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/a/div/div/div/span[2]/span')))

    string = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div/a/div/div/div/span[2]/span').text
    assert string == username

    driver.quit()
