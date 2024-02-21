import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://demoqa.com/frames")
driver.maximize_window()
def iframe1 ():
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"frame1")))
    # driver.switch_to.frame(driver.find_element(By.ID,"frame1" ))
    time.sleep(4)
    Actual_result = driver.find_element(By.ID, "sampleHeading")
    Message = Actual_result.text
    print(Message)
    Expected_result = "This is a sample page"
    if Message == Expected_result:
        print("Pass")
    else:
      print("Fail")

def iframe2 ():
    driver.switch_to.default_content()
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"frame2")))
    # driver.switch_to.frame(driver.find_element(By.ID, "frame2"))
    time.sleep(4)
    Actual_result = driver.find_element(By.ID, "sampleHeading")
    Message = Actual_result.text
    print(Message)
    Expected_result = "This is a sample page"
    if Message == Expected_result:
        print("Pass 1")
    else:
        print("Fail 2")
iframe1()
iframe2()