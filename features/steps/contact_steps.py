"""
This module implements test steps that are used in the contact.feature file.
"""
from selenium.webdriver.common.by import By
from ..pages.contact_us import ContactUsLocator

@step('I am on the toolsqa Site')
def step_impl(context):
    context.home_page.navigate("http://toolsqa.com/")
    #assert_equal (context.home_page.get_page_title(), "QA Automation Tools Tutorial")

@step('I search for "{search_term}"')
def step_impl(context, search_term):
    context.browser.find_element(By.ID, "search").send_keys(search_term)
    context.browser.find_element(By.CLASS_NAME, "search-form__button").click()

@step('I should be able to contact toolsqa with the following information')
def step_impl(context):
    context.home_page.go_to_contact()

@step('I should be able to enter name "{name}"')
def step_impl(context, name):
    context.contact_page.fill_name(name)

@step('I should be able to enter email "{email}"')
def step_impl(context, email):
    context.contact_page.fill_email(email)

@step('I should be able to enter message "{message}"')
def step_impl(context, message):
    context.contact_page.fill_message(message)

@step('I should be able to enter mobile "{mobile}"')
def step_impl(context, mobile):
    context.contact_page.fill_mobile(mobile)

@step('I should be able to enter city "{city}"')
def step_impl(context, city):
    context.contact_page.fill_city(city)

@step('I should be able to enter country "{country}"')
def step_impl(context, country):
    context.contact_page.fill_country(country)

@step('I should be able to enter company "{company}"')
def step_impl(context, company):
    context.contact_page.fill_company(company)

@step('I should not be able to submit')
def step_impl(context):
    context.contact_page.submit()
    #Check if we see validation errors per field
    context.contact_page.error_on_submit(ContactUsLocator.VALIDATION_GENERIC_MESSAGE,
                                         *ContactUsLocator.VALIDATION_PHONE_ERROR)
    context.contact_page.error_on_submit(ContactUsLocator.VALIDATION_GENERIC_MESSAGE,
                                         *ContactUsLocator.VALIDATION_CITY_ERROR)
    context.contact_page.error_on_submit(ContactUsLocator.VALIDATION_GENERIC_MESSAGE,
                                         *ContactUsLocator.VALIDATION_COUNTRY_ERROR)
    context.contact_page.error_on_submit(ContactUsLocator.VALIDATION_GENERIC_MESSAGE,
                                         *ContactUsLocator.VALIDATION_COMPANY_ERROR)
    #Check if the page has overall validation error
    context.contact_page.error_on_submit(ContactUsLocator.VALIDATION_ERROR_MESSAGE,
                                         *ContactUsLocator.SUCCESS_ERROR)

@step('Email validation should fail')
def step_impl(context):
    context.contact_page.submit()
    # Check if we see validation errors per field
    context.contact_page.error_on_submit(ContactUsLocator.VALIDATION_GENERIC_MESSAGE,
                                         *ContactUsLocator.VALIDATION_PHONE_ERROR)
    context.contact_page.error_on_submit(ContactUsLocator.VALIDATION_GENERIC_MESSAGE,
                                         *ContactUsLocator.VALIDATION_CITY_ERROR)
    context.contact_page.error_on_submit(ContactUsLocator.VALIDATION_GENERIC_MESSAGE,
                                         *ContactUsLocator.VALIDATION_COUNTRY_ERROR)
    context.contact_page.error_on_submit(ContactUsLocator.VALIDATION_GENERIC_MESSAGE,
                                         *ContactUsLocator.VALIDATION_COMPANY_ERROR)
    # Check if email vaildation error is shown
    context.contact_page.error_on_submit(ContactUsLocator.VALIDATION_EMAIL_ERROR_MESSAGE,
                                         *ContactUsLocator.VALIDATION_EMAIL_ERROR)
    # Check if the page has overall validation error
    context.contact_page.error_on_submit(ContactUsLocator.VALIDATION_ERROR_MESSAGE,
                                         *ContactUsLocator.SUCCESS_ERROR)

@step('Phone validation should fail')
def step_impl(context):
    context.contact_page.submit()
    # Check if we see validation errors per field
    context.contact_page.error_on_submit(ContactUsLocator.VALIDATION_GENERIC_MESSAGE,
                                         *ContactUsLocator.VALIDATION_PHONE_ERROR)
    context.contact_page.error_on_submit(ContactUsLocator.VALIDATION_GENERIC_MESSAGE,
                                         *ContactUsLocator.VALIDATION_CITY_ERROR)
    context.contact_page.error_on_submit(ContactUsLocator.VALIDATION_GENERIC_MESSAGE,
                                         *ContactUsLocator.VALIDATION_COUNTRY_ERROR)
    context.contact_page.error_on_submit(ContactUsLocator.VALIDATION_GENERIC_MESSAGE,
                                         *ContactUsLocator.VALIDATION_COMPANY_ERROR)
    # Check if the page has overall validation error
    context.contact_page.error_on_submit(ContactUsLocator.VALIDATION_ERROR_MESSAGE,
                                         *ContactUsLocator.SUCCESS_ERROR)


@step('I should be able to submit without error')
def step_impl(context):
    context.contact_page.submit()
    # Check if the page has success message
    context.contact_page.error_on_submit(ContactUsLocator.SUBMIT_SUCCESS_MESSAGE,
                                         *ContactUsLocator.SUCCESS_ERROR)