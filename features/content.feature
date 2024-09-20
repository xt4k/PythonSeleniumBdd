@allure.label.epic:Web_Graphic_User_Interface
@allure.label.suite:User_Interface
@allure.label.subSuite:Page_title_info
@allure.label.parentSuite:Top_User_Interface_information
@allure.label.layer:web
Feature: Test that pages have correct content

  @normal
  @allure.label.allure_id:6855
  @allure.label.owner:Yuriy_L
  @allure.label.story:Blog_page
  @allure.link:https://dev.example.com/id-2322
  @allure.issue:UI-123
  @allure.tms:TMS-45647
  Scenario:  Blog page has a correct title
    Given User on the blog page
    Then There is a title shown on the page
    Then The title tag has content "This is the blog page"


  @minor
  @allure.label.owner:Petro_M
  @allure.label.story:Home_page
  @allure.label.allure_id:12344
  @allure.link:https://dev.example.com/id-2323
  @allure.issue:UI-234
  @allure.tms:TMS-687
  Scenario: Home page has a correct title
    Given User on the home page
    Then There is a title shown on the page
    Then The title tag has content "This is the homepage"



