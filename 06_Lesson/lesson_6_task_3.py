from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

driver.maximize_window()

waiter = WebDriverWait(driver, 15)
waiter.until(EC.visibility_of_element_located((By.ID, "landscape")))

src_of_third_picture = driver.find_element(By.ID, "award").get_attribute("src")
print(src_of_third_picture)

driver.quit()
