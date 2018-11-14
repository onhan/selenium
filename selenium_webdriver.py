import time
from selenium import webdriver

driver = webdriver.Chrome('C:\\chromedriver.exe')
driver.get('https://hotline.ua/');

time.sleep(5)

search_box = driver.find_element_by_name('q')
search_box.send_keys('iPhone 7')
search_box.submit()

el = driver.find_element_by_link_text("Apple iPhone 7 32GB Black (MN8X2)").click()

time.sleep(5)

driver.quit()
