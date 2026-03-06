Feature: Booking seats
  As a registered user
  I want to book a seat for a movie
  So that I can attend the movie

  Scenario: Book a seat successfully
    Given I am a logged-in user
    And a movie exists
    And a seat is available
    When I book the seat
    Then the seat should be marked as booked
    And the booking should be recorded for the user