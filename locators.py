from selenium.webdriver.common.by import By


class Urls:
    SERVICE_BASE_URL = 'https://stellarburgers.education-services.ru'  # Базовый URL сервиса
    main_page = f'{SERVICE_BASE_URL}/'  # Главная страница
    registration_page = f'{SERVICE_BASE_URL}/register'  # Страница регистрации
    login_page = f'{SERVICE_BASE_URL}/login'  # Страница входа
    profile_page = f'{SERVICE_BASE_URL}/account/profile'  # Страница профиля пользователя
    forgot_password_page = f'{SERVICE_BASE_URL}/forgot-password'  # Страница восстановления пароля


class RegisterPageLocators:
    FIELD_NAME = (By.XPATH, './/label[text()="Имя"]//parent::*/input')  # Поле ввода имени
    FIELD_EMAIL = (By.XPATH, './/label[text()="Email"]//parent::*/input')  # Поле ввода email
    FIELD_PASSWORD = (By.XPATH, './/label[text()="Пароль"]//parent::*/input')  # Поле ввода пароля
    BUTTON_REGISTER = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    ERROR_INCORRECT_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']")  # Сообщение об ошибке "Некорректный пароль"
    ERROR_USER_EXISTING = (By.XPATH, ".//p[text()='Такой пользователь уже существует']")  # Сообщение об ошибке "Такой пользователь уже существует"
    TEXT_LOGIN = (By.CLASS_NAME, 'Auth_link__1fOlj')  # Ссылка "Войти" на странице регистрации


class MainPageLocators:
    BUTTON_LOGIN = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной
    BUTTON_ORDER = (By.XPATH, './/button[text()="Оформить заказ"]')  # Кнопка "Оформить заказ"
    TEXT_PROFILE = (By.XPATH, './/p[text()="Личный Кабинет"]')  # Ссылка/текст "Личный Кабинет" в шапке
    TEXT_CONSTRUCTOR = (By.XPATH, './/p[text()="Конструктор"]')  # Ссылка/текст "Конструктор" в шапке
    TAB_BUNS = (By.XPATH, './/span[text()="Булки"]/parent::*')  # Вкладка "Булки" в конструкторе
    TAB_SAUCES = (By.XPATH, './/span[text()="Соусы"]/parent::*')  # Вкладка "Соусы" в конструкторе
    TAB_FILLINGS = (By.XPATH, './/span[text()="Начинки"]/parent::*')  # Вкладка "Начинки" в конструкторе
    TAB_ACTIVE = (By.XPATH, './/div[contains(@class, "tab_tab_type_current")]')  # Активная (подсвеченная) вкладка
    LOGO = (By.XPATH, './/div[@class="AppHeader_header__logo__2D0X2"]')  # Логотип Stellar Burgers (кликабельный)
    
   

class LoginPage:
    TITLE_TEXT = (By.XPATH, './/h2[text()="Вход"]')  # Заголовок страницы "Вход"
    BUTTON_LOGIN = (By.XPATH, './/button[text()="Войти"]')  # Кнопка "Войти" на странице входа
    FIELD_EMAIL = (By.XPATH, './/label[text()="Email"]//parent::*/input')  # Поле ввода email на странице входа
    FIELD_PASSWORD = (By.XPATH, './/input[@type="password"]')  # Поле ввода пароля на странице входа


class RecoverPageLocators:
    LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")  # Ссылка "Войти" на странице восстановления пароля

class ProfilePageLocators:
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # Кнопка "Выйти"
    PROFILE_LINK = (By.XPATH, ".//a[text()='Профиль']")  # Ссылка на профиль (активная)

