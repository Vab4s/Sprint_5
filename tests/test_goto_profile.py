from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *


# Переход в личный кабинет
class TestToProfile:
    # Переход по клику на "Личный кабинет" без входа в аккаунт
    def test_main_page_open_profile_without_login(self, driver):
        driver.get(MAIN_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(PROFILE_BUTTON)).click()

        assert driver.current_url == LOGIN_PAGE
        driver.quit()

    # Переход по клику на "Личный кабинет" со входом в аккаунт
    def test_main_page_open_profile_with_login(self, driver):
        driver.get(MAIN_PAGE)
        driver.find_element(*LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*EMAIL_INPUT).send_keys('vadim_yakovlev_9@yandex.ru')
        driver.find_element(*PASSWORD_INPUT).send_keys('qwe7rty4')
        driver.find_element(*LOGIN_BUTTON).click()
        driver.find_element(*PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MENU_PROFILE_LINK))

        assert driver.find_element(*MENU_PROFILE_LINK).is_displayed() and driver.current_url == PROFILE_PAGE
        driver.quit()
