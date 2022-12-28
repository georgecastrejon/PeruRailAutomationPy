import unittest
import platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class peru_Rail(unittest.TestCase):

    def setUp(self):
        #usar rutas absolutas, no relativas
        self.driver = webdriver.Chrome(executable_path=r"C:\driver_chrome\chromedriver.exe")

    @unittest.skipUnless(platform.system() == 'Windows', "Solo se ejecuta en Windows")
    def test_peruRail(self):
        driver = self.driver
        #esperar un maximo de 0.5 segundos para encontrar el elemento
        driver.implicitly_wait(0.5)
        driver.maximize_window()
        driver.get("https://www.perurail.com/")
        tTravel = driver.find_element(By.XPATH, "//label[@for='oneway']//span")
        tTravel.click()
        tFrom = driver.find_element(By.XPATH, "//select[@id='Filtros_Ida_Origen']//option[@value='6022']")
        tFrom.click()
        tTo = driver.find_element(By.XPATH, "//select[@id='Filtros_Ida_Destino']//option[@value='6026']")
        tTo.click()
        cld = driver.find_element(By.XPATH, "//input[@id='Filtros_Ida_Fecha']")
        time.sleep(5)
        cld.click()
        time.sleep(5)
        selecCld = driver.find_element(By.XPATH, "//td[@data-month='11' and @data-year='2022']//a[text()='28']")
        selecCld.click()
        time.sleep(3)
        button_search = driver.find_element(By.XPATH, "//button[@id='btn_search']")
        button_search.click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(10)

        #nunca utilizar los implicit ni los timer en un mismo metodo
        #patron POM
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
