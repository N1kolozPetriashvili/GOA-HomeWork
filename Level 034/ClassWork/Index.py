favorite_movies = ("Squid Game", "The Dark Knight", "Nabeglavi", "The Matrix", "the flash", "kill bill")

first_movie, *other_movies = favorite_movies

print("First favorite movie: ", first_movie)
print("Other favorite movies: ", other_movies)

first_movie, *other_movies, last_movie = favorite_movies

print("First favorite movie: ", first_movie)
print("Last favorite movie: ", last_movie)