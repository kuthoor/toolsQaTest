"""
This module has all the relevant functions for the contact form.
It also implements functions to interact with the various fields.
"""
from nose.tools import assert_equal
from selenium.webdriver.common.by import By
from browser import Browser
from home_page import HomePageLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactUsLocator(object):
    """
    Class to store various locator and static string
    """

    TITLE = (By.XPATH, '/html/head/title')
    NAME = (By.NAME, "your-name")
    EMAIL = (By.NAME, "your-email")
    MOBILE = (By.NAME, "your-mobile")
    CITY = (By.NAME, "your-city")
    COUNTRY = (By.NAME, "your-country")
    COMPANY = (By.NAME, "your-company")
    MESSAGE = (By.NAME, "your-message")

    SUCCESS_ERROR = (By.XPATH, '//*[@id="wpcf7-f24985-p13-o1"]/form/div[2]')
    VALIDATION_ERROR_MESSAGE = 'Validation errors occurred. Please confirm the fields and submit it again.'
    SUBMIT_SUCCESS_MESSAGE = 'Your message was sent successfully. Thanks.'

    VALIDATION_NAME_ERROR = (By.XPATH, '//*[@id="wpcf7-f24985-p13-o1"]/form/p[1]/span/span')
    VALIDATION_EMAIL_ERROR = (By.XPATH, '//*[@id="wpcf7-f24985-p13-o1"]/form/p[2]/span/span')
    VALIDATION_PHONE_ERROR = (By.XPATH, '//*[@id="wpcf7-f24985-p13-o1"]/form/p[3]/span/span')
    VALIDATION_CITY_ERROR = (By.XPATH, '//*[@id="wpcf7-f24985-p13-o1"]/form/p[4]/span/span')
    VALIDATION_COUNTRY_ERROR = (By.XPATH, '//*[@id="wpcf7-f24985-p13-o1"]/form/p[5]/span/span')
    VALIDATION_COMPANY_ERROR = (By.XPATH, '//*[@id="wpcf7-f24985-p13-o1"]/form/p[6]/span/span')
    VALIDATION_MESSAGE_ERROR = (By.XPATH, '//*[@id="wpcf7-f24985-p13-o1"]/form/p[7]/span/span')

    VALIDATION_GENERIC_MESSAGE = 'Please fill the required field.'
    VALIDATION_EMAIL_ERROR_MESSAGE = 'Email address seems invalid.'


class ContactUs(Browser):
    """
    Class that implements test steps in contact form.
    It implements function to interact with various fields.
    """
    def click_element(self, *locator):
        """
        Clicks an element defined by locator
        :param locator:
        :return: None
        """
        self.driver.find_element(*locator).click()

    def get_message(self, *locator):
        """
        Returns text for an element
        :param locator:
        :return: string
        """
        return self.driver.find_element(*locator).text

    def get_entered_text(self, *locator):
        """
        Returns text for text box
        :param locator:
        :return: string
        """
        return self.driver.find_element(*locator).get_attribute('value')

    def get_page_title(self):
        """
        Returns page title
        :return: string
        """
        return self.driver.title

    def fill(self, text, *locator):
        """
        Fills an element defined by locator with the text provided
        :param text:
        :param locator:
        :return: None
        """
        self.driver.find_element(*locator).send_keys(text)

    def fill_name(self, name):
        """
        Fills name field and checks if the text field has the same text
        :param name:
        :return: None
        """
        self.fill(name, *ContactUsLocator.NAME)
        assert_equal(self.get_entered_text(*ContactUsLocator.NAME), name)

    def fill_email(self, email):
        """
        Fills email field and checks if the text field has the same text
        :param email:
        :return: None
        """
        self.fill(email, *ContactUsLocator.EMAIL)
        assert_equal(self.get_entered_text(*ContactUsLocator.EMAIL), email)

    def fill_mobile(self, mobile):
        """
        Fills mobile field and checks if the text field has the same text
        :param mobile:
        :return: None
        """
        self.fill(mobile, *ContactUsLocator.MOBILE)
        assert_equal(self.get_entered_text(*ContactUsLocator.MOBILE), mobile)

    def fill_city(self, city):
        """
        Fills city field and checks if the text field has the same text
        :param city:
        :return: None
        """
        self.fill(city, *ContactUsLocator.CITY)
        assert_equal(self.get_entered_text(*ContactUsLocator.CITY), city)

    def fill_country(self, country):
        """
        Fills country field and checks if the text field has the same text
        :param country:
        :return: None
        """
        self.fill(country, *ContactUsLocator.COUNTRY)
        assert_equal(self.get_entered_text(*ContactUsLocator.COUNTRY), country)

    def fill_company(self, company):
        """
        Fills company field and checks if the text field has the same text
        :param company:
        :return: None
        """
        self.fill(company, *ContactUsLocator.COMPANY)
        assert_equal(self.get_entered_text(*ContactUsLocator.COMPANY), company)

    def fill_message(self, message):
        """
        Fills message field and checks if the text field has the same text
        :param message:
        :return: None
        """
        self.fill(message, *ContactUsLocator.MESSAGE)
        assert_equal(self.get_entered_text(*ContactUsLocator.MESSAGE), message)

    def submit(self):
        """
        Submits the form
        :return: None
        """
        self.click_element(*HomePageLocator.SEND_BUTTON)

    def error_on_submit(self, error_message, *locator):
        """
        Compares the actual error message displayed in element with the expected message
        :param error_message:
        :param locator:
        :return: None
        """
        e = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(locator, error_message))
        assert_equal(self.get_message(*locator), error_message)
