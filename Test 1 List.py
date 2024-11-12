from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Sitio Web de prueba
driver.get("https://www.demoblaze.com/index.html")

wait = WebDriverWait(driver, 10)
products = []

for page in range(1, 3):  # Páginas 1 y 2
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "card-title")))

    # Detalles de los productos
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

# Guardar en un archivo de texto
with open("product_info.txt", "w") as f:
    for product in products:
        f.write(f"Product Name: {product[0]}\n")
        f.write(f"Price: {product[1]}\n")
        f.write(f"Link: {product[2]}\n\n")

driver.quit()
