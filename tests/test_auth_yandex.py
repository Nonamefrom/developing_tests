import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://passport.yandex.ru/auth/'
login = 'Введите логин'
password = 'Введите пароль'

class BasePage:

    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
        return self

    def element_is_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def fill_text(self, locator, txt, timeout=10):
        element = wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        element.click()
        element.clear()
        element.send_keys(txt)

    def click(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()


class ElementsOnPages(BasePage):

    LOGIN_FIELD = (By.XPATH, '//*[@id="passp-field-login"]')
    PASS_FIELD = (By.XPATH, '//*[@id="passp-field-passwd"]')
    ACCEPT_BUTTON = (By.XPATH, '//*[@id="passp:sign-in"]')
    LOGIN_FORM_TEXT = (By.XPATH, '//*[@class="passp-add-account-page-title"]')
    USER_CARD = (By.XPATH, '//*[@data-testid="profile-card"]')


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_yandex_login(driver):
    page = ElementsOnPages(driver, URL)
    page.open()

    # Проверяем наличие текста формы логина
    assert page.element_is_visible(ElementsOnPages.LOGIN_FORM_TEXT), "Login form text not found"

    # Заполняем поле логина и нажимаем кнопку "Принять"
    page.fill_text(ElementsOnPages.LOGIN_FIELD, login)
    page.click(ElementsOnPages.ACCEPT_BUTTON)

    # Заполняем поле пароля и нажимаем кнопку "Принять"
    page.fill_text(ElementsOnPages.PASS_FIELD, password)
    page.click(ElementsOnPages.ACCEPT_BUTTON)
    assert page.element_is_visible(
        ElementsOnPages.USER_CARD), "Карточка пользователя не найдена, возможно пользователь не авторизован"


"""
ДЗ не доделано, Яндекс требует ввода СМС из пуша на устройство - возможно аккаунты без 2FA пройдут прямо, 
как импортировать сюда код из устройства - не разобрался.    
с почтой было бы проще - так же урлом открывать почту, искать письмо от яндекса, проваливаться
из него забирать с помощью регулярки пароль и подставлять в последнюю форму авторизации"""
