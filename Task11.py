import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.guvi.in/")
time.sleep(2)
Login = driver.find_element(By.XPATH,"//*[@id='header-container']/child::div[1]/child::div[4]/div/button[1]")
Login.click()
time.sleep(4)
email = driver.find_element(By.ID,"email")
email.send_keys("gvajk625@gmail.com")
password = driver.find_element(By.ID,"password")
password.send_keys("Jeeva@123")
Login_button = driver.find_element(By.XPATH,"//a[@id='login-btn']").click()
time.sleep(10)
driver.quit()

