
from selenium.webdriver.common.by import By

class OrderPageLocators:
    ORDER_HEADER = By.XPATH, './/div[contains(@class, "Order_Header")]' # надпись "Для кого самокат" в форме заказа
    FIELD_NAME = By.XPATH, './/input[@placeholder="* Имя"]' # поле ввода Имя
    FIELD_SURNAME = By.XPATH, './/input[@placeholder="* Фамилия"]'  # поле ввода Фамилия
    FIELD_ADDRESS = By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]'  # поле ввода Адрес: куда привезти заказ
    FIELD_METRO = By.XPATH, './/input[@placeholder="* Станция метро"]'  # поле ввода Станция метро
    FIELD_PHONE = By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]'  # поле ввода Телефон: на него позвонит курьер
    BUTTON_METROS = By.XPATH, '.// button[contains( @class , "select-search__option") and @ value="4"]'#
    BUTTON_METRO = By.XPATH, '.// button[contains( @class , "select-search__option") and @ value="{}"]'#
    BUTTON_ONWARD = By.XPATH, '.// button[contains( @class ,"Button_Middle")]' # Кнопка Далее
    BUTTON_DATE = By.XPATH, '.// div[contains( @class , "react-datepicker__day--{}")]' # кнопка дата
    FIELD_DATE = By.XPATH, './/input[@placeholder="* Когда привезти самокат"]' # поле дата
    FIELD_OCCUPANCY = By.XPATH, '.// div[ @class ="Dropdown-placeholder"]'  # поле ввода Срок аренды
    BUTTON_OCCUPANCY = By.XPATH, '.// div[ @class ="Dropdown-option" and text()="{}"]'  # кнопка Срок аренды
    CHECK_COLOR_BLACK = By.XPATH, '.// input[ @ id = "black"]'  # чек цвет самоката черный
    CHECK_COLOR_GREY = By.XPATH, '.// input[ @ id = "grey"]'  # чек цвет самоката серый
    FIELD_COMMENT = By.XPATH, '.// input[ @ placeholder = "Комментарий для курьера"]'  # поле ввода Комментарий
    BUTTON_ORDER = By.XPATH, '.// button[contains( @class , "Button_Middle") and text() ="Заказать"]' # последняя кнопка "заказать"
    BUTTON_EYS = By.XPATH, '.// div[contains( @class , "Order_Button")] / button[(contains( @class , "Button_Button")) and text()="Да"]'  # кнопка Да
    ORDER_IS_PROCESSED = By.XPATH, '.// div[contains( @class , "Order_ModalHeader")]'  # результат заказа