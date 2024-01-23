from selenium.webdriver.common.by import By
'''
A collection of locators/selectors for elements on the three pages relevant to this test.
'''
class LoginPageSelectors():
    username_field = (By.CSS_SELECTOR, '#username')
    password_field = (By.CSS_SELECTOR, '#password')

    submit_button = (By.CSS_SELECTOR, 'button[type=submit]')

    login_page_flash_msg = (By.CSS_SELECTOR, '#flash')

class HomePageSelectors():
    form_auth_link = (By.LINK_TEXT, 'Form Authentication')

class SignedInPageSelectors():
    logout_button = (By.LINK_TEXT, 'Logout')
    signed_in_flash_msg = (By.CSS_SELECTOR, '#flash')