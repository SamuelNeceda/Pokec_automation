"""
Verify that application is working
"""
import requests
from selenium import webdriver


def test_webapp_working():
    driver = webdriver.Firefox(executable_path="C:\\Users\\samue\\Desktop\\Private\\Files\\AA programming\\Automation"
                                               "\\drivers\\geckodriver.exe")
    driver.get("https://pokec.azet.sk/")
    driver.maximize_window()
    driver.delete_all_cookies()

    # check html response
    url = "https://pokec.azet.sk/"
    response = requests.get(url)
    assert response.status_code == 200

    # check for URL loaded
    assert driver.current_url == url

    # check for page title
    title = "Pokec.sk - chat a zoznamka, kde je vždy najviac ľudí"
    assert title == driver.title

    driver.quit()
