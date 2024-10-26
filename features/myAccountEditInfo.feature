Feature: Edit account info functionality

  Background:
    Given lunch browser

  Scenario Outline: Enter existing user info
    When navigate to login page "<email>" "<loginpassword>"
    Then click edit account info text
    And enter the first name, last name, email id, telephone num "<firstname>" "<lastname>" "<emailId>" "<telephone>"
    Then click continue button to update the details
    Then a message should come as success
    Examples:
    |email             |loginpassword|firstname|lastname|emailId           |telephone |
    |lohiloki@gmail.com|loki         |lohi     |loki    |lohiloki@gmail.com|1234567890|

  @missingFirstName
  Scenario Outline: Enter existing user info miss first name
    When navigate to login page "<email>" "<loginpassword>"
    Then click edit account info text
    And do not enter first name,enter the last name, email id, telephone num "sai" "saisai@gmail.com" "1234567890"
    Then click continue button to update the details
    Then a warring message should come
    Examples:
    |email             |loginpassword|
    |saisai@gmail.com  |saisai       |
