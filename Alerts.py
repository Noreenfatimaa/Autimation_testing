import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
def button1():
    driver.find_element(By.CSS_SELECTOR, "button[id='alertButton']").click()
    alert = Alert(driver)
    alert.accept()
def button2():
    driver.find_element(By.CSS_SELECTOR, "button[id='timerAlertButton']").click()
    time.sleep(10)
    alert = Alert(driver)
    alert.accept()
def button3():
    driver.find_element(By.CSS_SELECTOR, "button[id='confirmButton']").click()
    alert = Alert(driver)
    alert.accept()
    time.sleep(5)
    Actual_result = driver.find_element(By.CSS_SELECTOR, "span[id='confirmResult']")
    Message = Actual_result.text
    print(Message)
    Expected_result = "You selected Ok"
    if Message == Expected_result:
        print("Pass")
    else:
        print("Fail")
    driver.find_element(By.CSS_SELECTOR, "button[id='confirmButton']").click()
    alert = Alert(driver)
    alert.dismiss()
    time.sleep(5)
    Actual_result = driver.find_element(By.CSS_SELECTOR, "span[id='confirmResult']")
    Message = Actual_result.text
    print(Message)
    Expected_result = "You selected Cancel"
    if Message == Expected_result:
        print("Pass")
    else:
        print("Fail")
def button4():
    time.sleep(3)
    actions = ActionChains(driver)
    element = driver.find_element(By.CSS_SELECTOR,".row .col>button[id='promtButton']")
    actions.click(element).perform()
    time.sleep(3)

    alert = Alert(driver)
    alert.send_keys("Text entered")
    alert.accept()
    time.sleep(5)
    Actual_result = driver.find_element(By.CSS_SELECTOR, "span[id='promptResult']")
    Message = Actual_result.text
    print(Message)
    Expected_result = "You entered Text entered"
    if Message == Expected_result:
        print("Pass")
    else:
        print("Fail")
button1()
button2()
button3()
button4()
