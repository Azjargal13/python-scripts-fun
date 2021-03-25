# this is movie.py which 
# only structure
# movie categories: regular, children, new releases
from enum import Enum
class Movie(Enum):
    _movie_name =""
    _movie_price=0
    REGULAR=0
    CHILDREN =1
    NEWRELEASE=2

    def getMovieName(self, movie_name):
        _movie_name = movie_name

    def getMovieType(self, movie_name):
        # assign types depend on categories
        # identifies movie type by their name or idk
    
    def getMoviePrice(self, price):
        return _movie_price = price