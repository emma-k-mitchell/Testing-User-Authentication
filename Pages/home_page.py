from Pages.base_page import BasePage
from Resources.locators import HomePageSelectors
'''
The homepage can be accessed at https://the-internet.herokuapp.com/. We navigate to this page at the start of each test.
'''
class HomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    # class methods CHANGE TO SELECT FORM AUTHENTICATION LINK
    def select_form_authentication_link(self):
        self.click(HomePageSelectors.form_auth_link)
       
