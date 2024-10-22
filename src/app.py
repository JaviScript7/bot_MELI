from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
from search_text import buscar_coincidencias

# Configura las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecutar Chrome en modo headless
chrome_options.add_argument("--no-sandbox")  # Necesario para entornos como Docker
chrome_options.add_argument("--disable-dev-shm-usage")  # Evita problemas con la memoria compartida

# Configura el controlador de Chrome
driver = webdriver.Chrome(options=chrome_options)

# URL de la categoría en Mercado Libre
#url = 'https://listado.mercadolibre.com.mx/ropa-bolsas-calzado/abrigos/'
url = 'https://listado.mercadolibre.com.mx/gabardinas-hombre?skipInApp=true'
driver.get(url)

# Esperamos un tiempo para asegurarnos de que la página ha cargado
time.sleep(3)

# Obtenemos el contenido HTML
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Extraemos los productos y precios de la página
products = soup.find_all('h2', class_='poly-component__title')
prices = soup.find_all('span', class_='andes-money-amount')

# Listas para almacenar los datos
product_names = []
product_prices = []

# Recorremos los resultados y extraemos la información
for product, price in zip(products, prices):
    product_names.append(product.get_text())
    product_prices.append(price.get_text())

print(product_names)
print(buscar_coincidencias(product_names))

# Creamos un DataFrame
df = pd.DataFrame({
    'Producto': product_names,
    'Precio': product_prices
})

# Guardamos los datos en un archivo CSV
df.to_csv('productos_selenium.csv', index=False)

print("Datos extraídos y guardados en 'productos_selenium.csv'")

# Cerramos el navegador
driver.quit()
