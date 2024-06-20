from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

class TransitionsPage(BasePage):

    @allure.step('Переключение на другую вкладку браузера')
    def switch_to_another_tab(self, locator):
        self.click_to_element(locator)
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])

    @allure.step("Переход на страницу заказа по кнопке в шапке")
    def go_to_order_page(self, locator):
        self.click_to_element(locator)
        return self.find_element_with_wait(OrderPageLocators.ORDER_HEADER).text


    @allure.step("Переход на страницу заказа по кнопке внизу страницы")
    def go_to_order_page_with_scroll(self, locator):
        self.scroll_to_element(locator)
        self.click_to_element(locator)
        return self.find_element_with_wait(OrderPageLocators.ORDER_HEADER).text

