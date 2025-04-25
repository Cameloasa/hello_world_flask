from behave import given, when, then
from app import app


@given('user is on the main page')
def step_impl(context):
    context.client = app.test_client()

@when('user makes GET on "/"')
def step_impl(context):
    context.response = context.client.get('/')

@then('user gets the message "Hello, World!"')
def step_impl(context):
    assert context.response.data.decode() == 'Hello, World!'
