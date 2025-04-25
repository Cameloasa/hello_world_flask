from behave import given, when, then
from app import app
from datetime import datetime


@given('user is on the main page')
def step_given_user_on_main_page(context):
    context.client = app.test_client()

@when('user makes GET on "/"')
def step_when_user_makes_get_on_valid_route(context):
    context.response = context.client.get('/')

@then('user gets the message "Hello, World!"')
def step_then_user_get_ok_message(context):
    assert context.response.data.decode() == 'Hello, World!'

@given(u'user is on the application')
def step_given_user_on_application(context):
    context.client = app.test_client()

@when(u'user makes GET on "/invalid-route"')
def step_when_user_makes_get_on_invalid_route(context):
    context.response = context.client.get('/invalid-route')

@then(u'user gets a 404 error')
def step_then_user_get_error_message(context):
    assert context.response.status_code == 404

@given(u'user is on the greet page')
def step_given_user_on_greet_page(context):
    context.client = app.test_client()

@when(u'user makes GET on "/greet/Alice"')
def step_when_user_makes_get_on_greet_page(context):
    context.response = context.client.get('/greet/Alice')

@then(u'user gets the message "Hello, Alice!"')
def step_then_user_get_greet_message(context):
    assert context.response.data.decode() == 'Hello, Alice!'

@given(u'user is on the date page')
def step_give_user_on_date_page(context):
    context.client = app.test_client()

@when(u'user makes GET on "/date"')
def step_when_user_makes_get_on_date(context):
    context.response = context.client.get('/date')

@then(u'user gets the current date')
def step_then_user_gets_current_date(context):
    expected_date = f'Current date: {datetime.now().strftime("%Y-%m-%d")}'
    assert context.response.data.decode() == expected_date



