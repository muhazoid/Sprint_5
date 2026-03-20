from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators, Urls



def test_constructor_click_buns_tab_success(driver):
    driver.get(Urls.main_page)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.BUTTON_LOGIN))
    driver.find_element(*MainPageLocators.TAB_SAUCES).click()
    driver.find_element(*MainPageLocators.TAB_BUNS).click()
    active_tab = driver.find_element(*MainPageLocators.TAB_ACTIVE).text
    
    assert "Булки" in active_tab


def test_constructor_click_sauces_tab_success(driver):    
    driver.get(Urls.main_page)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.BUTTON_LOGIN))
    driver.find_element(*MainPageLocators.TAB_SAUCES).click()
    active_tab = driver.find_element(*MainPageLocators.TAB_ACTIVE).text
    
    assert "Соусы" in active_tab


def test_constructor_click_fillings_tab_success(driver):
    driver.get(Urls.main_page)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.BUTTON_LOGIN))
    driver.find_element(*MainPageLocators.TAB_FILLINGS).click()
    active_tab = driver.find_element(*MainPageLocators.TAB_ACTIVE).text
    
    assert "Начинки" in active_tab






