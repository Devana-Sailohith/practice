Feature: Modify user address book

  Scenario: enter the address details
    Given lunch the browser
    Then navigate tot the login page "saisai@gmail.com" "saisai"
    Then click modify user address details
    Then enter the details "loki", "last", "company", "address1", "address2", "city", "postalcode", "India", "Andhra Pradesh"
    And click make it a non-default address
    And click continue button
  @newaddress
  Scenario: enter the required address details only
    Given lunch the browser
    Then navigate tot the login page "saisai@gmail.com" "saisai"
    Then click modify user address details
    Then enter the details "loki", "last", "address1", "city", "India", "Goa"
    And click make it a non-default address
    And click continue button
  @defaultaddress
  Scenario: enter the address details and make it as default address
    Given lunch the browser
    Then navigate tot the login page "saisai@gmail.com" "saisai"
    Then click modify user address details
    Then enter the details "loki", "last", "company", "address1", "address2", "city", "postalcode", "India", "Andhra Pradesh"
    And click make it a default address
    And click continue button
  @deleteGoa
  Scenario: Delete the specific address
    Given lunch the browser
    Then navigate tot the login page "saisai@gmail.com" "saisai"
    Then click modify user address details
    Then enter the state name "Goa" to delete the address
    Then logout
    And click on continue button to logout
