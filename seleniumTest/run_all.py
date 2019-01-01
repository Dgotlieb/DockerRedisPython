import os

from selenium import webdriver

#set driver for test
#dirname = os.path.dirname(__file__)
#filename = os.path.join(dirname, 'chromedriver')
driver = webdriver.Chrome(executable_path='usr/bin/chromedriver')
driver.implicitly_wait(10)

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
