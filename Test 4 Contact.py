from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Sitio de prueba
driver.get("https://www.demoblaze.com/index.html")

# Contact
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Contact"))).click()

wait.until(EC.visibility_of_element_located((By.ID, "exampleModal")))

wait.until(EC.visibility_of_element_located((By.ID, "recipient-email"))).send_keys("Chocolateblanco@gmail.com")
wait.until(EC.visibility_of_element_located((By.ID, "recipient-name"))).send_keys("Chocolate Blanco")
wait.until(EC.visibility_of_element_located((By.ID, "message-text"))).send_keys("Gracias Abstracta.")

# Send message
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Send message']"))).click()

time.sleep(2)

driver.quit()
