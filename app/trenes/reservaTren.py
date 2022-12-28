from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome(executable_path=r"C:\driver_chrome\chromedriver.exe")

driver.implicitly_wait(0.5)

driver.maximize_window()

driver.get("https://www.perurail.com/")

tTravel = driver.find_element(By.XPATH, "//label[@for='oneway']//span")
tTravel.click()
time.sleep(2)
tFrom = driver.find_element(By.XPATH, "//select[@id='Filtros_Ida_Origen']//option[@value='6022']")
tFrom.click()
time.sleep(2)
tTo = driver.find_element(By.XPATH, "//select[@id='Filtros_Ida_Destino']//option[@value='6026']")
tTo.click()


time.sleep(3)
driver.quit()



