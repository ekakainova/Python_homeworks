from selenium.webdriver.common.by import By


class BuyerForm:

    # заполняем форму данными покупателя
    def __init__(self, browser):
        self.driver = browser

        self.box_name = (By.ID, "first-name")
        self.box_surname = (By.ID, "last-name")
        self.box_postal_code = (By.ID, "postal-code")
        self.continue_button = (By.NAME, "continue")

    def buyer_name(self, name):
        first_name = self.driver.find_element(*self.box_name)
        first_name.clear()
        first_name.send_keys(name)

    def buyer_surname(self, surname):
        last_name = self.driver.find_element(*self.box_surname)
        last_name.clear()
        last_name.send_keys(surname)

    def buyer_zip(self, zip_code):
        postal_code = self.driver.find_element(*self.box_postal_code)
        postal_code.clear()
        postal_code.send_keys(zip_code)

    # нажимаем кнопку Continue
    def button_continue(self):
        self.driver.find_element(*self.continue_button).click()
