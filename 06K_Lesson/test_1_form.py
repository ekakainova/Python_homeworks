from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

driver.maximize_window()

# заполняем форму данными
first_name = driver.find_element(By.NAME, "first-name")
first_name.clear()
first_name.send_keys("Иван")

last_name = driver.find_element(By.NAME, "last-name")
last_name.clear()
last_name.send_keys("Петров")

address = driver.find_element(By.NAME, "address")
address.clear()
address.send_keys("Ленина, 55-3")

mail = driver.find_element(By.NAME, "e-mail")
mail.clear()
mail.send_keys("test@skypro.com")

phone = driver.find_element(By.NAME, "phone")
phone.clear()
phone.send_keys("+7985899998787")

zip_code = driver.find_element(By.NAME, "zip-code")
zip_code.clear()

city = driver.find_element(By.NAME, "city")
city.clear()
city.send_keys("Москва")

country = driver.find_element(By.NAME, "country")
country.clear()
country.send_keys("Россия")

job_position = driver.find_element(By.NAME, "job-position")
job_position.clear()
job_position.send_keys("QA")

company = driver.find_element(By.NAME, "company")
company.clear()
company.send_keys("SkyPro")

# нажимаем на кнопку Submit
driver.find_element(By.XPATH, "//button[text()='Submit']").click()

red_color = "rgba(245, 194, 199, 1)"
green_color = "rgba(186, 219, 204, 1)"


# проверяем на красный цвет
def alert_color():
    color_of_zip_code = driver.find_element(
        By.ID, "zip-code").value_of_css_property("border-bottom-color")
    assert red_color == color_of_zip_code


# проверяем на зеленый цвет все остальные поля
def success_color():
    rest_elements = driver.find_elements(By.CLASS_NAME, "alert-success")
    for element in rest_elements:
        color_of_element = element.value_of_css_property("border-bottom-color")
        assert green_color == color_of_element


# вызываем проверки на цвет
def test_form():
    alert_color()
    success_color()

    driver.quit()
