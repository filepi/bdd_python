from behave import given
from hamcrest import assert_that, equal_to
import requests
import json
from configuration import execute_frontend_test


URL = "https://petstore.swagger.io/v2/pet/"

@given('I make a GET Request using ID {id}')
def get_request(context, id):
    r = requests.get(URL + '3')
    assert_that(r.status_code, equal_to(200))


def post_request():
    r = requests.post('https://petstore.swagger.io/v2/pet/findByStatus?status=available')
    print(json.dumps(r.json(), indent=4, sort_keys=True))

