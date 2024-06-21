import allure

class TestTransitionsPage:

    @allure.title('проверка перехода к форме заказа по кнопке "Заказать" внизу')
    @allure.description('Прокручиваем до кнопки "Заказать" внизу страницы, нажимаем и проверяем, что на странице отображается надпись "Для кого свамокат"')
    def test_click_on_the_button_below(self, main_page, transitions_page):
        assert transitions_page.go_to_order_page_with_scroll() == "Для кого самокат" # проверяем наличие надписи "Для кого самока" на странице заказа

    @allure.title('проверка перехода к форме заказа по кнопке "Заказать" в шапке')
    @allure.description('Нажимаем кнопку "Заказать" в шапке и проверяем, что на странице отображается надпись "Для кого свамокат"')
    def test_click_on_the_button_header(self, main_page, transitions_page):
        assert transitions_page.go_to_order_page() == "Для кого самокат" # проверяем наличие надписи "Для кого самока" на странице заказа


    @allure.title('проверка перехода на главную страницу со страницы заказа')
    @allure.description('Переходим на страницу заказа и нажимае надпиь "Самокат". Проверяем что на странице отобразилась картинка самоката')
    def test_transition_to_main(self, main_page, transitions_page):
        assert transitions_page.transition_to_main() # проверяем наличие рисунка самоката на странице

    @allure.title('проверка перехода на сайт Дзен')
    @allure.description('Нажимаем на надпись Яндекс, переходим на таб с сайтом Дзен и проверяем наличие надписи "Темы в Дзене"')
    def test_transition_to_zen(self, main_page, transitions_page):
        assert transitions_page.transition_to_zen() == 'Темы в Дзене' # проверяем наличие надписи "Темы в Дзене" на странице


