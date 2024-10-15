from Form_MainPage import MainPage
from Form_ResultPage import ResultPage
from Calc_MainPage import CalcMainPage
from Shop_AuthPage import Authorization
from Shop_ProductsPage import Products
from Shop_CartPage import Cart
from Shop_BuyerFormPage import BuyerForm
from Shop_OverviewPage import Checkout_Overview

import pytest


# автотест на заполнение формы
@pytest.mark.form_test
def test_form(driver):

    main_page = MainPage(driver)
    main_page.input_name("Иван")
    main_page.input_surname("Петров")
    main_page.input_address("Ленина, 55-3")
    main_page.input_e_mail("test@skypro.com")
    main_page.input_phone_number("+7985899998787")
    main_page.input_zip_code("")
    main_page.input_city("Москва")
    main_page.input_country("Россия")
    main_page.input_job_position("QA")
    main_page.input_company("SkyPro")
    main_page.button_submit()

    red_color = "rgba(245, 194, 199, 1)"
    green_color = "rgba(186, 219, 204, 1)"

    result_page = ResultPage(driver)
    wrong_color = result_page.alert_color()
    right_color = result_page.success_color()

    assert red_color == wrong_color, f'''
    Поле Zip Code должно подсвечиваться красным,
    а оно подсвечивается цветом {wrong_color}'''

    assert green_color == right_color, f'''
    Остальные поля должны подсвечиваться зеленым,
    а они подсвечваются цветом {right_color}'''


# автотест на калькулятор
@pytest.mark.calculator_test
def test_calculator(driver):

    calc_main_page = CalcMainPage(driver)
    timeout = calc_main_page.waiting_time("45")
    calc_main_page.button_of_calc("7")
    calc_main_page.button_of_calc("+")
    calc_main_page.button_of_calc("8")
    calc_main_page.button_of_calc("=")
    result = calc_main_page.check_result(timeout, "15")

    expectation_result = "15"

    assert result == expectation_result, f'''
    Текущий и ожидаемый результат не совпадают,
    текущий результат равен {result}'''


# автотест на интернет-магазин
@pytest.mark.online_shop
def test_shop(driver):

    shop_auth = Authorization(driver)
    shop_auth.box_username("standard_user")
    shop_auth.box_password("secret_sauce")
    shop_auth.login_button()

    shop_product = Products(driver)
    shop_product.button_add_product("Sauce Labs Backpack")
    shop_product.button_add_product("Sauce Labs Bolt T-Shirt")
    shop_product.button_add_product("Sauce Labs Onesie")
    shop_product.shopping_cart()

    shop_cart = Cart(driver)
    shop_cart.button_checkout()

    shop_buyer = BuyerForm(driver)
    shop_buyer.buyer_name("Андрей")
    shop_buyer.buyer_surname("Петров")
    shop_buyer.buyer_zip("123456")
    shop_buyer.button_continue()

    shop_overview = Checkout_Overview(driver)
    total_sum = shop_overview.total()

    expected_total_sum = "Total: $58.29"

    assert total_sum == expected_total_sum, f'''
    Итоговая сумма не соотвествует ожидаемой и равна {total_sum}'''
