from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, Urls, LoginPage, RegisterPageLocators, RecoverPageLocators
from data import TestData


def test_login_main_button_valid_credentials_success(driver):
    driver.get(Urls.main_page)
    driver.find_element(*MainPageLocators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(LoginPage.TITLE_TEXT))
    driver.find_element(*LoginPage.FIELD_EMAIL).send_keys(TestData.LOGIN_EMAIL)
    driver.find_element(*LoginPage.FIELD_PASSWORD).send_keys(TestData.LOGIN_PASSWORD)
    driver.find_element(*LoginPage.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until_not(expected_conditions.presence_of_element_located(LoginPage.BUTTON_LOGIN))
    
    assert driver.current_url == Urls.main_page


def test_login_personal_account_button_valid_credentials_success(driver):
    driver.get(Urls.main_page)
    driver.find_element(*MainPageLocators.TEXT_PROFILE).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(LoginPage.TITLE_TEXT))
    driver.find_element(*LoginPage.FIELD_EMAIL).send_keys(TestData.LOGIN_EMAIL)
    driver.find_element(*LoginPage.FIELD_PASSWORD).send_keys(TestData.LOGIN_PASSWORD)
    driver.find_element(*LoginPage.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until_not(expected_conditions.presence_of_element_located(LoginPage.BUTTON_LOGIN))
    
    assert driver.current_url == Urls.main_page


def test_login_registration_page_link_valid_credentials_success(driver):
    driver.get(Urls.registration_page)
    driver.find_element(*RegisterPageLocators.TEXT_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(LoginPage.TITLE_TEXT))
    driver.find_element(*LoginPage.FIELD_EMAIL).send_keys(TestData.LOGIN_EMAIL)
    driver.find_element(*LoginPage.FIELD_PASSWORD).send_keys(TestData.LOGIN_PASSWORD)
    driver.find_element(*LoginPage.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until_not(expected_conditions.presence_of_element_located(LoginPage.BUTTON_LOGIN))
    
    assert driver.current_url == Urls.main_page


def test_login_forgot_password_page_link_valid_credentials_success(driver):
    driver.get(Urls.forgot_password_page)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RecoverPageLocators.LOGIN_LINK))
    driver.find_element(*RecoverPageLocators.LOGIN_LINK).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.TITLE_TEXT))
    driver.find_element(*LoginPage.FIELD_EMAIL).send_keys(TestData.LOGIN_EMAIL)
    driver.find_element(*LoginPage.FIELD_PASSWORD).send_keys(TestData.LOGIN_PASSWORD)
    driver.find_element(*LoginPage.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until_not(expected_conditions.presence_of_element_located(LoginPage.BUTTON_LOGIN))
    
    assert driver.current_url == Urls.main_page


    





