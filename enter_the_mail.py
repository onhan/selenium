from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

driver = webdriver.Chrome('C:\\chromedriver.exe')
driver.maximize_window()
driver.get("https://accounts.google.com/signin")

driver.implicitly_wait(1)
driver.find_element_by_id("identifierId").send_keys("********@gmail.com")
driver.find_element_by_id("identifierNext").click()

driver.implicitly_wait(3)
password = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
password = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]/div/div[1]/div/div[1]/input")
password.send_keys("************")

element = driver.find_element_by_id('passwordNext')
driver.execute_script("arguments[0].click();", element)