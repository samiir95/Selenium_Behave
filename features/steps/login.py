from behave import given, then, when
from selenium.webdriver.common.by import By


@given(u'I open the 8 tracks website')
def step_impl(context):
    context.home_page.navigate("https://8tracks.com/")


@when(u'I click the log in button')
def step_impl(context):
    context.home_page.click_element(context.home_page.LOGIN_BTN)


@when(u'I enter my username')
def step_impl(context):
    context.home_page.fill('myusername', context.home_page.USERNAME_FIELD)


@when(u'I type my password')
def step_impl(context):
    context.home_page.fill('mypassword', context.home_page.PASSWD_FIELD)


@when(u'Im submit the log in button')
def step_impl(context):
    context.home_page.click_element(context.home_page.SUBMIT_BUTTON)


@then(u'I should see a validation message')
def step_impl(context):
    context.home_page.assert_elementText('Login was unsuccessful', context.home_page.SUCCESSFULL_MSG)
