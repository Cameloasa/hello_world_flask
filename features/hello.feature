# language: en

Feature: Show welcome message

  Scenario: User accesses the main page
    Given user is on the main page
    When user makes GET on "/"
    Then user gets the message "Hello, World!"

  Scenario: User accesses an invalid page
    Given user is on the application
    When user makes GET on "/invalid-route"
    Then user gets a 404 error
