from selenium.webdriver.common.by import By

class TransitionsPageLocators:
    YANDEX_LOCATOR = By.XPATH, './/*[contains(@class, "Header_LogoYandex")]' # логотип яндекса
    SCOOTER_LOCATOR = By.XPATH, '.// *[contains( @class , "Header_LogoScooter")]' # логотип самоката
    ZEN_THEMES = By.XPATH, '.// div[contains( @class ,"trends-entry-desktop__title")]' # заголовок на странице дзена