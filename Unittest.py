import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class searchenginestest(unittest.TestCase):
    def test_download(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demoqa.com/upload-download")
        time.sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/a').click()
        time.sleep(5)

    def test_upload(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demoqa.com/upload-download")
        time.sleep(4)
        file_input = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/form/div/input' )
        file_input.send_keys("C:/Users/DELL/Downloads/selenium.png")
        time.sleep(4)
if __name__ == "__main__":
    unittest.main()