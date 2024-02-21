import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://demoqa.com/slider")
driver.maximize_window()

slider=driver.find_element(By.CSS_SELECTOR, "input[type='range']")
move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(3, 0).release().perform()
time.sleep(5)

move.click_and_hold(slider).move_by_offset(180, 0).release().perform()
time.sleep(5)

move.click_and_hold(slider).move_by_offset(300, 0).release().perform()
time.sleep(5)
