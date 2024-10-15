from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcMainPage:

    def __init__(self, browser):
        self.driver = browser
        base_url = "https://bonigarcia.dev/selenium-webdriver-java/"
        self.driver.get(f"{base_url}slow-calculator.html")

    # выставляем время ожидания
    def waiting_time(self, time):
        timeout = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        timeout.clear()
        timeout.send_keys(time)

        return time

    # нажимаем на калькуляторе нужные кнопочки
    def button_of_calc(self, value):
        self.driver.find_element(By.XPATH, f"//span[text()='{value}']").click()

    # ждём и получаем результат для сравнения
    def check_result(self, timeout, expected_value):
        WebDriverWait(self.driver, int(timeout) + 10).until(
            EC.text_to_be_present_in_element((
                By.CLASS_NAME, "screen"), f"{expected_value}"))

        result = self.driver.find_element(By.CLASS_NAME, "screen").text
        return result
