Feature: Login Functionality


  Scenario Outline: Login with valid credentials
    Given I navigated to login page
    When i enter valid email address "<email>" and valid password "<password>"
    And i click on Login button
    Then i should get exit
    Examples:
    |email                     |password    |
    |xasal82798@heweek.com     |lohi        |



  Scenario: Login with valid mail id and invalid password
    Given I navigated to login page
    When i enter valid email address "xasal82798@heweek.com" and in_valid password "loki"
    And i click on Login button
    Then i should get warring message as


  Scenario: Login with invalid mail id and invalid password
    Given I navigated to login page
    When i enter invalid email address "xasal82798@heweek12.com" and invalid password "lokii"
    And i click on Login button
    Then i should get warring message as


  Scenario: Login with no email id and password
    Given I navigated to login page
    When i wont enter the email id " " and password " "
    And i click on Login button
    Then i should get warring message as

