from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random
from locators import MainPageLocators, Urls, LoginPage, RegisterPageLocators

from helpers import TestData


def test_login_in_login_btn_success(driver):
    driver.get(Urls.main_page)
        
    driver.find_element(*MainPageLocators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(LoginPage.TITLE_TEXT))
    driver.find_element(*LoginPage.FIELD_EMAIL).send_keys(TestData.LOGIN_EMAIL)
    driver.find_element(*LoginPage.FIELD_PASSWORD).send_keys(TestData.LOGIN_PASSWORD)
    driver.find_element(*LoginPage.BUTTON_LOGIN).click()

    WebDriverWait(driver, 5).until_not(expected_conditions.presence_of_element_located(LoginPage.BUTTON_LOGIN))
    
    assert driver.current_url == Urls.main_page


def test_login_via_personal_account_success(driver):
    driver.get(Urls.main_page)
    driver.find_element(*MainPageLocators.TEXT_PROFILE).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(LoginPage.TITLE_TEXT))
    driver.find_element(*LoginPage.FIELD_EMAIL).send_keys(TestData.LOGIN_EMAIL)
    driver.find_element(*LoginPage.FIELD_PASSWORD).send_keys(TestData.LOGIN_PASSWORD)
    driver.find_element(*LoginPage.BUTTON_LOGIN).click()

    WebDriverWait(driver, 5).until_not(expected_conditions.presence_of_element_located(LoginPage.BUTTON_LOGIN))
    
    assert driver.current_url == Urls.main_page


def test_login_via_registration_page_show_main_page(driver):
    driver.get(Urls.registration_page)
    driver.find_element(*RegisterPageLocators.TEXT_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(LoginPage.TITLE_TEXT))
    driver.find_element(*LoginPage.FIELD_EMAIL).send_keys(TestData.LOGIN_EMAIL)
    driver.find_element(*LoginPage.FIELD_PASSWORD).send_keys(TestData.LOGIN_PASSWORD)
    driver.find_element(*LoginPage.BUTTON_LOGIN).click()

    WebDriverWait(driver, 5).until_not(expected_conditions.presence_of_element_located(LoginPage.BUTTON_LOGIN))
    
    assert driver.current_url == Urls.main_page




