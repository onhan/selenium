from selenium import webdriver

driver = webdriver.Chrome('C:\\chromedriver.exe')
driver.maximize_window()
driver.get("https://ua.sinoptik.ua/погода-київ/10-днів");

file = open(r"C:\captures.html", "w")
file.write("<!DOCTYPE html><html><head></head><body width=\"600px\">")

file.write("<img src=\"data:image/png;base64,")
file.write(driver.get_screenshot_as_base64())
file.write("\">")

file.write("</body></html>")
file.close()

driver.quit()