from selenium import webdriver
from browser import Browser
from pages.home_page import HomePage
from pages.contact_us import ContactUs

def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.contact_page = ContactUs()

def after_all(context):
    context.browser.close()
