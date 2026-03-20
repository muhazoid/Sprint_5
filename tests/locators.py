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
    TEXT_LOGIN = (By.CLASS_NAME, 'Auth_link__1fOlj')


class MainPageLocators:
    BUTTON_LOGIN = (By.XPATH, ".//button[text() = 'Войти в аккаунт']") #Кнопка войти в аккаунт
    BUTTON_ORDER = (By.XPATH, './/button[text()="Оформить заказ"]')
    TEXT_PROFILE = (By.XPATH, './/p[text()="Личный Кабинет"]')
    TEXT_CONSTRUCTOR = (By.XPATH, './/p[text()="Конструктор"]')
    TAB_BUNS = (By.XPATH, './/span[text()="Булки"]/parent::*')
    TAB_SAUCES = (By.XPATH, './/span[text()="Соусы"]/parent::*')
    TAB_FILLINGS = (By.XPATH, './/span[text()="Начинки"]/parent::*')
    LOGO = (By.XPATH, './/div[@class="AppHeader_header__logo__2D0X2"]')
   

class LoginPage:
    TITLE_TEXT = (By.XPATH, './/h2[text()="Вход"]')
    BUTTON_LOGIN = (By.XPATH, './/button[text()="Войти"]')
    FIELD_EMAIL = (By.XPATH, './/label[text()="Email"]//parent::*/input')
    FIELD_PASSWORD = (By.XPATH, './/input[@type="password"]')


class RecoverPageLocators:
    LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")  # Ссылка "Войти" на странице восстановления


class ProfilePageLocators:
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # Кнопка "Выйти"
    PROFILE_LINK = (By.XPATH, ".//a[text()='Профиль']")  # Ссылка на профиль (активная)

    