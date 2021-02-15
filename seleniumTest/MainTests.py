from seleniumTest.HomeScreen import HomeScreen
from seleniumTest.InitializeDriver import InitializeDriver


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
