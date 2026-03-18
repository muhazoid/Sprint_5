from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
from locators import RegisterPageLocators, Urls




def generate_unique_email():
    first_name = "alexey"
    last_name = "chikichev" 
    cohort = "42"
    random_digits = str(random.randint(100, 999))
    login = f"{first_name}_{last_name}_{cohort}_{random_digits}"
    domains = ["yandex.ru", "ya.ru", "gmail.com", "mail.ru"]
    domain = random.choice(domains)
    email = f"{login}@{domain}"
    return email


driver = webdriver.Chrome()
driver.get(Urls.registration_page)
email = generate_unique_email()
driver.find_element(*RegisterPageLocators.FIELD_NAME).send_keys("Алексей")
driver.find_element(*RegisterPageLocators.FIELD_EMAIL).send_keys(email)
print(email)
driver.find_element(*RegisterPageLocators.FIELD_PASSWORD).send_keys("12345678")
driver.find_element(*RegisterPageLocators.BUTTON_REGISTER).click()

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))

assert driver.current_url == Urls.login_page

driver.quit()


driver = webdriver.Chrome()
driver.get(Urls.registration_page)
email = generate_unique_email()
driver.find_element(*RegisterPageLocators.FIELD_NAME).send_keys("Алексей")
driver.find_element(*RegisterPageLocators.FIELD_EMAIL).send_keys(email)
print(email)
driver.find_element(*RegisterPageLocators.FIELD_PASSWORD).send_keys("12345")
driver.find_element(*RegisterPageLocators.BUTTON_REGISTER).click()

WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(RegisterPageLocators.ERROR_INCORRECT_PASSWORD))
error_message = driver.find_element(*RegisterPageLocators.ERROR_INCORRECT_PASSWORD)

assert error_message.text == 'Некорректный пароль'

driver.quit()
