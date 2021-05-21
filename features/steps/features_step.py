from behave import when, then
from hamcrest import assert_that, equal_to
from time import sleep
import requests
import json


from features.pages.HomePage import HomePage

MAIN_URL = "https://petstore.swagger.io/v2/"
STORE_INVENTORY = "store/inventory"


@when('I get the store inventory')
def get_request(context):
    r = requests.get(MAIN_URL + STORE_INVENTORY)
    # convert do Dictionary so we can indent in the next line
    parsed = json.loads(r.text)
    print(json.dumps(parsed, indent=4, sort_keys=True))
    context.status_code = r.status_code


@then('I verify that I receive "{status_code:d}" status code')
def verify_status_code(context, status_code):
    assert_that(context.status_code, equal_to(status_code))


@given('I am in HomePage')
def load_home_page(context):
    context.home_page = HomePage(context.driver)
    context.home_page.access_url("https://www.tumblr.com")


@when('I click in Login in the middle of page')
def click_minha_conta(context):
    context.home_page.click_login_button()
    sleep(10)
