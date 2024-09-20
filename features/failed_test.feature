@allure.label.epic:Web_Graphic_User_Interface_Bug
@allure.label.suite:User_Interface
@allure.label.subSuite:Page_title_info
@allure.label.parentSuite:Top_User_Interface_information
Feature: Failed test example

  @trivial
  @allure.label.owner:Petro_M
  @allure.label.story:Home_page
  @allure.link:https://dev.example.com/id-2323
  @allure.issue:UI-234
  @allure.tms:TMS-687
  @allure.label.allure_id:58123
  Scenario: Failed test for navigation from Home to Blog (but we expect home) page
    Given User on the home page
    When User click on "Go to blog" link

    #vvv Failed step vvv
    Then User navigated to the home page
    #^^^ Failed step ^^^
