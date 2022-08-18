from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = "welcome"
        self.logout_button_XPATH = '//*[@id="welcome-menu"]/ul/li[3]/a'

    def click_welcome_link(self):
        self.driver.find_element(By.ID,self.welcome_link_id).click()

    def click_logout(self):
        self.find_by_element(By.XPATH,self.logout_button_XPATH).click()
