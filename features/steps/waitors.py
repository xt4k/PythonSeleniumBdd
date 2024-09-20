import allure
from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators.blog_page import BlogPageLocators


use_step_matcher("re")


@given('User wait for posts to load')
@allure.step('User wait for posts to load')
def step_impl(context):
    WebDriverWait(context.driver, 5).until(
        expected_conditions.visibility_of_element_located(BlogPageLocators.POSTS_SECTION)
    )