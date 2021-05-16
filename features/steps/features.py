from behave import given
from hamcrest import assert_that, equal_to
import requests
import json


MAIN_URL = "https://petstore.swagger.io/v2/"
STORE_INVENTORY = "store/inventory"


@given('I get the store inventory')
def get_request(context):
    r = requests.get(MAIN_URL + STORE_INVENTORY)
    parsed = json.loads(r.text)#convert do Dictonary so we can indent
    print(json.dumps(parsed, indent=4, sort_keys=True))
    assert_that(r.status_code, equal_to(200))