from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for button in range(5):
    element_button = driver.find_element(
        By.XPATH, '//button[text()="Add Element"]').click()

delete_buttons = driver.find_elements(
    By.XPATH, '//button[text()="Delete"]')

print(len(delete_buttons))
