from selenium.webdriver.common.by import By


class ResultPage:

    def __init__(self, browser):

        self.driver = browser

    # проверка, что поле Zip Code подсвечивается красным
    def alert_color(self):

        color_of_element = self.driver.find_element(
            By.ID, "zip-code").value_of_css_property("border-bottom-color")
        return color_of_element

    # проверка, что остальные поля подсвечиваются зеленым
    def success_color(self):

        full_elements = self.driver.find_elements(
            By.CLASS_NAME, "alert-success")
        for element in full_elements:
            color_of_element = element.value_of_css_property(
                "border-bottom-color")

            return color_of_element
