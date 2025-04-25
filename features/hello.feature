
Feature: Show welcome message
  Scenario: User accesses the main page
    Given user is on the main page
    When user makes GET on "/"
    Then user gets the message "Hello, World!"
