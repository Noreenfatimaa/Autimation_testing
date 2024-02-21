import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://demoqa.com/nestedframes")
driver.maximize_window()
def parentframe():
    driver.switch_to.frame(driver.find_element(By.ID,"frame1" ))
    time.sleep(4)
    Meessage= driver.find_element(By.XPATH, "/html/body")
    print(Meessage.text)
    assert Meessage.text in "Parent frame"
    if Meessage.text == "Parent frame":
        print("Pass")
    else:
        print("Fail")
def childclass ():
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.ID, "frame1"))
    driver.switch_to.frame(driver.find_element(By.XPATH,"/html/body/iframe" ))
    time.sleep(4)
    Meessage= driver.find_element(By.XPATH, "/html/body")
    print(Meessage.text)
    assert Meessage.text in "Child Iframe"
    if Meessage.text == "Child Iframe":
        print("Pass")
    else:
        print("Fail")

parentframe()
childclass()