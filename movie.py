class Movie:
    # Movie call holds data about the movie in question
    # For this program that data comes from The Movie Database
    def __init__(self, title, description, poster, trailer):
        self.title = title  # the title of the movie
        self.desc = description  # a description of the movie
        # link to the poster art for the movie, stored on the movie database
        self.poster_image_url = poster
        # youtube link to the movie's trailer or a placeholder video if no
        # trailer was found
        self.trailer_youtube_url = trailer
