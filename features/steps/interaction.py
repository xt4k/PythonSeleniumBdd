import allure
from behave import *

from tests.page_model.base_page import BasePage
from tests.page_model.new_post_page import NewPostPage

use_step_matcher("re")


@when('User click on "(.*)" link')
@allure.step('User click on {link_text} link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.navigation
    match_link = [lnk for lnk in links if lnk.text == link_text]
    if len(match_link) > 0:
        match_link[0].click()
    else:
        raise RuntimeError("Not fount link with text: " + link_text)


@when('User enter "(.*)" in the "(.*)" field')
@allure.step('User enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = NewPostPage(context.driver)
    page.form_field(field_name).send_keys(content)



@when('User press "submit" button')
@allure.step('User press "submit" button')
def step_impl(context):
    page = NewPostPage(context.driver)
    page.submit_button.click()
