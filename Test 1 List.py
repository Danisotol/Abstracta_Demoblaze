from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración de WebDriver (asegúrate de tener el ChromeDriver instalado y en tu PATH)
driver = webdriver.Chrome()

# Navegar al sitio de prueba
driver.get("https://www.demoblaze.com/index.html")

# Esperar a que los productos estén cargados en la página
wait = WebDriverWait(driver, 10)
products = []

for page in range(1, 3):  # Página 1 y Página 2
    # Esperar que los productos se carguen antes de extraerlos
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "card-title")))

    # Extraer detalles de los productos
    product_elements = driver.find_elements(By.CLASS_NAME, "card-title")
    
    for product in product_elements:
        name = product.text
        
        # Buscar el precio en un <h5>, ajustando el selector para que se acceda al precio correspondiente
        price = product.find_element(By.XPATH, "../..//h5").text  # Esto busca el precio relacionado con el producto
        
        # Obtener el enlace del producto correctamente (accediendo al <a> con la clase 'hrefch')
        link = product.find_element(By.XPATH, "../..//a[@class='hrefch']").get_attribute("href")
        
        # Agregar los detalles del producto a la lista
        products.append((name, price, link))

    # Navegar a la siguiente página
    try:
        # Busca el botón de 'Next' para avanzar a la siguiente página
        next_button = driver.find_element(By.ID, "next2")
        next_button.click()
        
        # Esperar que la nueva página cargue
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "card-title")))
    except Exception as e:
        print(f"No se pudo encontrar el botón 'Next' o hubo un error al cambiar de página: {e}")
        break  # Si no hay un botón 'Next', detener el ciclo

# Guardar la información en un archivo de texto
with open("product_info.txt", "w") as f:
    for product in products:
        f.write(f"Product Name: {product[0]}\n")
        f.write(f"Price: {product[1]}\n")
        f.write(f"Link: {product[2]}\n\n")

# Cerrar el navegador
driver.quit()
