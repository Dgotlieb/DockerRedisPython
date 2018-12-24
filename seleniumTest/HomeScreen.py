from selenium import webdriver

# *********************************************************************************************************************************************************************************************
# selectors erea
body_text_selector = "//body[contains(text(),'Hello World')]"


# *********************************************************************************************************************************************************************************************

class HomeScreen:
    def __init__(self, driver):
        self.driver = driver

    def connect_to_web_site(self, urlAddress):
        self.driver.get(urlAddress)

    def print_body_text(self):
        print(self.driver.find_element_by_xpath(body_text_selector).text)
