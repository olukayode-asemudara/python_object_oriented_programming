from .movie import Movie

class MovingRating:
    def __init__(self):
        self.movies = []

    def add(self, title:str, producer, year):
        title = title.lower()
        movie = Movie(title, producer, year)
        self.movies.append(movie)

    def get_movies(self):
        return self.movies

    def rate_movie(self, title:str, rating:int):
        if rating < 0 or rating > 5:
            raise ValueError("rating must be between 0 and 5")
        for movie in self.movies:
            if movie.title == title.lower():
                rating = movie.rating.append(rating)

    def unrate_movies(self, title:str, rating:int):
        for movie in self.movies:
            if movie.title == title.lower():
                if rating: return 0
            return None
        return None

    def get_rating(self):
        for movie in self.movies:
            return movie.rating
        return None