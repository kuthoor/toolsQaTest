from selenium import webdriver
'''
Browser class
'''
class Browser(object):
    #Change path to point to the chrome driver in your local system
    driver = webdriver.Chrome('<path>/chromedriver.exe')
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(context):
        context.driver.quit()
