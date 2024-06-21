import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step(" поиск элемента с ожиданием")
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until((expected_conditions.visibility_of_element_located(locator)))
        return self.driver.find_element(*locator)

    @allure.step("поиск элемента с нажатием на него")
    def click_to_element(self, locator):
        self.find_element_with_wait(locator).click()

    @allure.step("поиск элемента ввода и ввод текста")
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("получение текста элемента")
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step("форматирование локатора из списка")
    def format_locators(self, locator_original, number):
        method, locator = locator_original # делим исходный локатора на метод и путь
        locator = locator.format(number) # подставляем в путь номер
        return (method, locator)

    @allure.step("скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Переключение на другую вкладку браузера')
    def switch_to_another_tab(self, locator):
        self.click_to_element(locator)
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])
