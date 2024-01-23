import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import sys
sys.path.append('../')
from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from Pages.signed_in_page import SignedInPage

from Resources.session import Sessions

def initialize_page_drivers(driver):
    global homepage
    global loginpage
    global signedinpage

    homepage = HomePage(driver)
    loginpage = LoginPage(driver)
    signedinpage = SignedInPage(driver)

class TestFormAuthentication:
    '''
    Author: Emma Mitchell
    Purpose: This testcase checks if a user can login using valid credentials.
    Browser: Firefox
    '''
    def test_login_valid_credentials(self):

        driver = Sessions.create_firefox_session()
        initialize_page_drivers(driver)

        driver.get("http://the-internet.herokuapp.com")

        homepage.select_form_authentication_link()

        loginpage.login("tomsmith", "SuperSecretPassword!")

        assert 'logged into' in signedinpage.find_flash_msg()

        driver.quit()
    '''
    Author: Emma Mitchell
    Purpose: This testcase ensures that a user cannot login using an invalid username.
    Browser: Edge
    '''
    def test_login_invalid_username(self):

        driver = Sessions.create_edge_session()
        initialize_page_drivers(driver)

        driver.get("http://the-internet.herokuapp.com")

        homepage.select_form_authentication_link()

        loginpage.login("invalid_username", "SuperSecretPassword!")

        assert 'username is invalid!' in loginpage.find_flash_msg()

        driver.quit()
    
    '''
    Author: Emma Mitchell
    Purpose: This testcase ensures that a user cannot login using an invalid password.
    Browser: Firefox
    '''
    def test_login_invalid_password(self):

        driver = Sessions.create_firefox_session()
        initialize_page_drivers(driver)

        driver.get("http://the-internet.herokuapp.com")

        homepage.select_form_authentication_link()

        loginpage.login("tomsmith", "invalid_password")

        assert 'password is invalid!' in loginpage.find_flash_msg()

        driver.quit()

        