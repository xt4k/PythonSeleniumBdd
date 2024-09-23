import allure
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from tests.page_model.blog_page import BlogPage
from tests.page_model.home_page import HomePage
from tests.page_model.new_post_page import NewPostPage

use_step_matcher("re")


# -*- coding: utf-8 -*-

@given('User on the home page')
@allure.step('User on the home page')
def step_impl(context):
    context.driver = get_chrome_driver()
    page = HomePage(context.driver)

    context.driver.get(page.url)


@step('User on the blog page')
@allure.step('User on the blog page')
def step_impl(context):
    context.driver = get_chrome_driver()

    page = BlogPage(context.driver)
    context.driver.get(page.url)


def get_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--start-maximized')
    service = Service(executable_path="C:\\Users\\Admin\\Downloads\\chrome_web_driver\\chromedriver.exe")
    driver = webdriver.Chrome(
        service=service,
        options=chrome_options
    )
    return driver


@given('User on the new post page')
@allure.step('User on the new post page')
def step_impl(context):
    context.driver = get_chrome_driver()

    page = NewPostPage(context.driver)
    context.driver.get(page.url)


@then("User navigated to the Blog page")
@allure.step("User navigated to the Blog page")
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url


@then("User navigated to the home page")
@allure.step("User navigated to the home page")
def step_impl(context):
    expected_url = HomePage(context.driver).url
    actual_url = context.driver.current_url
    assert actual_url == expected_url, f"Expected URL to be '{expected_url}', but got '{actual_url}' instead."
