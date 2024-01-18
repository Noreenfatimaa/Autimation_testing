import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/webtables")
driver.find_element(By.ID, "addNewRecordButton").click()
time.sleep(4)
driver.find_element(By.CLASS_NAME, "mr-sm-2").send_keys("Noreen")
driver.find_element(By.XPATH, "//*[@id='lastName']").send_keys("Fatima")
driver.find_element(By.ID, "userEmail").send_keys("test@mailinator.com")
driver.find_element(By.ID, "age").send_keys("30")
driver.find_element(By.ID, "salary").send_keys("5000")
driver.find_element(By.ID, "department").send_keys("Computer")
driver.find_element(By.ID, "submit").click()
time.sleep(4)
def search():
    driver.find_element(By.ID, "searchBox").send_keys("kierra")
    driver.find_element(By.ID, "searchBox").clear()
    driver.refresh()
    time.sleep(4)
def edit():
    driver.find_element(By.ID, "edit-record-2").click()
    driver.find_element(By.ID, "department").clear()
    driver.find_element(By.ID, "department").send_keys("Computer science")
    driver.find_element(By.ID, "submit").click()
    time.sleep(4)
def delete():
    driver.find_element(By.ID, "delete-record-1").click()
    time.sleep(4)
search()
edit()
delete()

driver.quit()
