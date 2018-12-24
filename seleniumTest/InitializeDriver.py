import os

from selenium import webdriver


class InitializeDriver:

    def get_driver(self, browserType):

        dirname = os.path.dirname(__file__)


        if browserType == "Chrome":
            filename = os.path.join(dirname, 'chromedriver')
            driver = webdriver.Chrome(executable_path=filename)
            driver.implicitly_wait(10)

        return driver





####### for windows change to below code :########


        # if browserType == "Chrome":
        #     filename = os.path.join(dirname, 'seleniumTest/chromedriver.exe')
        #     driver = webdriver.Chrome(executable_path=filename)
        #     driver.implicitly_wait(10)
        #
        #
        # elif browserType == "FireFox":
        #     filename = os.path.join(dirname, 'seleniumTest/geckodriver.exe')
        #     driver = webdriver.Chrome(executable_path=filename)
        #     driver.implicitly_wait(10)
        #
        # # set default browser
        # else:
        #     filename = os.path.join(dirname, 'seleniumTest/chromedriver.exe')
        #     driver = webdriver.Chrome(executable_path="seleniumTest/chromedriver.exe")
        #     driver.implicitly_wait(10)