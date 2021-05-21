Feature: Requests Feature

    Scenario: Get the store inventory
        When I get the store inventory
        Then I verify that I receive "200" status code

    Scenario: Using Tumblr web app
        Given I am in HomePage
        When  I click in Login in the middle of page
