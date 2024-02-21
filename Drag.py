import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://demoqa.com/droppable")
driver.maximize_window()
def simple ():
    drag = driver.find_element(By.ID, 'draggable')
    drop = driver.find_element(By.ID, 'droppable')
    Action = ActionChains(driver)
    ActionChains(driver).drag_and_drop(drag, drop).perform()
    time.sleep(5)
    Message = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div/div[2]/p")
    print(Message.text)
    assert Message.text in "Dropped!"
    if Message.text == "Dropped!":
        print("Pass")
    else:
        print("Fail")


def Accept ():
    driver.find_element(By.ID, "droppableExample-tab-accept").click()
    time.sleep(5)
    dragg = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[1]")
    dropp = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]")
    Action = ActionChains(driver)
    ActionChains(driver).drag_and_drop(dragg, dropp).perform()
    time.sleep(5)
    Message = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/p")
    print(Message.text)
    assert Message.text in "Dropped!"
    if Message.text == "Dropped!":
        print("Pass")
    else:
        print("Fail")

def Preventpropagation1():
    driver.find_element(By.ID, "droppableExample-tab-preventPropogation").click()
    time.sleep(5)
    dragg = driver.find_element(By.ID, "dragBox")
    dropp = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div[1]/p")
    Action = ActionChains(driver)
    ActionChains(driver).drag_and_drop(dragg, dropp).perform()
    time.sleep(5)
    Message = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div[1]/p")
    print(Message.text)
    assert Message.text in "Dropped!"
    if Message.text == "Dropped!":
        print("Pass")
    else:
        print("Fail")

    time.sleep(5)
    dragg = driver.find_element(By.ID, "dragBox")
    dropp = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div[1]/div")
    Action = ActionChains(driver)
    ActionChains(driver).drag_and_drop(dragg, dropp).perform()
    time.sleep(5)
    Message = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div[1]/div/p")
    print(Message.text)
    assert Message.text in "Dropped!"
    if Message.text == "Dropped!":
        print("Pass")
    else:
        print("Fail")

def preventprop2():
    driver.find_element(By.ID, "droppableExample-tab-preventPropogation").click()
    time.sleep(5)
    dragg = driver.find_element(By.ID, "dragBox")
    dropp = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div[2]/p")
    Action = ActionChains(driver)
    ActionChains(driver).drag_and_drop(dragg, dropp).perform()
    time.sleep(5)
    Message = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div[2]/p")
    print(Message.text)
    assert Message.text in "Dropped!"
    if Message.text == "Dropped!":
        print("Pass")
    else:
        print("Fail")

    time.sleep(5)
    dragg = driver.find_element(By.ID, "dragBox")
    dropp = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div[2]/div/p")
    Action = ActionChains(driver)
    ActionChains(driver).drag_and_drop(dragg, dropp).perform()
    time.sleep(5)
    Message = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div[2]/div[2]/div/p")
    print(Message.text)
    assert Message.text in "Dropped!"
    if Message.text == "Dropped!":
        print("Pass")
    else:
        print("Fail")

def revert():
    driver.find_element(By.ID, "droppableExample-tab-revertable").click()
    # time.sleep(5)
    dragg = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[4]/div/div[1]/div[1]")
    dropp = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[4]/div/div[2]")
    Action = ActionChains(driver)
    ActionChains(driver).drag_and_drop(dragg, dropp).perform()
    # time.sleep(5)
    Message = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[4]/div/div[2]/p")
    print(Message.text)
    assert Message.text in "Dropped!"
    if Message.text == "Dropped!":
        print("Pass")
    else:
        print("Fail")

    dragg = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[4]/div/div[1]/div[2]")
    dropp = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[4]/div/div[2]")
    Action = ActionChains(driver)
    ActionChains(driver).drag_and_drop(dragg, dropp).perform()
    # time.sleep(5)
    Message = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div/div[4]/div/div[2]/p")
    print(Message.text)
    assert Message.text in "Dropped!"
    if Message.text == "Dropped!":
        print("Pass")
    else:
        print("Fail")


simple()
Accept()
Preventpropagation1()
preventprop2()
revert()



