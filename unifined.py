import os

#  A.Redis app

def redis_app_screen_test():
    # set driver for actions
    initializeDriver = InitializeDriver()
    driver_for_actions = initializeDriver.get_driver("Chrome")
    driver_for_actions.maximize_window()

    # Enter to website
    homeScreen = HomeScreen(driver_for_actions)
    homeScreen.connect_to_web_site("http://localhost:5000/")
    homeScreen.print_body_text()
    # notification for test finish succsefuly
    print("redis_app_screen_test finish succsefuly!")

    # close the window and the session for next test
    driver_for_actions.close()
    driver_for_actions.quit()


def main():
    redis_app_screen_test()

if __name__ == "__main__":
    main()




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





class InitializeDriver:

    def get_driver(self, browserType):

        dirname = os.path.dirname(__file__)


        if browserType == "Chrome":
            filename = os.path.join(dirname, 'chromedriver')
            driver = webdriver.Chrome(executable_path=filename)
            driver.implicitly_wait(10)

        return driver



