from selenium.webdriver.common.by import By


class Urls:
    SERVICE_BASE_URL = 'https://stellarburgers.education-services.ru'
    main_page = f'{SERVICE_BASE_URL}/'
    registration_page = f'{SERVICE_BASE_URL}/register'
    login_page = f'{SERVICE_BASE_URL}/login'
    profile_page = f'{SERVICE_BASE_URL}/account/profile'
    order_history_page = f'{SERVICE_BASE_URL}/account/order-history'
    forgot_password_page = f'{SERVICE_BASE_URL}/forgot-password'


class RegisterPageLocators:
    FIELD_NAME = (By.XPATH, './/label[text()="Имя"]//parent::*/input') # Поле ввода Имени
    FIELD_EMAIL = (By.XPATH, './/label[text()="Email"]//parent::*/input') # Поле ввода Email
    FIELD_PASSWORD = (By.XPATH, './/label[text()="Пароль"]//parent::*/input') # Поле ввода Пароля
    BUTTON_REGISTER = (By.XPATH, ".//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    ERROR_INCORRECT_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']") # Ошибка "Некорректный пароль"
    ERROR_USER_EXISTING  = (By.XPATH, ".//p[text()='Такой пользователь уже существует']") # Ошибка "Такой пользователь уже существует"

