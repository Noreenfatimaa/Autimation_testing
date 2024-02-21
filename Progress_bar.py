import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://demoqa.com/progress-bar")
driver.maximize_window()

def case1():
    progress = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID,"startStopButton")))
    progress.click()
    while True:
        progressCondition = driver.find_element(By.ID, "progressBar")
        Bar= progressCondition.text
        if Bar == '30%':
            driver.find_element(By.ID, "startStopButton").click()
            time.sleep(3)
            print(Bar)
            break
def case2():
    progress = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID,"startStopButton")))
    progress.click()
    while True:
        progressCondition = driver.find_element(By.ID, "progressBar")
        Bar= progressCondition.text
        if Bar == '70%':
            driver.find_element(By.ID, "startStopButton").click()
            time.sleep(3)
            print(Bar)
            break
case1()
case2()



