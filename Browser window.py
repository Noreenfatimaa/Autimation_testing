import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")

def newtab():
    driver.find_element(By.ID, "tabButton").click()
    time.sleep(4)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    element= driver.find_element(By.XPATH, "/html/body/h1")
    assert element.text in 'This is a sample page'
    if element.text == "This is a sample page":
        print("Pass")
    else:
        print("Fail")
    time.sleep(4)
    driver.close()
def newwindow():
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.ID, "windowButton").click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(4)
    element = driver.find_element(By.XPATH, "/html/body/h1")
    assert element.text in 'This is a sample page'
    if element.text == "This is a sample page":
        print("New window test pass")
    else:
        print("New window test fail")
    time.sleep(4)
    driver.close()

def newwindowmessage():
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.ID, "messageWindowButton").click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(4)
    driver.close()

newtab()
newwindow()
newwindowmessage()
