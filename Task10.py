import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.CLASS_NAME,"submit-button").click()

#to fetch the tile of the application
Header=driver.find_element(By.CLASS_NAME,"app_logo")
print("Title of the webpage:",Header.text)
time.sleep(4)

#to fetch the current_URL
print("Current URL has been printed:",driver.current_url)

# to fetch the content of the webpage
html_content = driver.page_source

#to save the webpage content in text file
file = open("D:\\WebPage_Task_11.txt","w")
file.write(html_content)

