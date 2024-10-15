from selenium.webdriver.common.by import By


class MainPage:

    # заполняем форму данными
    def __init__(self, browser):
        self.driver = browser
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        self.box_first_name = (By.NAME, "first-name")
        self.box_last_name = (By.NAME, "last-name")
        self.box_address = (By.NAME, "address")
        self.box_e_mail = (By.NAME, "e-mail")
        self.box_phone_number = (By.NAME, "phone")
        self.box_zip_code = (By.NAME, "zip-code")
        self.box_city = (By.NAME, "city")
        self.box_country = (By.NAME, "country")
        self.box_job_position = (By.NAME, "job-position")
        self.box_company = (By.NAME, "company")
        self.submit_button = (By.XPATH, "//button[text()='Submit']")

    def input_name(self, name):
        first_name = self.driver.find_element(*self.box_first_name)
        first_name.clear()
        first_name.send_keys(name)

    def input_surname(self, surname):
        last_name = self.driver.find_element(*self.box_last_name)
        last_name.clear()
        last_name.send_keys(surname)

    def input_address(self, direction):
        address = self.driver.find_element(*self.box_address)
        address.clear()
        address.send_keys(direction)

    def input_e_mail(self, e_mail):
        mail = self.driver.find_element(*self.box_e_mail)
        mail.clear()
        mail.send_keys(e_mail)

    def input_phone_number(self, phone_number):
        phone = self.driver.find_element(*self.box_phone_number)
        phone.clear()
        phone.send_keys(phone_number)

    def input_zip_code(self, postal_code):
        zip_code = self.driver.find_element(*self.box_zip_code)
        zip_code.clear()
        zip_code.send_keys(postal_code)

    def input_city(self, your_city):
        city = self.driver.find_element(*self.box_city)
        city.clear()
        city.send_keys(your_city)

    def input_country(self, your_country):
        country = self.driver.find_element(*self.box_country)
        country.clear()
        country.send_keys(your_country)

    def input_job_position(self, position):
        job_position = self.driver.find_element(*self.box_job_position)
        job_position.clear()
        job_position.send_keys(position)

    def input_company(self, firm):
        company = self.driver.find_element(*self.box_company)
        company.clear()
        company.send_keys(firm)

    # нажимаем на кнопку Submit
    def button_submit(self):
        self.driver.find_element(*self.submit_button).click()
