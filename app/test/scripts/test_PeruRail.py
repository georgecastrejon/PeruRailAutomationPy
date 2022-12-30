import time
from app.src.POM.Pages import peruRail
from app.src.TestBase.base import WebDriverSetup
from app.src.POM.Pages.peruRail import PeruRail


class Test_peruRail(WebDriverSetup):
    def test_homePage(self):
        driver = self.driver
        self.driver.get(PeruRail.get_base_url())
        peruRail = PeruRail(driver)
        time.sleep(3)
        peruRail.click_tTravel()
        peruRail.click_tFrom()
        peruRail.click_tTo()
        peruRail.click_cTrain()
        peruRail.click_cld()
        peruRail.click_selecCld()
        peruRail.click_button_search()
        peruRail.click_expand()
        peruRail.click_fecha()
        peruRail.click_dia()
        # peruRail.click_bus()

