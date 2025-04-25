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

  Scenario: User accesses the greet page with a name
    Given user is on the greet page
    When user makes GET on "/greet/Alice"
    Then user gets the message "Hello, Alice!"

  Scenario: User accesses the date page
    Given user is on the date page
    When user makes GET on "/date"
    Then user gets the current date