Feature: Remove out of stock item from the wish list

  Background:
    Given lunch the browser
    When go the the website
    Then Login to the application "saisai@gmail.com" "saisai"
    And click the wish list to modify

  @Regression
  Scenario: without removing the out of stock
    And after entering into wish list then click continue button
    Then logout from the application

  @Regression
  Scenario: remove the out of stock
    Then check the out of stock items and remove
    And after removing the items click continue button
    Then logout from the application
