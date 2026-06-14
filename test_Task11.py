import time

from selenium import webdriver
from selenium.webdriver.common.by import By



def validate(element,name):
    assert element.is_displayed(),f"{name} is not visible"
    assert element.is_enabled(),f"{name} is not enabled"

def test_login_pos():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")
    time.sleep(2)
    Login = driver.find_element(By.XPATH, "//*[@id='header-container']/child::div[1]/child::div[4]/div/button[1]")
    Login.click()
    time.sleep(4)
    assert "https://www.guvi.in/sign" in driver.current_url     # to validate the URL of the Login button
    driver.quit()

def test_username_password_pos():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")
    Login = driver.find_element(By.XPATH, "//*[@id='header-container']/child::div[1]/child::div[4]/div/button[1]")
    Login.click()
    email = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "password")

# validating Username and password field enabled and displayed
    validate(email, "Email")
    validate(password, "Password")
    driver.quit()

def test_submit_pos():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")
    Login = driver.find_element(By.XPATH, "//*[@id='header-container']/child::div[1]/child::div[4]/div/button[1]")
    Login.click()
    time.sleep(5)
    email = driver.find_element(By.ID, "email")
    email.send_keys("gvajk625@gmail.com")
    password = driver.find_element(By.ID, "password")
    password.send_keys("Jeeva@123")
    Login_button = driver.find_element(By.XPATH, "//a[@id='login-btn']")
    validate(Login_button,"Login")               # validating submit button
    Login_button.click()
    time.sleep(5)
    driver.quit()


#############Negative testcase##############

def test_login_neg():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")
    time.sleep(2)
    Login = driver.find_element(By.XPATH, "//*[@id='header-container']/child::div[1]/child::div[4]/div/button[1]")
    Login.click()
    time.sleep(4)
    assert "https://www.guvisign.in" in driver.current_url     # to validate the URL of the Login button neg case
    driver.quit()

def test_username_password_neg():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")
    Login = driver.find_element(By.XPATH, "//*[@id='header-container']/child::div[1]/child::div[4]/div/button[1]")
    Login.click()
    email = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "password")

# validating Username and password field negative case
    assert "email.com" in email
    assert "checkassertion" in password
    # validate(email, "")
    # validate(password, "")
    driver.quit()

def test_submit_neg():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")
    Login = driver.find_element(By.XPATH, "//*[@id='header-container']/child::div[1]/child::div[4]/div/button[1]")
    Login.click()
    email = driver.find_element(By.ID, "email")
    email.send_keys("gvajk625@gmail.com")
    time.sleep(4)
    password = driver.find_element(By.ID, "password").send_keys("Jeeva@123")
    time.sleep(4)
    Login_button = driver.find_element(By.XPATH, "//a[@id='login-btn']")
    assert "submitassertion" in Login_button
    #validate(Login_button,"")               # validating submit button neg case
    Login_button.click()
    driver.quit()


