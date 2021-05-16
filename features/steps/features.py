from behave import given
from hamcrest import assert_that, equal_to
import requests
import json


MAIN_URL = "https://petstore.swagger.io/v2/"
STORE_INVENTORY = "store/inventory"


@when('I get the store inventory')
def get_request(context):
    r = requests.get(MAIN_URL + STORE_INVENTORY)
    parsed = json.loads(r.text) #convert do Dictonary so we can indent in the next line
    print(json.dumps(parsed, indent=4, sort_keys=True))
    context.status_code = r.status_code


@then('I verify that I receive "{status_code:d}" status code')
def verify_status_code(context, status_code):
    assert_that(context.status_code, equal_to(status_code))