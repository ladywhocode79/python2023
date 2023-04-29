import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Applications/Sonal/selenium/drivers/chromedriver_mac64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
#driver = webdriver.Chrome(executable_path="/Applications/Sonal/selenium/drivers/chromedriver_mac64/chromedrive")

driver.maximize_window()
driver.get("https://demoqa.com/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()

#xpath
driver.find_element(By.XPATH, "//h5[text()='Elements']").click()

#xpath
driver.find_element(By.XPATH,"//span[text()='Text Box']").click()

#id
driver.find_element(By.ID,"userName").send_keys("sonal")

#xpath
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("sonal@infog.com")

#css selector
driver.find_element(By.CSS_SELECTOR,"textarea[placeholder='Current Address']").send_keys("abcdeh")

driver.find_element(By.ID,"permanentAddress").send_keys("abcdeh-fhfhfh")

#by name

#by id
driver.find_element(By.ID,"submit").click()

name=driver.find_element(By.ID,"name").text
email=driver.find_element(By.ID,"email").text
adress1= driver.find_element(By.CSS_SELECTOR,"#currentAddress").text

time.sleep(2)

print(name)
print(email)
print(adress1)


assert "sonal" in name

assert "sonal@infog.com" in email

#driver.close()


