Feature: Change user password
  Scenario: Enter valid passwords
    Given lunch the browser
    Then navigate to login page and enter the login details "saisai@gmail.com" "saisai"
    Then click on change your password
    And enter the new password "saisai" and conform password "saisai"
    Then click on continue button
    And i should get a success message in page


  Scenario: Enter valid passwords and come back without continue
    Given lunch the browser
    Then navigate to login page and enter the login details "saisai@gmail.com" "saisai"
    Then click on change your password
    And enter the new password "sailoki" and conform password "sailoki"
    Then click on back button


  Scenario: Enter random passwords
    Given lunch the browser
    Then navigate to login page and enter the login details "saisai@gmail.com" "saisai"
    Then click on change your password
    And enter the new password "lokisai" and conform password "saisai"
    Then click on continue button
    And i should get a conform password not match message in page

  @newandconformpassword
  Scenario: Enter less than 4 characters in new password field and more then 4 characters in conform password field
    Given lunch the browser
    Then navigate to login page and enter the login details "saisai@gmail.com" "saisai"
    Then click on change your password
    And enter the new password "lok" and conform password "saisai"
    Then click on continue button
    And i should get a new password warring message and conform password warring message in page

  @newpassword
  Scenario: Enter less than 4 characters in new password field
    Given lunch the browser
    Then navigate to login page and enter the login details "saisai@gmail.com" "saisai"
    Then click on change your password
    And enter the new password "lok" and conform password "lok"
    Then click on continue button
    And i should get a new password warring message in page

  @finalstep
  Scenario: do not enter any text in fields
    Given lunch the browser
    Then navigate to login page and enter the login details "saisai@gmail.com" "saisai"
    Then click on change your password
    And enter the new password and conform password
    Then click on continue button
    And i should get a warring message in page
