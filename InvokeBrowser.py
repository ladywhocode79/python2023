from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service_obj = Service("/Applications/Sonal/selenium/drivers/chromedriver_mac64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://google.com")
print(driver.title)
print(driver.current_url)
driver.get("https://ubs.com")
driver.minimize_window()
driver.maximize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()

