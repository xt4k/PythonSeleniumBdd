@allure.label.epic:General_post_page_functionality
@allure.label.owner:Yuriy_L
@allure.label.suite:Posts
@allure.label.subSuite:Posts_CRUD_operation
@allure.label.parentSuite:Application_general_functionality
Feature: Verify post's general functionality

  @blocker
  @allure.label.story:Post_on_blog_page
  @allure.link:https://dev.example.com/id-236544
  @allure.label.allure_id:12344
  @allure.issue:UI-8721
  @allure.tms:TMS-9641
  Scenario: Blog page loads the posts
    Given User on the blog page
    And User wait for posts to load
    Then There is a post section on the page


  @critical
  @allure.label.story:New_post
  @allure.label.allure_id:12344
  @allure.link:https://dev.example.com/id-2365
  @allure.issue:UI-8721
  @allure.tms:TMS-9641
  Scenario: User can create new posts
    Given User on the new post page
    When User enter "Test Post" in the "title" field
    And User enter "Test Content" in the "content" field
    And User press "submit" button
    Then User on the blog page
    Given User wait for posts to load
    Then User see a new post with title "Test Post" in the posts section