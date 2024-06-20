# Sprint_6

## conftest.py 
фикстуры
_driver_ - инициация вебдрайвера
_main_page_ - создание объекта главной страницы и принятие куков
_transitions_page_ - создание объекта страницы переходов
_order_page_ - создание объекта страницы заказа

## data.py
тестовые данные

## helpers.py
вспомогательные функции
_generated_phone_ - генерация номера телефона
_generated_str_ - генерация строки (имени/фамилии/адреса)
_generated_metro_ - генерация номера станции метро
_generated_date_ - генерация числа даты
_generated_occupancy_ - генерация срока аренды

## base_page.my
базовые методы
_find_element_with_wait_ - поиск элемента с ожиданием
_click_to_element_ - поиск элемента с нажатием на него
_add_text_to_element_ - поиск элемента ввода и ввод текста
_get_text_from_element_ - получение текста элемента
_format_locator_ - форматирование локатора из списка
_scroll_to_element_ - скролл до элемента

## main_page.py
методы главной страницы
_click_coockie_ - Принятие куков
_click_to_question_ - форматирование локатора вопроса и нажатие на вопрос
_get_text_answer_ - форматирование локатора ответа и получение текста ответа
_getting_answer_to_question_ - получение ответа на вопрос


## main_page_locators.py
локаторы для главной страницы

## test_main_page.py
/n тесты главной страницы
_test_answer_to_question_ - проверка соответствия ответа выбранному вопросу


## order_page.py
методы страницы заказа
_go_to_order_page_ - переход к странице заказа
_choice_element_ - Выбор станции метро/даты/срока аренды
_set_order_ - Оформление заказа

## order_page_locators.py
локаторы для страницы заказы

## test_order_page.py
/n тесты страницы заказа
_test_create_order_ - проверка успешного оформления заказа

## transitions_page.py
методы переходов
_go_to_order_page_ - Переход на страницу заказа по кнопке в шапке
_go_to_order_page_with_scroll_ - Переход на страницу заказа по кнопке внизу страницы
_switch_to_another_tab_ - Переключение на другую вкладку браузера

## transitions_page_locators.py
локаторы переходов

## test_transitions_page.py
/n тесты переходов
_test_click_on_the_button_below_ - роверка перехода к форме заказа по кнопке внизу
_test_click_on_the_button_header_ - проверка перехода к форме заказа по кнопке в шапке
_test_transition_to_main_ - проверка перехода на главную страницу со страницы заказа
_test_transition_to_zen_ - проверка перехода на сайт Дзен
