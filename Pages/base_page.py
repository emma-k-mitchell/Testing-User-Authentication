from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
''' 
The file base_page.py is used by the three other page files relevant to this test: home_page.py, login_page.py, and signed_in_page.py.
This class has a driver initialization method, and three basic methods to be used by the other pages: click, enter_text, and find.
'''
class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).click()
    
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).send_keys(text)
    
    def find(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))