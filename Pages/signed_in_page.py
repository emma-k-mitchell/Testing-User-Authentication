from Pages.base_page import BasePage
from Resources.locators import SignedInPageSelectors
'''
The signed in page is accessable from the login page only after entering valid user credentials.
'''
class SignedInPage(BasePage):
     
    def __init__(self, driver):
        self.driver = driver
        
    #class methods
    def logout(self):
        self.click(SignedInPageSelectors.logout_button)

    def find_flash_msg(self):
        flash_msg = self.find(SignedInPageSelectors.signed_in_flash_msg).text
        return flash_msg