from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from locators.transitions_page_locator import TransitionsPageLocators
import allure

class TransitionsPage(BasePage):

    @allure.step("Переход на сайт Дзен")
    def transition_to_zen(self):
        self.switch_to_another_tab(TransitionsPageLocators.YANDEX_LOCATOR) # кликаем на надпись "Яндекс"
        return self.find_element_with_wait(TransitionsPageLocators.ZEN_THEMES).text # ищем надпись на сайте Дзен и возвращаем текст надписи

    @allure.step("Переход на страницу заказа по кнопке в шапке")
    def go_to_order_page(self):
        self.click_to_element(MainPageLocators.BUTTON_ORDER_HEADER) # ищем кнопку и нажимаем
        return self.find_element_with_wait(OrderPageLocators.ORDER_HEADER).text # ищем надпись на странице заказа и возвращаем текст

    @allure.step("Переход на страницу заказа по кнопке внизу страницы")
    def go_to_order_page_with_scroll(self):
        self.scroll_to_element(MainPageLocators.BUTTON_ORDER_BELOW)  # прокручиваем до кнопки и нажимаем
        self.click_to_element(MainPageLocators.BUTTON_ORDER_BELOW) # ищем кнопку и нажимаем
        return self.find_element_with_wait(OrderPageLocators.ORDER_HEADER).text # ищем надпись на странице заказа и возвращаем текст

    @allure.step("Переход на главную страницу со страницы заказа")
    def transition_to_main(self):
        self.click_to_element(MainPageLocators.BUTTON_ORDER_HEADER) # Нажимаем кнопку "Заказать"
        self.click_to_element(TransitionsPageLocators.SCOOTER_LOCATOR) # Нажимаем на надпись "Самокат"
        return self.find_element_with_wait(MainPageLocators.SCOOTER_IMG) # ищем рисунок самоката на странице


