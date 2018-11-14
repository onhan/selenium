from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.google.co.uk");

file = open(r"C:\captures.html", "w")
file.write("<!DOCTYPE html><html><head></head><body width=\"600px\">")

file.write("<img src=\"data:image/png;base64,")
file.write(driver.get_screenshot_as_base64())
file.write("\">")

file.write("</body></html>")
file.close()

driver.quit()