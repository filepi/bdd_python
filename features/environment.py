from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_all(context):
    # chrome_options = Options()
    # chrome_options.add_experimental_option("detach", True)
    context.driver = webdriver.Chrome("features/chromedriver")
    context.driver.delete_all_cookies()
    context.driver.maximize_window()
