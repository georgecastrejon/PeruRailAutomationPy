import time

from selenium.webdriver.common.by import By

base_url = "https://www.perurail.com/"


class PeruRail:
    def __init__(self, driver):
        self.driver = driver
        #capturar los webelement usando xpath
        self.tTravel = "//label[@for='oneway']//span"
        self.tFrom = "//select[@id='Filtros_Ida_Origen']//option[@value='6022']"
        self.tTo = "//select[@id='Filtros_Ida_Destino']//option[@value='6028']"
        self.cTrain = "//select[@id='cbTrenSelect']//option[@value='1']"
        self.cld = "//input[@id='Filtros_Ida_Fecha']"
        self.selecCld = "//td[@data-month='11' and @data-year='2022']//a[text()='27']"
        self.button_search = "//button[@id='btn_search']"

    def get_tTravel(self):
        return self.driver.find_element(By.XPATH, self.tTravel)

    def get_tFrom(self):
        return self.driver.find_element(By.XPATH, self.tFrom)

    def get_tTo(self):
        return self.driver.find_element(By.XPATH, self.tTo)

    def get_cTrain(self):
        return self.driver.find_element(By.XPATH, self.cTrain)

    def get_cld(self):
        return self.driver.find_element(By.XPATH, self.cld)

    def get_selecCld(self):
        return self.driver.find_element(By.XPATH, self.selecCld)

    def get_button_search(self):
        return self.driver.find_element(By.XPATH, self.button_search)

#funciones de las acciones en las paginas

    def click_tTravel(self):
        self.get_tTravel().click()
        time.sleep(3)

    def click_tFrom(self):
        self.get_tFrom().click()
        time.sleep(3)

    def click_tTo(self):
        self.get_tTo().click()
        time.sleep(3)

    def click_cTrain(self):
        self.get_cTrain().click()
        time.sleep(3)

    def click_cld(self):
        self.get_cld().click()
        time.sleep(5)

    def click_selecCld(self):
        self.get_selecCld().click()
        time.sleep(5)

    def click_button_search(self):
        self.get_button_search().click()
        time.sleep(3)

    # def switch_to_window(driver):
    #   driver.switch_to_window(driver.window_handles[1])
    #  time.sleep(10)

    @staticmethod
    def get_base_url():
        return base_url
