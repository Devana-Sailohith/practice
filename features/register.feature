Feature: Register functionality

  Background:
    Given lunch the browser

  @completed
  Scenario: Register with valid details
    Then navigate to register web page
    And give first,last name and telephone
    And give password and conform password
    And subscribe and privacy policy
    Then click on continue
    And click continue to complete register

  @completed
  Scenario: Register with already registered account details
    Then navigate to register web page
    And give first,last name and telephone of existing customer
    And give password and conform password of existing customer
    And subscribe and privacy policy
    Then click on continue
    Then i should get an error as Warning: E-Mail Address is already registered!
