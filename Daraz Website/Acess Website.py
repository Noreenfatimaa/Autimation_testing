import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.daraz.pk/")
driver.maximize_window()
def Productaddtocart ():
    driver.find_element(By.CSS_SELECTOR, "input[type='search']").click()
    driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys("Mobile")
    driver.find_element(By.CSS_SELECTOR, "button[class='search-box__button--1oH7']").click()
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "ant-select-selection__rendered").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,"[data-spm-click='gostr=/lzdse.result.sort;locaid=d4']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div[1]/div[2]/div[7]/div/a").click()
    time.sleep(5)
def verifymesg ():
    Actual_result = driver.find_element(By.CSS_SELECTOR, "[class='pdp-product-price']")
    Message = Actual_result.text
    print(Message)
    Expected_result = "Rs. 1,350"
    if Message == Expected_result:
        print("Pass")
    else:
        print("Fail")
def remain ():
    driver.find_element(By.CSS_SELECTOR, "[class='next-number-picker-handler-up-inner']").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "[class='add-to-cart-buy-now-btn  pdp-button pdp-button_type_text pdp-button_theme_orange pdp-button_size_xl']").click()
    time.sleep(5)
Productaddtocart()
verifymesg()
remain()