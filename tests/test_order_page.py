import pytest
import allure
from data import ORDER_INFO_DICT
from locators.order_page_locators import OrderPageLocators


class TestOrderPage:

    @pytest.mark.parametrize('locator_color', [OrderPageLocators.CHECK_COLOR_BLACK, OrderPageLocators.CHECK_COLOR_GREY])
    @allure.description('Переходим на страницу заказа, заполняем данные и проверяем, что элемент страницы с результатом заказа содержит надпись "Заказ оформлен". ПРоверка выполняется для двух цветов самоката ')
    @allure.title('проверка успешного оформления заказа')
    def test_create_order(self, main_page, order_page, locator_color):
        result = order_page.set_order(locator_color, ORDER_INFO_DICT) # заполняем параметры заказа и получаем элемент текущей страницы
        assert "Заказ оформлен" in result # проверяем наличие надписи "Заказ оформлен" в тексе элемента
