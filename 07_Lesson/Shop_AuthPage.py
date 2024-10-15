from selenium.webdriver.common.by import By


# авторизация как standart_user
class Authorization:

    def __init__(self, browser):
        self.driver = browser
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        self.box_name = (By.ID, "user-name")
        self.box_secret_word = (By.ID, "password")
        self.button_of_log = (By.ID, "login-button")

    def box_username(self, name_of_user):
        username = self.driver.find_element(*self.box_name)
        username.clear()
        username.send_keys(name_of_user)

    def box_password(self, password_of_user):
        password = self.driver.find_element(*self.box_secret_word)
        password.clear()
        password.send_keys(password_of_user)

    def login_button(self):
        self.driver.find_element(*self.button_of_log).click()
