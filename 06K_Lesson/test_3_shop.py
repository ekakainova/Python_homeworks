from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.saucedemo.com/")

driver.maximize_window()

# авторизация как standart_user
username = driver.find_element(By.ID, "user-name")
username.clear()
username.send_keys("standard_user")

password = driver.find_element(By.ID, "password")
password.clear()
password.send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").click()

# добавляем товары в корзину
driver.find_element(By.CSS_SELECTOR,
                    "button#add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CSS_SELECTOR,
                    "button#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.CSS_SELECTOR,
                    "button#add-to-cart-sauce-labs-onesie").click()

# переходим в корзину
driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

# нажимаем на Checkout
driver.find_element(By.ID, "checkout").click()

# заполняем форму данными
first_name = driver.find_element(By.ID, "first-name")
first_name.clear()
first_name.send_keys("Андрей")

last_name = driver.find_element(By.ID, "last-name")
last_name.clear()
last_name.send_keys("Петров")

postal_code = driver.find_element(By.ID, "postal-code")
postal_code.clear()
postal_code.send_keys("123456")

# нажимаем кнопку Continue
driver.find_element(
    By.NAME, "continue").click()

# надем и выведем Total
total_sum = driver.find_element(
    By.CSS_SELECTOR, "div.summary_total_label").text
print(total_sum)

driver.quit()
