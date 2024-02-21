import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://demoqa.com/date-picker")
driver.maximize_window()
def seldate1():
    driver.find_element(By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']").click()
    Expected_date= "December 1999"
    while True:

        Actual_date= driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]")
        if Expected_date== Actual_date.text:
            break
        else:
           driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/button[1]").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[5]/div[2]").click()
    time.sleep(5)
def seldate2():
    driver.find_element(By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']").click()
    date= "February 2020"
    while True:
        mydate = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]")
        if date == mydate.text:
            break
        else:
           driver.find_element(By.CSS_SELECTOR,"button[class='react-datepicker__navigation react-datepicker__navigation--previous']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[6]").click()
    time.sleep(4)
def seltime():
    driver.find_element(By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']").click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div/ul/li[44]").click()
    time.sleep(5)

seldate1()
seldate2()
seltime()
