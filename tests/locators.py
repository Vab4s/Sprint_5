MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'        # Главная страница
LOGIN_PAGE = 'https://stellarburgers.nomoreparties.site/login'  # Страница входа
REGISTRATION_PAGE = 'https://stellarburgers.nomoreparties.site/register'    # Страница регистрации
PROFILE_PAGE = 'https://stellarburgers.nomoreparties.site/account/profile'  # Страница профиля
FORGOT_PASSWORD_PAGE = 'https://stellarburgers.nomoreparties.site/forgot-password'  # Страница восстановления пароля

NAME_INPUT = ('xpath', '//label[text()="Имя"]/following-sibling::input')    # Поле ввода имени
EMAIL_INPUT = ('xpath', '//label[text()="Email"]/following-sibling::input') # Поле ввода адреса почты
PASSWORD_INPUT = ('xpath', '//label[text()="Пароль"]/following-sibling::input')  # Поле ввода пароля

REGISTRATION_BUTTON = ('xpath', '//button[text()="Зарегистрироваться"]')    # Кнопка "Зарегистрироваться"
LOGIN_BUTTON = ('xpath', '//button[text()="Войти"]')          # Кнопка "Войти"
LOGIN_TO_ACCOUNT_BUTTON = ('xpath', '//button[text()="Войти в аккаунт"]')   # Кнопка "Войти в аккаунт"
PROFILE_BUTTON = ('xpath', '//p[text()="Личный Кабинет"]/parent::a')    # Кнопка "Личный Кабинет"
MAKE_ORDER_BUTTON = ('xpath', '//button[text()="Оформить заказ"]')      # Кнопка "Оформить заказ"
CONSTRUCTOR_BUTTON = ('xpath', '//p[text()="Конструктор"]')   # Кнопка "Конструктор"

ENTER_TO_ACCOUNT_LINK = ('xpath', '//a[text()="Войти"]')    # Ссылка "Войти" на странице регистрации
LOGO_LINK = ('xpath', '//div[@class="AppHeader_header__logo__2D0X2"]')    # Ссылка логотипа

MENU_PROFILE_LINK = ('xpath', '//a[text()="Профиль"]')      # Пункт меню личного кабинета "Профиль"
MENU_EXIT_BUTTON = ('xpath', '//button[text()="Выход"]')    # Пункт меню личного кабинета "Выход"

BUN_BUTTON = ('xpath', '//span[text()="Булки"]/parent::div')    # Пункт меню конструктора "Булки"
SAUCE_BUTTON = ('xpath', '//span[text()="Соусы"]/parent::div')  # Пункт меню конструктора "Соусы"
FILLINGS_BUTTON = ('xpath', '//span[text()="Начинки"]/parent::div')  # Пункт меню конструктора "Начинки"

ERROR_MESSAGE = ('xpath', '//p[contains(@class, "input__error")]')  # Сообщение "Некорректный пароль"
