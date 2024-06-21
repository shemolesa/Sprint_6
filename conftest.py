import pytest
import data
from selenium import webdriver
from pages.transitions_page import TransitionsPage
from pages.order_page import OrderPage
from pages.main_page import MainPage

@pytest.fixture() # инициация вебдрайвера
def driver():
    driver = webdriver.Firefox()
    driver.get(data.URL_MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture() # создание объекта главной страницы и принятие куков
def main_page(driver):
    main_page = MainPage(driver)
    main_page.click_coockie()
    return main_page

@pytest.fixture() # создание объекта страницы переходов
def transitions_page(driver):
    transitions_page = TransitionsPage(driver)
    return transitions_page

@pytest.fixture() # создание объекта страницы заказа
def order_page(driver):
    order_page = OrderPage(driver)
    return order_page
