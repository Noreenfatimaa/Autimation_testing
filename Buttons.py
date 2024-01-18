import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://demoqa.com/buttons")
time.sleep(4)
def doubleclick():
    element= driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/button")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    time.sleep(4)
    Actual_result = driver.find_element(By.ID, "doubleClickMessage")
    Message= Actual_result.text
    print(Message)
    Expected_result= "You have done a double click"
    if Message == Expected_result:
        print("Pass")
    else:
        print("Fail")

def rightclick():
    element= driver.find_element(By.ID, "rightClickBtn")
    actions = ActionChains(driver)
    actions.context_click(element).perform()
    time.sleep(10)
    Actual_result = driver.find_element(By.ID, "rightClickMessage")
    Message = Actual_result.text
    print(Message)
    Expected_result = "You have done a right click"
    if Message == Expected_result:
        print("Pass")
    else:
        print("Fail")

def clickme():
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button").click()
    time.sleep(10)
    Actual_result = driver.find_element(By.ID, "dynamicClickMessage")
    Message = Actual_result.text
    print(Message)
    Expected_result = "You have done a dynamic click"
    if Message == Expected_result:
        print("Pass")
    else:
        print("Fail")

doubleclick()
rightclick()
clickme()

driver.quit()