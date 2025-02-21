from typing import assert_type

from behave import *
from python_behave_bdd_demo import uk_postcode_checker
from python_behave_bdd_demo.uk_postcode_checker import search_town_from_postcode_double, search_postal_town


@given(u'a postcode value of "{postcode}"')
def step_impl(context, postcode):
    assert postcode is not None
    assert_type(postcode, str)
    context.postcode = postcode


@when("I query the postcode service")
def step_impl(context):
    search_result = search_postal_town(postcode=context.postcode)
    assert search_result is not None
    assert len(search_result) > 0
    context.search_result = search_result



@then(u'I can see the administrative district is "{admin_district}"')
def step_impl(context, admin_district):
    assert admin_district == context.search_result


@then('I will see an message containing the error "{error_message}"')
def step_impl(context, error_message):
    assert context.search_result == error_message