import movie
import the_movie_db
import fresh_tomatoes
import sys
# This product uses the TMDb API but is not endorsed or certified by TMDb.

# api key to make requests from the movie db
api_key = ""  # you will need to provide your own API key from themoviedb.org

# create a the_movie_db object called moviedb
# moved a lot of the api calls over to there to better organize things and
# make it easier to reuse it in the future
moviedb = the_movie_db.The_Movie_DB(api_key)
try:
    input_file = open('input.txt')
except FileNotFoundError as file_not_found:
    print("""File could not be located, make sure it is in the same directory
          as the program and is labeled 'input.txt'""")
    sys.exit(1)  # if the file could not be found, exit the program

input_list = input_file.readlines()
input_file.close()
movie_list = []
for index in range(0, len(input_list)):
    input_list[index] = input_list[index].strip()

for item in input_list:
    movie_id = moviedb.get_movie_id(item)
    if movie_id is None:
        continue  # if the movie not found, go to the next item
    movie_data = moviedb.get_movie_data(
        movie_id, "title", "overview", 'poster_path', 'trailer')
    poster_link = 'http://image.tmdb.org/t/p/w185//{}'.format(
        movie_data['poster_path'])
    trailer_link = 'https://www.youtube.com/watch?v={}'.format(
        movie_data['trailer'])
    movie_list.append(
        movie.Movie(movie_data['title'],
                    movie_data['overview'],
                    poster_link,
                    trailer_link))

fresh_tomatoes.open_movies_page(movie_list)
