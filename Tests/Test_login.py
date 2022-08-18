import time
from PytestDemo.Pages.test_login_page import Login_Page
from PytestDemo.Pages.test_Homepage import HomePage
from selenium import webdriver


class test_LoginTest:
    def __init__(self):
        self.driver = webdriver.Chrome("C:\\Users\\Kunal\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        time.sleep(3)

        Login = Login_Page(driver)
        Login.enter_username("Admin")
        Login.enter_password("admin123")
        Login.click_login_button()

        welcome = HomePage(driver)
        welcome.click_welcome_link()
        welcome.click_logout()

    time.sleep(2)
