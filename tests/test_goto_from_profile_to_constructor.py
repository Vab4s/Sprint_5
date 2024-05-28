from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *


# Переход из личного кабинета в конструктор
class TestFromProfileToConstructor:
    # Переход из личного кабинета в конструктор по клику на "Конструктор"
    def test_from_profile_page_open_constructor_with_press_constructor_button(self, driver):
        driver.get(MAIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGIN_TO_ACCOUNT_BUTTON)).click()
        driver.find_element(*EMAIL_INPUT).send_keys('vadim_yakovlev_9@yandex.ru')
        driver.find_element(*PASSWORD_INPUT).send_keys('qwe7rty4')
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PROFILE_BUTTON)).click()
        driver.find_element(*CONSTRUCTOR_BUTTON).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()

    # Переход из личного кабинета в конструктор по клику логотип Stellar Burgers
    def test_from_profile_page_open_constructor_with_press_logo(self, driver):
        driver.get(MAIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PROFILE_BUTTON)).click()
        driver.find_element(*LOGO_LINK).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()
