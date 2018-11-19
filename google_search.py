from selenium import webdriver
 
driver = webdriver.Chrome('C:\\chromedriver.exe')
driver.maximize_window()
driver.get("http://www.google.com")
 
elem = driver.find_element_by_name("q")
elem.send_keys("Порошенко")
elem.submit()
 
print(driver.title)