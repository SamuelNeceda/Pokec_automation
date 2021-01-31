"""
Verify that login is not working with invalid user.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_invalid_user():
    # credentials
    username = ["", "", "", "invalid", "UserTest1", "UserTest1", "invalid", "invalid"]
    password = ["", "invalid", "PokecTestUser1", "", "", "invalid", "PokecTestUser1", "invalid"]

    driver = webdriver.Firefox(executable_path="C:\\Users\\samue\\Desktop\\Private\\Files\\AA programming\\Automation"
                                               "\\drivers\\geckodriver.exe")
    driver.get("https://pokec.azet.sk/")
    driver.maximize_window()
    driver.delete_all_cookies()

    # accept cookies
    cookies_button = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]/p')
    cookies_button.click()

    for i in range(8):
        # login
        username_input = driver.find_element_by_name('username')
        username_input.clear()
        username_input.send_keys(username[i])

        password_input = driver.find_element_by_name('password')
        password_input.clear()
        password_input.send_keys(password[i])

        login_button = driver.find_element_by_xpath('//*[@id="root"]/div/div[4]/div/form/button')
        login_button.click()

        # error message
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]')))

        string = driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]').text
        expected_string1 = "Zadané údaje nie sú správne."
        expected_string2 = "Nezadali ste prihlasovacie meno."
        assert string in expected_string1 or string in expected_string2

        # wait for alert to disappear
        WebDriverWait(driver, 20).until(
            EC.invisibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]')))

        driver.quit()
