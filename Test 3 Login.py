from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración de WebDriver
driver = webdriver.Chrome()

# Navegar al sitio de prueba
driver.get("https://www.demoblaze.com/index.html")

# Esperar a que el botón "Log in" esté visible y hacer clic
wait = WebDriverWait(driver, 10)
login_button = wait.until(EC.element_to_be_clickable((By.ID, "login2")))
login_button.click()

# Esperar a que se abra el modal de login
wait.until(EC.visibility_of_element_located((By.ID, "logInModal")))

# Ingresar el nombre de usuario
username_input = driver.find_element(By.ID, "loginusername")
username_input.send_keys("Chocolate Blanco")

# Ingresar la contraseña
password_input = driver.find_element(By.ID, "loginpassword")
password_input.send_keys("Chocolate")

# Hacer clic en el botón "Log in" del modal
login_modal_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]")
login_modal_button.click()

# Esperar un momento para asegurarse de que el login se complete
time.sleep(2)

# Verificar si el usuario está logueado, por ejemplo, comprobando la presencia del nombre de usuario en la página
try:
    user_welcome = wait.until(EC.visibility_of_element_located((By.ID, "nameofuser")))
    print("Log in exitoso. Usuario:", user_welcome.text)
except:
    print("Error al iniciar sesión.")

# Cerrar el navegador
driver.quit()
