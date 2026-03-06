from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

#Create your views here

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "bookings/movie_list.html", {"movies": movies})


@login_required
def book_seat(request, movie_id):

    movie = Movie.objects.get(id=movie_id)
    seats = Seat.objects.filter(is_booked=False)

    if request.method == "POST":
        seat_id = request.POST["seat"]
        seat = Seat.objects.get(id=seat_id)

        Booking.objects.create(
            movie=movie,
            seat=seat,
            user=request.user
        )

        seat.is_booked = True
        seat.save()

        return redirect("booking_history")

    return render(request, "bookings/seat_booking.html", {
        "movie": movie,
        "seats": seats
    })


@login_required
def booking_history(request):

    bookings = Booking.objects.filter(user=request.user)

    return render(request, "bookings/booking_history.html", {
        "bookings": bookings
    })