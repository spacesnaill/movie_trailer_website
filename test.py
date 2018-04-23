import requests

api_key = "aeaf03c5d04aa0655aa5b437097043b9"

payload = {'year': '1995', 'include_adult': 'false', 'page': '1',
           'query': 'Toy Story', 'language': 'en-US', 'api_key': api_key, }
r = requests.get(
    'http://api.themoviedb.org/3/search/movie', params=payload)
# ?api_key = {self.api_key} & language = en-US & append_to_response = videos"
q_payload = {'api_key': api_key, 'language': 'en-US',
             'append_to_response': 'videos'}
q = requests.get('https://api.themoviedb.org/3/movie/862', params=q_payload)

print(q.status_code)
print(q.json().get('title'))
