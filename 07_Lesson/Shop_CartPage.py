from selenium.webdriver.common.by import By


class Cart:

    def __init__(self, browser):
        self.driver = browser

    def button_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
