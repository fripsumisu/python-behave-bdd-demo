from typing import assert_type

from behave import *
from python_behave_bdd_demo import uk_postcode_checker
from python_behave_bdd_demo.uk_postcode_checker import search_town_from_postcode


@given(u'a postcode value of "{postcode}"')
def step_impl(context, postcode):
    assert postcode is not None
    assert_type(postcode, str)
    context.postcode = postcode


@when("I query the postcode service")
def step_impl(context):
    search_result = search_town_from_postcode(context.postcode)
    assert search_result is not None
    assert len(search_result) > 0
    context.search_result = search_result



@then(u'I can see the administrative district is "{admin_district}"')
def step_impl(context, admin_district):
    assert admin_district == context.search_result