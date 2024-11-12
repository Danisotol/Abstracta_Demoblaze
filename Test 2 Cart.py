from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# Sitio de prueba
driver.get("https://www.demoblaze.com/index.html")

wait = WebDriverWait(driver, 10)
products = []

for page in range(1, 3):  # Páginas 1 y 2
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "card-title")))
    product_elements = driver.find_elements(By.CLASS_NAME, "card-title")
    
    for product in product_elements:
        name = product.text
        price = product.find_element(By.XPATH, "../..//h5").text
        link = product.find_element(By.XPATH, "../..//a[@class='hrefch']").get_attribute("href")
        products.append((name, price, link))
    
    try:
        next_button = driver.find_element(By.ID, "next2")
        next_button.click()
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "card-title")))
    except Exception as e:
        print(f"No se pudo encontrar el botón 'Next' o hubo un error al cambiar de página: {e}")
        break

# Seleccionar producto
if products:
    first_product_name, first_product_price, first_product_link = products[0]
    print(f"Seleccionando el producto: {first_product_name} ({first_product_price})")
    driver.get(first_product_link)
    
    # Add to cart
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Add to cart')]")))
    add_to_cart_button.click()
    
    # Alerta de confirmación
    wait.until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print(f"Producto {first_product_name} agregado al carrito.")
    
    driver.get("https://www.demoblaze.com/cart.html")

    # Place Order
    place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Place Order')]")))
    place_order_button.click()

    
    wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("Chocolate Blanco")
    driver.find_element(By.ID, "country").send_keys("Argentina")
    driver.find_element(By.ID, "city").send_keys("Buenos Aires")
    driver.find_element(By.ID, "card").send_keys("1234567890123456")
    driver.find_element(By.ID, "month").send_keys("11")
    driver.find_element(By.ID, "year").send_keys("2025")
    
    # Confirmar orden
    driver.find_element(By.XPATH, "//button[contains(text(),'Purchase')]").click()
    

    confirmation_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "sweet-alert"))).text
    print("Confirmación de compra:")
    print(confirmation_message)
    
    driver.find_element(By.XPATH, "//button[contains(text(),'OK')]").click()

else:
    print("No se encontraron productos para agregar al carrito.")

driver.quit()
