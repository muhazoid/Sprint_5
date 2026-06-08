from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, Urls, LoginPage, ProfilePageLocators
from data import TestData



def test_profile_click_profile_button_valid_credentials_success(driver):
    driver.get(Urls.main_page)
    driver.find_element(*MainPageLocators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.TITLE_TEXT))
    driver.find_element(*LoginPage.FIELD_EMAIL).send_keys(TestData.LOGIN_EMAIL)
    driver.find_element(*LoginPage.FIELD_PASSWORD).send_keys(TestData.LOGIN_PASSWORD)
    driver.find_element(*LoginPage.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.BUTTON_ORDER))
    driver.find_element(*MainPageLocators.TEXT_PROFILE).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ProfilePageLocators.PROFILE_LINK))

    assert driver.current_url == Urls.profile_page


def test_profile_constructor_button_from_profile_valid_credentials_success(driver):
    driver.get(Urls.main_page)
    driver.find_element(*MainPageLocators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.TITLE_TEXT))
    driver.find_element(*LoginPage.FIELD_EMAIL).send_keys(TestData.LOGIN_EMAIL)
    driver.find_element(*LoginPage.FIELD_PASSWORD).send_keys(TestData.LOGIN_PASSWORD)
    driver.find_element(*LoginPage.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.BUTTON_ORDER))
    driver.find_element(*MainPageLocators.TEXT_PROFILE).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ProfilePageLocators.PROFILE_LINK))
    driver.find_element(*MainPageLocators.TEXT_CONSTRUCTOR).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.BUTTON_ORDER))

    assert driver.current_url == Urls.main_page


def test_profile_logo_click_from_profile_valid_credentials_success(driver):
    driver.get(Urls.main_page)
    driver.find_element(*MainPageLocators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.TITLE_TEXT))
    driver.find_element(*LoginPage.FIELD_EMAIL).send_keys(TestData.LOGIN_EMAIL)
    driver.find_element(*LoginPage.FIELD_PASSWORD).send_keys(TestData.LOGIN_PASSWORD)
    driver.find_element(*LoginPage.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.BUTTON_ORDER))
    driver.find_element(*MainPageLocators.TEXT_PROFILE).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ProfilePageLocators.PROFILE_LINK))
    driver.find_element(*MainPageLocators.LOGO).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.BUTTON_ORDER))

    assert driver.current_url == Urls.main_page


def test_profile_logout_button_valid_credentials_success(driver):
    driver.get(Urls.main_page)
    driver.find_element(*MainPageLocators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.TITLE_TEXT))
    driver.find_element(*LoginPage.FIELD_EMAIL).send_keys(TestData.LOGIN_EMAIL)
    driver.find_element(*LoginPage.FIELD_PASSWORD).send_keys(TestData.LOGIN_PASSWORD)
    driver.find_element(*LoginPage.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.BUTTON_ORDER))
    driver.find_element(*MainPageLocators.TEXT_PROFILE).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ProfilePageLocators.PROFILE_LINK))
    driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.TITLE_TEXT))

    assert driver.current_url == Urls.login_page