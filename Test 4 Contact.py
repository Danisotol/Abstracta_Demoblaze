from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración de WebDriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Navegar al sitio de prueba
driver.get("https://www.demoblaze.com/index.html")

# Esperar a que la página cargue y hacer clic en el enlace de "Contact"
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Contact"))).click()

# Esperar a que el formulario de contacto aparezca
wait.until(EC.visibility_of_element_located((By.ID, "exampleModal")))

# Llenar el formulario de contacto
wait.until(EC.visibility_of_element_located((By.ID, "recipient-email"))).send_keys("Chocolateblanco@gmail.com")
wait.until(EC.visibility_of_element_located((By.ID, "recipient-name"))).send_keys("Chocolate Blanco")
wait.until(EC.visibility_of_element_located((By.ID, "message-text"))).send_keys("Gracias Abstracta.")

# Hacer clic en el botón "Send message"
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Send message']"))).click()

# Esperar un momento para ver la acción realizada
time.sleep(2)

# Cerrar el navegador
driver.quit()
