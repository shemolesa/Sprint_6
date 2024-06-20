from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from helpers import generated_occupancy, generated_metro, generated_date
import allure

class OrderPage(BasePage):

    @allure.step("Выбор станции метро/даты/срока аренды")
    def choice_element(self, field_locator, button_locator, generated_method):
        self.click_to_element(field_locator)
        format_locator = self.format_locators(button_locator, generated_method())
        self.click_to_element(format_locator)

    @allure.step("Оформление заказа")
    def set_order(self, check_color_locator, order_info_dict):
        self.add_text_to_element(OrderPageLocators.FIELD_NAME, order_info_dict['name'])
        self.add_text_to_element(OrderPageLocators.FIELD_SURNAME, order_info_dict['surname'])
        self.add_text_to_element(OrderPageLocators.FIELD_ADDRESS, order_info_dict['address'])
        self.choice_element(OrderPageLocators.FIELD_METRO, OrderPageLocators.BUTTON_METRO, generated_metro)
        self.add_text_to_element(OrderPageLocators.FIELD_PHONE, order_info_dict['phone'])
        self.click_to_element(OrderPageLocators.BUTTON_ONWARD)
        self.choice_element(OrderPageLocators.FIELD_DATE, OrderPageLocators.BUTTON_DATE, generated_date)
        self.choice_element(OrderPageLocators.FIELD_OCCUPANCY, OrderPageLocators.BUTTON_OCCUPANCY, generated_occupancy)
        self.click_to_element(check_color_locator)
        self.add_text_to_element(OrderPageLocators.FIELD_COMMENT, order_info_dict['comment'])
        self.click_to_element(OrderPageLocators.BUTTON_ORDER)
        self.click_to_element(OrderPageLocators.BUTTON_EYS)
        return self.get_text_from_element(OrderPageLocators.ORDER_IS_PROCESSED)

