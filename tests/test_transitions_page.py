import allure
from locators.main_page_locators import MainPageLocators
from locators.transitions_page_locator import TransitionsPageLocators

class TestTransitionsPage:

    @allure.title('проверка перехода к форме заказа по кнопке внизу')
    @allure.description('Прокручиваем до кнопки "Заказать" внизу страницы, нажимаем и проверяем, что на странице отображается надпись "Для кого свамокат"')
    def test_click_on_the_button_below(self, main_page, transitions_page):
        main_page.scroll_to_element(MainPageLocators.BUTTON_ORDER_BELOW) # скроллим о кнопки "Заказать" внизу страницы
        assert transitions_page.go_to_order_page(MainPageLocators.BUTTON_ORDER_BELOW) == "Для кого самокат" # проверяем наличие надписи "Для кого самока" на странице заказа

    @allure.title('проверка перехода к форме заказа по кнопке в шапке')
    @allure.description('Нажимаем кнопку "Заказать" в шапке и проверяем, что на странице отображается надпись "Для кого свамокат"')
    def test_click_on_the_button_header(self, main_page, transitions_page):
        assert transitions_page.go_to_order_page(MainPageLocators.BUTTON_ORDER_HEADER) == "Для кого самокат" # проверяем наличие надписи "Для кого самока" на странице заказа


    @allure.title('проверка перехода на главную страницу со страницы заказа')
    @allure.description('Переходим на страницу заказа и нажимае надпиь "Самокат". Проверяем что на странице отобразилась картинка самоката')
    def test_transition_to_main(self, main_page, transitions_page):
        main_page.click_to_element(MainPageLocators.BUTTON_ORDER_HEADER) # Нажимаем кнопку "Заказать"
        transitions_page.click_to_element(TransitionsPageLocators.SCOOTER_LOCATOR) # Нажимаем на надпись "Самокат"
        assert main_page.find_element_with_wait(MainPageLocators.SCOOTER_IMG) # проверяем наличие рисунка самоката на странице

    @allure.title('проверка перехода на сайт Дзен')
    @allure.description('Нажимаем на надпись Яндекс, переходим на таб с сайтом Дзен и проверяем наличие надписи "Темы в Дзене"')
    def test_transition_to_zen(self, main_page, transitions_page):
        transitions_page.switch_to_another_tab(TransitionsPageLocators.YANDEX_LOCATOR) # кликаем на надпись "Яндекс"
        assert transitions_page.find_element_with_wait(TransitionsPageLocators.ZEN_THEMES) # проверяем наличие надписи "Темы в Дзене" на странице


