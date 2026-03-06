from behave import given, when, then
from bookings.models import Movie, Seat, Booking
from django.contrib.auth.models import User

@given("I am a logged-in user")
def step_impl(context):
    context.user = User.objects.create_user(username="testuser", password="pass")

@given("a movie exists")
def step_impl(context):
    context.movie = Movie.objects.create(
        title="Test Movie",
        description="A movie for testing",
        release_date="2025-01-01",
        duration=120
    )

@given("a seat is available")
def step_impl(context):
    context.seat = Seat.objects.create(seat_number="A1", is_booked=False)

@when("I book the seat")
def step_impl(context):
    Booking.objects.create(movie=context.movie, seat=context.seat, user=context.user)
    context.seat.is_booked = True
    context.seat.save()

@then("the seat should be marked as booked")
def step_impl(context):
    context.seat.refresh_from_db()
    assert context.seat.is_booked is True

@then("the booking should be recorded for the user")
def step_impl(context):
    booking_exists = Booking.objects.filter(user=context.user, movie=context.movie, seat=context.seat).exists()
    assert booking_exists is True