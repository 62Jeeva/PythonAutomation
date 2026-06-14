import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_sauce_demo_pos():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(4)
    driver.find_element(By.CLASS_NAME, "submit-button").click()

# to check the title of the webpage
    header = driver.find_element(By.XPATH, "//div[@class='app_logo']")
    print(header.text)
    assert driver.title == 'Swag Labs'
    time.sleep(4)
    driver.quit()

def test_homepage_pos():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

#to check the current-URL of the dashboard
    assert driver.current_url ==  "https://www.saucedemo.com/"
    driver.quit()

def test_dashboard_pos():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CLASS_NAME, "submit-button").click()
    assert "www.saucedemo.com" in driver.current_url
    driver.quit()


def test_sauce_demo_neg():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(4)
    driver.find_element(By.CLASS_NAME, "submit-button").click()

# to check the title of the webpage
    header = driver.find_element(By.XPATH, "//div[@class='app_logo']")
    print(header.text)
    assert driver.title == 'SwagLabs'
    time.sleep(4)
    driver.quit()


def test_homepage_neg():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    assert driver.current_url == 'www.sauce_demo.co'
    driver.quit()

def test_dashboard_neg():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CLASS_NAME, "submit-button").click()
    assert "saucedemo_shooping.com" in driver.current_url






