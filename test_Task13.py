import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

def test_drag_and_drop_pos():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://jqueryui.com/droppable/")
#action class to drag and drop
    actions = ActionChains(driver)
    frame = driver.find_element(By.XPATH, "//iframe[@src = '/resources/demos/droppable/default.html']")
    driver.switch_to.frame(frame)

#xpath for the source frame and target
    source_Image = driver.find_element(By.XPATH, "//div[@id='draggable']/p")
    target_Area = driver.find_element(By.XPATH, "//div[@id='droppable']")

# for holding,move to element,drag and drop
    (actions.click_and_hold(source_Image)
     .move_to_element(target_Area)
     .release(target_Area)
     .perform())

    driver.switch_to.default_content()
    driver.close()

def test_direct_drag_and_drop_pos():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://jqueryui.com/droppable/")
    iframe = driver.find_element(By.CLASS_NAME, "demo-frame")
    driver.switch_to.frame(iframe)
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")
    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()
    driver.switch_to.default_content()
    driver.quit()

def test_drag_and_drop_neg():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://jqueryui.com/droppable/")
    # action class to drag and drop
    actions = ActionChains(driver)
    frame1 = driver.find_element(By.XPATH, "//iframe[@src = '/resources/demos/droppable/default.html']")
    driver.switch_to.frame(frame1)

    # xpath for the source frame and target
    source_Image = driver.find_element(By.XPATH, "//div[@id='draggable1']/p")
    target_Area = driver.find_element(By.XPATH, "//div[@id='droppable2']")

    # for holding,drag and drop
    (actions.click_and_hold(source_Image)
     .move_to_element(target_Area)
     .release(target_Area)
     .perform())

    driver.switch_to.default_content()
    driver.close()

