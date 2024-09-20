from tests.locators.blog_page import BlogPageLocators
from tests.page_model.base_page import BasePage


# -*- coding: utf-8 -*-

class BlogPage(BasePage):

    @property
    def url(self):
        return super(BlogPage, self).url + '/blog'

    @property
    def posts_section(self):
        return self.driver.find_element(*BlogPageLocators.POSTS_SECTION)

    @property
    def posts(self):
        return self.driver.find_elements(*BlogPageLocators.POST)

    @property
    def add_post_link(self):
        return self.driver.find_elements(*BlogPageLocators.ADD_POST_LINK)
