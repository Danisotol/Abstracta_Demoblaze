from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# Sitio de prueba
driver.get("https://www.demoblaze.com/index.html")

#
wait = WebDriverWait(driver, 10)
login_button = wait.until(EC.element_to_be_clickable((By.ID, "login2")))
login_button.click()

# Login
wait.until(EC.visibility_of_element_located((By.ID, "logInModal")))

username_input = driver.find_element(By.ID, "loginusername")
username_input.send_keys("Chocolate Blanco")

password_input = driver.find_element(By.ID, "loginpassword")
password_input.send_keys("Chocolate")

login_modal_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")
login_modal_button.click()

time.sleep(2)

try:
    user_welcome = wait.until(EC.visibility_of_element_located((By.ID, "nameofuser")))
    print("Log in exitoso. Usuario:", user_welcome.text)
except:
    print("Error al iniciar sesión.")


driver.quit()
