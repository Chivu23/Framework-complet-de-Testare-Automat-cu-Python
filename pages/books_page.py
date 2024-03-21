from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BooksPage(BasePage):
    # selectors
    LOGIN_BUTTON = '//button[@id="login"]'

    # actions
    def click_login_button(self):
        self.driver.get('https://demoqa.com')

    def click_book_store_application(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()
