from locators import *
from data import *

# Раздел "Конструктор"
class TestConstructor:
    # Переход к разделу "Соусы"
    def test_sauce_button(self, driver):
        driver.get(MAIN_PAGE)
        driver.find_element(*SAUCE_BUTTON).click()

        assert 'tab_tab_type_current__2BEPc' in driver.find_element(*SAUCE_BUTTON).get_attribute('class')

    # Переход к разделу "Начинки"
    def test_fillings_button(self, driver):
        driver.get(MAIN_PAGE)
        driver.find_element(*FILLINGS_BUTTON).click()

        assert 'tab_tab_type_current__2BEPc' in driver.find_element(*FILLINGS_BUTTON).get_attribute('class')

    # Переход к разделу "Булки"
    def test_bun_button(self, driver):
        driver.get(MAIN_PAGE)
        driver.find_element(*FILLINGS_BUTTON).click()
        driver.find_element(*BUN_BUTTON).click()

        assert 'tab_tab_type_current__2BEPc' in driver.find_element(*BUN_BUTTON).get_attribute('class')
