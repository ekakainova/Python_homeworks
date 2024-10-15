from selenium.webdriver.common.by import By


class Checkout_Overview:

    def __init__(self, browser):
        self.driver = browser

    # надем и выведем Total
    def total(self):
        total_sum = self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text

        return total_sum
