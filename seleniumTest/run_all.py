import os

from selenium import webdriver
from selenium.webdriver import FirefoxOptions


opt =FirefoxOption()
opts.add_argument("--headless")
# driver = webdriver.Firefox(executable_path='/home/gilad/Documents/Test/geckodriver')
#driver.implicitly_wait(10)
driver = webdriver.Firefox(fire_fox_option=opts)
#open browser with url of redis app
driver.get("http://localhost:5000/")
driver.maximize_window()

body_text_selector = "//body[contains(text(),'Hello World')]"
print(driver.find_element_by_xpath(body_text_selector).text)

# notification for test finish succsefuly
print("redis_app_screen_test finish succsefuly!")

# close the window and the session for next test
driver.close()
driver.quit()
