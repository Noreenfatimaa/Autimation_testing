import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/links")
time.sleep(4)
Actual_result = driver.find_element(By.XPATH, "//*[@id='linkWrapper']/h5[1]/strong")
Message= Actual_result.text
print(Message)
Expected_result= "Following links will open new tab"
if Message == Expected_result:
        print("Pass")
else:
        print("Fail")
        driver.quit()
def home():
    driver.find_element(By.LINK_TEXT, "Home").click()
    time.sleep(4)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    driver.close()
    time.sleep(3)
def HomeHLML5():
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.ID, "dynamicLink").click()
    time.sleep(4)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    driver.close()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[0])
home()
HomeHLML5()
Actual_result = driver.find_element(By.XPATH, "//*[@id='linkWrapper']/h5[2]/strong")
Message= Actual_result.text
print(Message)
Expected_result= "Following links will send an api call"
if Message == Expected_result:
    print("Pass")
else:
    print("Fail")
    driver.quit()
def Created():
    driver.find_element(By.LINK_TEXT, "Created").click()
    time.sleep(3)
    Actual_result = driver.find_element(By.ID, "linkResponse")
    Message= Actual_result.text
    print(Message)
    Expected_result= "Link has responded with staus 201 and status text Created"
    if Message == Expected_result:
            print("Pass")
    else:
            print("Fail")
Created()

def no_content():
    driver.find_element(By.LINK_TEXT, "No Content").click()
    time.sleep(3)
    Actual_result = driver.find_element(By.ID, "linkResponse")
    Message= Actual_result.text
    print(Message)
    Expected_result= "Link has responded with staus 204 and status text No Content"
    if Message == Expected_result:
            print("Pass")
    else:
            print("Fail")
no_content()

def Moved():
    driver.find_element(By.LINK_TEXT, "Moved").click()
    time.sleep(3)
    Actual_result = driver.find_element(By.ID, "linkResponse")
    Message= Actual_result.text
    print(Message)
    Expected_result= "Link has responded with staus 301 and status text Moved Permanently"
    if Message == Expected_result:
            print("Pass")
    else:
            print("Fail")
Moved()

def bad_request():
    driver.find_element(By.LINK_TEXT, "Bad Request").click()
    time.sleep(3)
    Actual_result = driver.find_element(By.ID, "linkResponse")
    Message= Actual_result.text
    print(Message)
    Expected_result= "Link has responded with staus 400 and status text Bad Request"
    if Message == Expected_result:
            print("Pass")
    else:
            print("Fail")
bad_request()

def unauthorized():
    driver.find_element(By.LINK_TEXT, "Unauthorized").click()
    time.sleep(3)
    Actual_result = driver.find_element(By.ID, "linkResponse")
    Message= Actual_result.text
    print(Message)
    Expected_result= "Link has responded with staus 401 and status text Unauthorized"
    if Message == Expected_result:
            print("Pass")
    else:
            print("Fail")
unauthorized()

def forbidden():
    driver.find_element(By.LINK_TEXT, "Forbidden").click()
    time.sleep(3)
    Actual_result = driver.find_element(By.ID, "linkResponse")
    Message= Actual_result.text
    print(Message)
    Expected_result= "Link has responded with staus 403 and status text Forbidden"
    if Message == Expected_result:
            print("Pass")
    else:
            print("Fail")
forbidden()

def not_found():
    driver.find_element(By.LINK_TEXT, "Not Found").click()
    time.sleep(3)
    Actual_result = driver.find_element(By.ID, "linkResponse")
    Message= Actual_result.text
    print(Message)
    Expected_result= "Link has responded with staus 404 and status text Not Found"
    if Message == Expected_result:
            print("Pass")
    else:
            (print("Fail"))
not_found()













