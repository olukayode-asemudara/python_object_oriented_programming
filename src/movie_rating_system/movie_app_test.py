from unittest import TestCase
from .movie_rating import MovingRating
from .movie import Movie

class MovieAppTest(TestCase):

    def setUp(self):
        self.rating = MovingRating()
        self.movie = Movie("koto aiye", "Dele Giwa", 2005)

    def test_rate_movie(self):
        self.rating.rate_movie("koto aiye", 3)
        assert len(self.rating.get_rating()) == 1

    def test_unrate_movie(self):
        self.rating.rate_movie("koto aiye", 3)
        assert len(self.rating.get_rating()) == 0






