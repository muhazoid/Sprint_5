from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegisterPageLocators, Urls, LoginPage
from helpers import generate_unique_email
from data import TestData




def test_register_valid_user_success(driver):
    driver.get(Urls.registration_page)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.FIELD_NAME))
    driver.find_element(*RegisterPageLocators.FIELD_NAME).send_keys(TestData.USER_NAME)
    driver.find_element(*RegisterPageLocators.FIELD_EMAIL).send_keys(generate_unique_email())
    driver.find_element(*RegisterPageLocators.FIELD_PASSWORD).send_keys(TestData.LOGIN_PASSWORD)
    driver.find_element(*RegisterPageLocators.BUTTON_REGISTER).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.TITLE_TEXT))

    assert driver.current_url == Urls.login_page



def test_register_invalid_password_show_error(driver):
    driver.get(Urls.registration_page)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.FIELD_NAME))
    driver.find_element(*RegisterPageLocators.FIELD_NAME).send_keys(TestData.USER_NAME)
    driver.find_element(*RegisterPageLocators.FIELD_EMAIL).send_keys(generate_unique_email())
    driver.find_element(*RegisterPageLocators.FIELD_PASSWORD).send_keys("12345")
    driver.find_element(*RegisterPageLocators.BUTTON_REGISTER).click()
    error_element = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.ERROR_INCORRECT_PASSWORD))

    assert error_element.is_displayed()

    

def test_register_existing_user_show_error(driver):
    driver.get(Urls.registration_page)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.FIELD_NAME))
    test_email = generate_unique_email()
    driver.find_element(*RegisterPageLocators.FIELD_NAME).send_keys(TestData.USER_NAME)
    driver.find_element(*RegisterPageLocators.FIELD_EMAIL).send_keys(test_email)
    driver.find_element(*RegisterPageLocators.FIELD_PASSWORD).send_keys("12345678")
    driver.find_element(*RegisterPageLocators.BUTTON_REGISTER).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.TITLE_TEXT))

    driver.get(Urls.registration_page)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.FIELD_NAME))
    driver.find_element(*RegisterPageLocators.FIELD_NAME).send_keys("Ольга")
    driver.find_element(*RegisterPageLocators.FIELD_EMAIL).send_keys(test_email)
    driver.find_element(*RegisterPageLocators.FIELD_PASSWORD).send_keys(TestData.LOGIN_PASSWORD)
    driver.find_element(*RegisterPageLocators.BUTTON_REGISTER).click()
    error_element = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.ERROR_USER_EXISTING))
    

    assert error_element.is_displayed()








