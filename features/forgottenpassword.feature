

Feature: Forgot password

  Background:
    Given lunch the browser
    Then navigate to loginpage
    And click on forgotten password option


  Scenario: valid email id for forgot password functionality
    And enter registered email id
    And click on continue
    Then a message will be displayed as An email with a confirmation link has been sent your email address.


  Scenario: invalid email id for forgot password functionality
    And enter invalid email id
    And click on continue
    Then a message will be displayed as Warning: The E-Mail Address was not found in our records, please try again!