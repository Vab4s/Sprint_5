from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from data import *


# Вход
class TestLogin:
    # Вход по кнопке "Войти в аккаунт" на главной странице
    def test_main_page_login_button(self, driver):
        driver.get(MAIN_PAGE)
        driver.find_element(*LOGIN_TO_ACCOUNT_BUTTON).click()
        driver.find_element(*EMAIL_INPUT).send_keys(LOGIN_EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(LOGIN_PASSWORD)
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MAKE_ORDER_BUTTON))

        assert driver.find_element(*MAKE_ORDER_BUTTON).is_displayed()

    # Вход через кнопку "Личный кабинет"
    def test_main_page_personal_account_login_button(self, driver):
        driver.get(MAIN_PAGE)
        driver.find_element(*PROFILE_BUTTON).click()
        driver.find_element(*EMAIL_INPUT).send_keys(LOGIN_EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(LOGIN_PASSWORD)
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MAKE_ORDER_BUTTON))

        assert driver.find_element(*MAKE_ORDER_BUTTON).is_displayed()

    # Вход через кнопку в форме регистрации
    def test_registration_page_login_button(self, driver):
        driver.get(REGISTRATION_PAGE)
        driver.find_element(*ENTER_TO_ACCOUNT_LINK).click()
        driver.find_element(*EMAIL_INPUT).send_keys(LOGIN_EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(LOGIN_PASSWORD)
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MAKE_ORDER_BUTTON))

        assert driver.find_element(*MAKE_ORDER_BUTTON).is_displayed()

    # Вход через кнопку в форме восстановления пароля
    def test_forgot_password_page_login_button(self, driver):
        driver.get(FORGOT_PASSWORD_PAGE)
        driver.find_element(*ENTER_TO_ACCOUNT_LINK).click()
        driver.find_element(*EMAIL_INPUT).send_keys(LOGIN_EMAIL)
        driver.find_element(*PASSWORD_INPUT).send_keys(LOGIN_PASSWORD)
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(MAKE_ORDER_BUTTON))

        assert driver.find_element(*MAKE_ORDER_BUTTON)
