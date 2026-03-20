from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
from locators import RegisterPageLocators, Urls
from helpers import generate_unique_email




def test_successful_registration(driver):
    driver.get(Urls.registration_page)
    email = generate_unique_email()
    driver.find_element(*RegisterPageLocators.FIELD_NAME).send_keys("Алексей")
    driver.find_element(*RegisterPageLocators.FIELD_EMAIL).send_keys(email)
    driver.find_element(*RegisterPageLocators.FIELD_PASSWORD).send_keys("12345678")
    driver.find_element(*RegisterPageLocators.BUTTON_REGISTER).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))

    assert driver.current_url == Urls.login_page



def test_registration_incorrect_password(driver):
    driver.get(Urls.registration_page)
    email = generate_unique_email()
    driver.find_element(*RegisterPageLocators.FIELD_NAME).send_keys("Алексей")
    driver.find_element(*RegisterPageLocators.FIELD_EMAIL).send_keys(email)
    driver.find_element(*RegisterPageLocators.FIELD_PASSWORD).send_keys("12345")
    driver.find_element(*RegisterPageLocators.BUTTON_REGISTER).click()

    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(RegisterPageLocators.ERROR_INCORRECT_PASSWORD))
    error_message = driver.find_element(*RegisterPageLocators.ERROR_INCORRECT_PASSWORD)

    assert error_message.text == 'Некорректный пароль'


def test_registration_existing_user(driver):
    driver.get(Urls.registration_page)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.FIELD_NAME))
        
    test_email = generate_unique_email()

    driver.find_element(*RegisterPageLocators.FIELD_NAME).send_keys("Алексей")
    driver.find_element(*RegisterPageLocators.FIELD_EMAIL).send_keys(test_email)
    driver.find_element(*RegisterPageLocators.FIELD_PASSWORD).send_keys("12345678")
    driver.find_element(*RegisterPageLocators.BUTTON_REGISTER).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))

    driver.get(Urls.registration_page)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.FIELD_NAME))
    driver.find_element(*RegisterPageLocators.FIELD_NAME).send_keys("Ольга")
    driver.find_element(*RegisterPageLocators.FIELD_EMAIL).send_keys(test_email)
    driver.find_element(*RegisterPageLocators.FIELD_PASSWORD).send_keys("0987654321")
    driver.find_element(*RegisterPageLocators.BUTTON_REGISTER).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_any_elements_located(RegisterPageLocators.ERROR_USER_EXISTING))
    error = driver.find_element(*RegisterPageLocators.ERROR_USER_EXISTING).text

    assert error == 'Такой пользователь уже существует' 








