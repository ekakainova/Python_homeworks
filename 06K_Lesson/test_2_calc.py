from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

driver.maximize_window()

waiting_time = driver.find_element(By.CSS_SELECTOR, "#delay")
waiting_time.clear()
waiting_time.send_keys("45")

# нажимаем на калькуляторе нужные кнопочки
driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()

# ждем прежде чем проверить результат
WebDriverWait(driver, 50).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

# сравним результат
def check_result():
    expectation_result = "15"
    result = driver.find_element(By.CLASS_NAME, "screen").text
    assert result == expectation_result

def test_result():
    check_result()

    driver.quit()
