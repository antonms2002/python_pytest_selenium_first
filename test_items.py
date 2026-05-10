from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestItems:

    _ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')


    def test_button_add_to_cart_exists(self, browser, wait):
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')

        button = wait.until(EC.visibility_of_element_located(self._ADD_TO_CART_BUTTON))

        assert button.is_displayed()