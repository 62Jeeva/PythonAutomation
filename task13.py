import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")
# action class to drag and drop
actions = ActionChains(driver)
frame = driver.find_element(By.XPATH, "//iframe[@src = '/resources/demos/droppable/default.html']")
driver.switch_to.frame(frame)

# xpath for the source frame and target
source_Image = driver.find_element(By.XPATH, "//div[@id='draggable']/p")
target_Area = driver.find_element(By.XPATH, "//div[@id='droppable']")

# for holding,drag and drop
(actions.click_and_hold(source_Image)
 .move_to_element(target_Area)
 .release(target_Area)
 .perform())

driver.switch_to.default_content()
driver.close()


