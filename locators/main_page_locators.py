from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, './/*[@id="accordion__heading-{}"]' # вопрос
    ANSWER_LOCATORS = By.XPATH, './/*[@id="accordion__panel-{}"]' # ответ
    LAST_QUESTION_LOCATOR = By.XPATH, './/*[@id="accordion__heading-7"]' #  последний вопрос
    BUTTON_COOKIE = By.XPATH, './/*[@id="rcc-confirm-button"]' # кнопка принятия куков
    BUTTON_ORDER_HEADER = By.XPATH, './/div [contains(@class,"Header_Nav")]/button[(contains(@class, "Button_Button")) and text()="Заказать"]' # кнопка "заказать" в шапке
    BUTTON_ORDER_BELOW = By.XPATH, './/button[(contains(@class, "Button_Middle")) and text() ="Заказать"]' # нижняя кнопка "Заказать"
    SCOOTER_IMG = By.XPATH, '.// img[ @ alt = "Scooter blueprint"]' # изображение самоката
