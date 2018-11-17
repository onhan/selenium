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







































# from selenium import webdriver 
# from selenium.webdriver.common.keys import Keys 
# from selenium.webdriver.common.by import By 
# import time 

# driver = webdriver.Chrome('C:\\chromedriver.exe')
# browser.get('http://gmail.com') 
# action = webdriver.ActionChains(browser) 
# emailElem = browser.find_element_by_id('artem.shmahun@gmail.com') 
# emailElem.send_keys("MyUserName") 
# browser.find_element_by_name('signIn').click() 
# #browser.get('https://accounts.google.com/ServiceLogin?   service=mail&continue=https://mail.google.com/mail/#password') 
# passwordElem = browser.find_element_by_id('Artem070689') 
# passwordElem.send_keys("MyPassword") 
# browser.find_element_by_name('signIn').click() 

# # from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys

# # driver = webdriver.Chrome('C:\\chromedriver.exe')
# # driver.maximize_window()

# # browser.get('https://mail.google.com')
# # browser.implicitly_wait(3)

# # email = browser.find_element_by_id('Email')
# # email.send_keys('artem.shmahun@gmail.com')
# # email.send_keys(Keys.ENTER)

# # pw = browser.find_element_by_id('Passwd')
# # pw.send_keys('Artem070689')
# # pw.send_keys(Keys.ENTER)

# # from selenium import webdriver
# # from bs4 import BeautifulSoup
# # import time
 
# # EMAIL = 'artem.shmahun@gmail.com'
# # PASSWORD = 'Artem070689'
# # CHROMEPATH = 'C:\\chromedriver.exe'
 
# # login_url = 'https://www.google.com/accounts/Login'
# # browser = webdriver.Chrome('C:\\chromedriver.exe')
# # browser.set_window_position(0,0)
# # browser.get(login_url)
# # time.sleep(2)
# # browser.find_element_by_id("identifierId").send_keys(artem.shmahun@gmail.com)
# # browser.find_element_by_id("identifierNext").click()
# # time.sleep(2)
# # browser.find_element_by_name("password").send_keys(Artem070689)
# # browser.find_element_by_id("passwordNext").click()
# # time.sleep(2)
 
# # soup = BeautifulSoup(browser.page_source, 'html.parser')

# 