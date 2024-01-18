
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/radio-button")

driver.find_element(By.CSS_SELECTOR, "label[for='impressiveRadio']").click()
# driver.find_element(By.CSS_SELECTOR, "label[class='custom-control-label']").click()
Message = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p/span")
Actual_result = Message.text
print(Actual_result)
time.sleep(4)
Expected_Result= "Impressive"
if Expected_Result==Actual_result:
    print("Test case is pass")
else:
    print("Test case is fail")

driver.quit()

