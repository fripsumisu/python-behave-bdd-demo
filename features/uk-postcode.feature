# Created by Philip Smith on 16/01/2025
Feature: Searching postcode locations
  As a nosey parker
  I wish to be able to identify a valid UK postal code
  So that I may understand more geospatial and location data

  Scenario: Searching for a valid well-formed postcode
    Given a postcode value of "SW1A 2AA"
    When I query the postcode service
    Then I can see the administrative district is "Westminster"

  Scenario: Searching for an invalid postcode
    Given a postcode value of "No Such Postcode"
    When I query the postcode service
    Then I will see an message containing the error "Invalid postcode"