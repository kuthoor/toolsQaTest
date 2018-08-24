"""
This module has all the functions related to the home page and navigation to contact form
"""
from nose.tools import assert_equal
from selenium.webdriver.common.by import By
from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePageLocator(object):
    """
    Class to define locators and static text
    """

    TITLE = (By.XPATH, 'html/head/title')
    HOME_PAGE_TITLE = 'QA Automation Tools Tutorial'
    ABOUT = (By.LINK_TEXT, 'ABOUT')
    CONTACT_US = (By.LINK_TEXT, 'Contact Us')
    CONTACT_TITLE = 'Contact US ToolsQA | Lakshay Sharma'
    SEND_BUTTON = (By.XPATH, '//*[@id="wpcf7-f24985-p13-o1"]/form/p[8]/input')

class HomePage(Browser):
    """
    Class for homepage, it has function to navigate to contact form
    """

    def click_element(self, *locator):
        """
        Clicks an element defined by locator
        :param locator:
        :return: None
        """
        self.driver.find_element(*locator).click()

    def navigate(self, address):
        """
        Navigates to a given web address
        :param address:
        :return: None
        """
        self.driver.get(address)
        assert_equal(self.get_page_title(), HomePageLocator.HOME_PAGE_TITLE)

    def get_page_title(self):
        """
        Returns page title
        :return: string
        """
        return self.driver.title

    def go_to_contact(self):
        """
        Navigates to the contact us page
        :return: None
        """
        self.click_element(*HomePageLocator.ABOUT)
        self.click_element(*HomePageLocator.CONTACT_US)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(HomePageLocator.SEND_BUTTON))
        assert_equal(self.get_page_title(), HomePageLocator.CONTACT_TITLE)
