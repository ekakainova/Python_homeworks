from selenium.webdriver.common.by import By


class Products:

    def __init__(self, browser):
        self.driver = browser

    # добавляем товары в корзину
    def button_add_product(self, name_of_product):
        name = str.lower(name_of_product)
        name = name.strip().split(" ")
        new_name = ("-").join(name)
        self.driver.find_element(By.CSS_SELECTOR,
                                 f"button#add-to-cart-{new_name}").click()

    # переходим в корзину
    def shopping_cart(self):
        self.driver.get("https://www.saucedemo.com/cart.html")
