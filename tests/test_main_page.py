import pytest
import allure
from data import AnswerText

class TestMainPage:

    @pytest.mark.parametrize (
        'question_number, answer',
        [
                (0, AnswerText.ANSWER_TEXT_PRICE),
                (1, AnswerText.ANSWER_TEXT_AMOUNT),
                (2, AnswerText.ANSWER_TEXT_OCCUPANCY),
                (3, AnswerText.ANSWER_TEXT_TODAY),
                (4, AnswerText.ANSWER_TEXT_EXTENSION),
                (5, AnswerText.ANSWER_TEXT_CHARGER),
                (6, AnswerText.ANSWER_TEXT_CANCELLATION),
                (7, AnswerText.ANSWER_TEXT_DELIVERY)
        ]
    )
    @allure.description("Открываем поочередно каждый вопрос и проверяем, что текст ответа соответствует эталону")
    @allure.title('проверка соответствия ответа выбранному вопросу')
    def test_answer_to_question(self, main_page, question_number, answer):
        assert main_page.getting_answer_to_question(question_number) == answer

