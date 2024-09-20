@allure.label.epic:Inter_page_navigation
@allure.label.owner:Yuriy_L
@allure.label.suite:Application_pages_navigation
@allure.label.subSuite:Between_home_and_other_pages
@allure.label.parentSuite:Application_pages
Feature: Verify inter_pages navigation
  We can have a longer description
  Than can span a few lines

  @critical
  @allure.label.story:Navigate_from_home_page
  @allure.label.allure_id:12344
  @allure.link:https://dev.example.com/id-2365
  @allure.issue:UI-872154
  @allure.tms:TMS-964168
  Scenario: Navigation from Home to Blog page
    Given User on the home page
    When User click on "Go to blog" link
    Then User navigated to the Blog page

  @normal
  @allure.label.story:Navigate_from_Blog_page
  @allure.label.allure_id:12344
  @allure.link:https://dev.example.com/id-2365
  @allure.issue:UI-878812
  @allure.tms:TMS-89941
  Scenario: Navigation from Blog to Home page
    Given User on the blog page
    When User click on "Go to home" link
    Then User navigated to the home page