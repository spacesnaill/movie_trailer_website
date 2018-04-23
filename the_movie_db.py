import requests
import time
from http import client


class The_Movie_DB:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_movie_id(self, movie_name):
        # using the Requests module, we can organize
        # all the parameters into a dictionary
        # and then pass them off to the get Request
        payload = {'include_adult': 'false',
                   'page': '1',
                   'query': movie_name,
                   'language': 'en-US',
                   'api_key': self.api_key, }

        # make the request to the database
        # the documentation of the Requests library was a big help here
        r = requests.get(
            'http://api.themoviedb.org/3/search/movie', params=payload)
        if r.status_code == 429:
            # status code 429 means we sent too many requests.
            # 'Retry-After' is the amount of seconds that it wants us to wait
            # before sending another request.
            time.sleep(int(r.headers.get('Retry-After')))
            return self.get_movie_id(movie_name)
        else:
            # return the id of the first movie in the search results
            return r.json().get('results')[0].get('id')

    def get_movie_data(self, movie_id, *args):
        # make a http request to the movie database using the movie_id
        # proivded as a parameter to get that particular movie's data
        payload = {'api_key': self.api_key, 'language': 'en-US',
                   'append_to_response': 'videos'}
        r = requests.get(
            'https://api.themoviedb.org/3/movie/{}'.format(movie_id),
            params=payload)

        if r.status_code == 429:
            # status code 429 means we sent too many requests.
            # 'Retry-After' is the amount of seconds that it wants us to wait
            # before sending another request.
            time.sleep(int(r.headers.get('Retry-After')))
            return self.get_movie_data(movie_id, args)
        data_output = {}

        for element in args:
            if element == 'videos' or element == 'video' or element == 'trailer':
                try:
                    data_output[element] = r.json().get(
                        'videos').get('results')[0].get('key')
                except IndexError as i_error:
                    # appends a placeholder video key if there is no video
                    data_output[element] = '5Peo-ivmupE'
            else:
                try:
                    data_output[element] = r.json().get(element)
                except KeyError as k_error:
                    # appends None if the argument isn't found
                    data_output[element] = None
        # return a dictionary with the data requested
        return data_output
