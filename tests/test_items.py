import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestMultiLanguage:
    def test_present_of_button(self, browser, language):
        page = f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/'
        browser.get(page)
        browser.implicitly_wait(10)
        time.sleep(30)  # Чтобы убедиться в смене языка
        try:
            assert WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '.btn-add-to-basket')))
            # Для тех, кто в танке. Это bool, возвращающий True, если кнопка есть.
            # assert и так ожидает True, поэтому дополнительно прописывать '==' не требуется.
        except Exception as e:
            print('Нет кнопки "Добавить в корзину"')
            raise e
