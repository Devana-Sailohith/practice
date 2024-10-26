Feature: Searching for the product

  Background:
    Given lunch the browser

  Scenario: Search for valid product
    When browser has lunched enter the product "MacBook"
    Then click search button
    And get the product title name "MacBook"


  Scenario: Search for invalid product
    When browser has lunched enter the product "Asus laptop"
    Then click search button
    And i should get a product missing warring


  Scenario: Search without entering product name
    When browser has lunched enter the product
    Then click search button
    And i should get a product missing warring