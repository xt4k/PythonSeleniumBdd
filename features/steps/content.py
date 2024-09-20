import allure
from behave import *

from tests.page_model.base_page import BasePage
from tests.page_model.blog_page import BlogPage

use_step_matcher("re")


@then('There is a title shown on the page')
@allure.step('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@then('The title tag has content "(.*)"')
@allure.step('The title tag has content "(.*)"')
def step_impl(context, title_text):
    page = BasePage(context.driver)
    assert page.title.text == title_text


@then('There is a post section on the page')
@allure.step('There is a post section on the page')
def step_impl(context):
    page = BlogPage(context.driver)

    assert page.posts_section.is_displayed()


@then('User see a new post with title "(.*)" in the posts section')
@allure.step('User see a new post with title "(.*)" in the posts section')
def step_impl(context, title):
    page = BlogPage(context.driver)
    posts_with_title = [post for post in page.posts if post.text == title]

    assert len(posts_with_title) > 0
    assert all([post.is_displayed() for post in posts_with_title])
