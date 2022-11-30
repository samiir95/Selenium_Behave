Feature: Homepage

  Scenario: Successful login
    Given I open the 8 tracks website
    When I click the log in button
    And I enter my username
    And I type my password
    And Im submit the log in button
    Then I should see a validation message
