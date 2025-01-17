from typing import assert_type

from behave import *
from python_behave_bdd_demo import demo_app

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False

@given(u'my name is "{name}"')
def step_impl(context, name):
    assert name is not None
    assert_type(name, str)
    context.input_name = name


@when(u'I run the application')
def step_impl(context):
    ut_greeting = demo_app.user_greeting(context.input_name)
    assert ut_greeting is not None
    context.output_greeting = ut_greeting


@then(u'I shall see the message "{greeting}"')
def step_impl(context, greeting):
    assert greeting is not None
    expected_greeting = "Hello " + context.input_name
    assert greeting == expected_greeting
