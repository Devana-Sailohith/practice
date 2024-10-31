Feature: Contact Us Function

  @Regression
  Scenario: Enter the details
    Given lunch the browser
    When go to the website and login "saisai@gmail.com" "saisai"
    Then click the contact us option
    And enter the name, email, and the enquiry
    Then click the submit button
    And last click the continue buttton

  @Regression
  Scenario: Enter the details
    Given lunch the browser
    When go to the website and login "saisai@gmail.com" "saisai"
    Then click the contact us option
    And enter the name, email, and the enquiry
    Then click the submit button
    And last click the continue buttton