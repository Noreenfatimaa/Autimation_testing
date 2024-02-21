import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://practice.cydeo.com/dropdown")
driver.maximize_window()
Select(driver.find_element(By.ID ,"dropdown")).select_by_index("1")
time.sleep(5)
Select(driver.find_element(By.ID ,"year")).select_by_visible_text("2005")
Select(driver.find_element(By.ID ,"month")).select_by_visible_text("May")
Select(driver.find_element(By.ID ,"day")).select_by_value("13")
time.sleep(5)
Select(driver.find_element(By.ID ,"state")).select_by_value("CT")
time.sleep(5)
Select(driver.find_element(By.XPATH ,"/html/body/div[1]/div[2]/div/select[6]")).select_by_value("c")
time.sleep(5)
driver.find_element(By.ID ,"dropdownMenuLink").click()
driver.find_element(By.XPATH ,"/html/body/div[1]/div[2]/div/div/div/a[2]").click()
time.sleep(5)
