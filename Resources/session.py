from selenium import webdriver
'''
This file is used to create a new test session using one of the browsers below. These methods are called from the testing class.
'''
class Sessions():

    def create_firefox_session():
        driver = webdriver.Firefox()
        return driver
    
    def create_edge_session():
        driver = webdriver.Edge()
        return driver