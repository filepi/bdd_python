Feature: Requests Feature

    Scenario: I make a GET Request
        When I get the store inventory
        Then I verify that I receive "200" status code