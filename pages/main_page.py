import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step("Принятие куков")
    def click_coockie(self):
       self.click_to_element(MainPageLocators.BUTTON_COOKIE)


    @allure.step("Нажатие на вопрос")
    def click_to_question(self, number):
        locator_question_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, number)  # форматируем локатор вопроса
        self.click_to_element(locator_question_formatted) # нажимаем на вопрос

    @allure.step("Получение текста ответа")
    def get_text_answer(self, number):
        locator_answer_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATORS, number) # форматируем локатор ответа
        return self.get_text_from_element(locator_answer_formatted)  # возвращаем полученный ответ

    @allure.step("ПОлучение ответа на вопрос")
    def getting_answer_to_question(self, number):
        self.scroll_to_element(MainPageLocators.LAST_QUESTION_LOCATOR) # пролистываем до последнего вопроса
        self.click_to_question(number)
        return self.get_text_answer(number) # возвращаем полученный ответ