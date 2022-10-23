from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# First we tell the bot what page it should get
# driver = webdriver.Safari()
service = Service(executable_path="./ChromeDriver/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get('https://sede.administracionespublicas.gob.es/pagina/index/directorio/icpplus')
driver.maximize_window()
time.sleep(2)

# First Page - Scroll Down and Submit
driver.execute_script("window.scrollBy(0,500)", "")
submit_button = driver.find_element(By.CSS_SELECTOR, '[name="submit"]')
submit_button.click()

# Second Page - Select a Spain Province
# Takes the select form and choose Alicante
find_province = \
driver.find_element(By.ID, 'form')
select_province = Select(find_province)
select_province.select_by_visible_text("Alicante")
time.sleep(5)
# Clicks on submit button
accept_button = driver.find_element(By.ID, 'btnAceptar')
accept_button.click()

# Third Page
# Takes the select form (Only at Police Station by now)
find_procedure = \
driver.find_element(By.ID, 'tramiteGrupo[1]')
select_procedure = Select(find_procedure)
select_procedure.select_by_index('1')
time.sleep(5)


