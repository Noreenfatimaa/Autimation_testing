# Import webdriver
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/text-box")

driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/input").send_keys("Fatima")
driver.find_element(By.ID,"userEmail").send_keys("test@mailinator.com")
driver.find_element(By.CSS_SELECTOR, "textarea[placeholder='Current Address']").send_keys("Lahore")
driver.find_element(By.ID, "permanentAddress").send_keys("Toba Tek Singh")
driver.find_element(By.CLASS_NAME, "btn-primary").click()
time.sleep(20)
driver.quit()