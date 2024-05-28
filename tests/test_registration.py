from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *


# Регистрация
class TestRegistration:
    # Успешная регистрация
    def test_registration_correct_data(self, login_generator, password_generator, driver):
        driver.get(REGISTRATION_PAGE)
        driver.find_element(*NAME_INPUT).send_keys('AnyUser')
        driver.find_element(*EMAIL_INPUT).send_keys(login_generator)
        driver.find_element(*PASSWORD_INPUT).send_keys(password_generator)
        driver.find_element(*REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGIN_BUTTON))

        assert driver.current_url == LOGIN_PAGE and driver.find_element(*LOGIN_BUTTON)
        driver.quit()

    # Ошибка "Некорректный пароль"
    def test_registration_incorrect_password_error_message(self, login_generator, password_generator, driver):
        driver.get(REGISTRATION_PAGE)
        driver.find_element(*NAME_INPUT).send_keys('AnyUser')
        driver.find_element(*EMAIL_INPUT).send_keys(login_generator)
        driver.find_element(*PASSWORD_INPUT).send_keys(password_generator[:5])
        driver.find_element(*REGISTRATION_BUTTON).click()

        assert driver.current_url == REGISTRATION_PAGE and driver.find_element(*ERROR_MESSAGE).text == "Некорректный пароль"
        driver.quit()
