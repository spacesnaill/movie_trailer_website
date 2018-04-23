import urllib
import urllib.error
import json
import time
from http import client


class The_Movie_DB:
    def __init__(self, api_key):
        self.api_key = api_key
        self.connection = client.HTTPSConnection("api.themoviedb.org")

    def get_movie_id(self, movie_name, year=''):
        # cleans up the name to something that can actually be used in an http request
        movie_name = urllib.parse.quote(movie_name)

        # search the movie database for a particular name along with the year if that's available information
        # returns the id of the first movie that comes out o the search
        # try to make a request, if throttled then back off by the amount that it asks us to
        try:
            self.connection.request(
                "GET",
                f"/3/search/movie?{year}&include_adult=false&page=1&query={movie_name}&language=en-US&api_key={self.api_key}&append_to_response=videos")
            result = self.connection.getresponse()
            data = result.read()
            if data == None:
                return None
            movie_info = json.loads(data)
            try:
                return movie_info['results'][0]['id']
            except (IndexError, KeyError) as index_error:
                return None
        except urllib.error.HTTPError as error:
            print(error.reason)
            time.sleep(error.headers['Retry-After'])
            # recurseively call to get the output we want after backing off
            return self.get_movie_id(movie_name, year)

    def get_movie_data(self, movie_id, *args):
        # takes in the id of the movie and a variable number of arguments
        try:
            self.connection.request(
                "GET",
                f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={self.api_key}&language=en-US&append_to_response=videos")
            result = self.connection.getresponse()
            data = result.read()
            movie_info = json.loads(data)

            output = {}

            for data_request in args:
                if data_request == 'trailer' or data_request == 'video' or data_request == 'videos':
                    try:
                        output[data_request] = movie_info['videos']['results'][0]['key']
                    except IndexError as index_error:
                        output[data_request] = '5Peo-ivmupE'
                else:
                    output[data_request] = movie_info[data_request]
            return output
        except urllib.error.HTTPError as error:
            print(error.reason)
            time.sleep(error.headers['Retry-After'])
            # recurseively call to get the output we want after backing off
            return self.get_movie_data(movie_id, args)
