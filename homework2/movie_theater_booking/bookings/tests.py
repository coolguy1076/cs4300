from django.test import TestCase
from .models import Movie

# Create your tests here.

class MovieTest(TestCase):

    def test_movie_creation(self):

        movie = Movie.objects.create(
            title="Test Movie",
            description="Test Description",
            release_date="2025-01-01",
            duration=120
        )

        self.assertEqual(movie.title, "Test Movie")