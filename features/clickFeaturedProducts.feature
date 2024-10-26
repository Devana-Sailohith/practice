Feature: With login and without login clicking and Adding the featured product from the web site
  Background:
    Given lunch the browser
    When browser has lunched give the weblink to open
  @firstProduct
  Scenario: click first product and add it to the cart
    Then click the featured first product
    And enter the quantity "2"
    Then verify the featured first product title and the actual product title
    And Add it to the cart

  @secondProduct
  Scenario: click second product and add it to the cart
    Then click the featured second product
    And enter the quantity "2"
    Then verify the featured second product title and the actual product title
    And Add it to the cart

  @thirdProduct
  Scenario: click third product and add it to the wishlist
    Then click the featured third product
    Then verify the featured third product title and the actual product title
    And Add it to the wish list


  @loginWishList @firstproduct
  Scenario: login and click first product and add it to the cart
    Then login into the application "saisai@gmail.com" "saisai"
    Then click the featured first product
    And enter the quantity "2"
    Then verify the featured first product title and the actual product title
    And Add it to the cart

  @loginWishList @secondproduct
  Scenario: login and click second product and add it to the cart
    Then login into the application "saisai@gmail.com" "saisai"
    Then click the featured second product
    And enter the quantity "2"
    Then verify the featured second product title and the actual product title
    And Add it to the cart

  @loginWishList @thirdproduct
  Scenario: login and click third product and add it to the wishlist
    Then login into the application "saisai@gmail.com" "saisai"
    Then click the featured third product
    Then verify the featured third product title and the actual product title
    And Add it to the wish list
