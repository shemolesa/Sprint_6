import pytest
import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.transitions_page import TransitionsPage
from pages.order_page import OrderPage

@pytest.fixture() # инициация вебдрайвера
def driver():
#    options = Options()
#    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Firefox()
#    driver.set_window_size(1920, 1080)
    driver.get(data.URL_MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture() # создание объекта главной страницы и принятие куков
def main_page(driver):
    main_page = MainPage(driver)
    main_page.click_to_element(MainPageLocators.BUTTON_COOKIE)
    return main_page

@pytest.fixture() # создание объекта страницы переходов
def transitions_page(driver):
    transitions_page = TransitionsPage(driver)
    return transitions_page

@pytest.fixture() # создание объекта страницы заказа
def order_page(driver):
    order_page = OrderPage(driver)
    return order_page
