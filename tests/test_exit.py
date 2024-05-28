from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *


# Выход из аккаунта
class TestExit:
    # Выход по кнопке "Выйти" в личном кабинете
    def test_exit_from_profile(self, driver):
        driver.get(MAIN_PAGE)
        driver.find_element(*LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*EMAIL_INPUT).send_keys('vadim_yakovlev_9@yandex.ru')
        driver.find_element(*PASSWORD_INPUT).send_keys('qwe7rty4')
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PROFILE_BUTTON)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MENU_EXIT_BUTTON)).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))

        assert driver.find_element(*LOGIN_BUTTON).is_displayed() and driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()
