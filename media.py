import webbrowser


class Movie:

    def __init__(
            self,
            title,
            storyline,
            poster_image_url,
            trailer_youtube_url):
        """ This contruction is used to insert the title, storyline, image and trailer
        from movie.

        Args:
        title (str): The tilte movie.
        storyline (str): The storyline.
        poster_image_url(str): That image that represent the movie.
        trailer_youtube_url(str): The URL trailer from movie.

        Returns:
        Movie: A new intantiate movie with the args received.
    """

        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
