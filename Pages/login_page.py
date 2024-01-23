from Pages.base_page import BasePage
from Resources.locators import LoginPageSelectors
'''
The login page can be accessed from the homepage by clicking on the form authentication link.
'''
class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    # class methods
    def enter_username(self, username):
        self.enter_text(LoginPageSelectors.username_field, username)
    
    def enter_password(self, password):
        self.enter_text(LoginPageSelectors.password_field, password)
    
    def click_button(self):
        self.click(LoginPageSelectors.submit_button)

    # uses the three methods above to create a simple login method, which is called from the testing class
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_button()

    def find_flash_msg(self):
        flash_msg = self.find(LoginPageSelectors.login_page_flash_msg).text
        return flash_msg