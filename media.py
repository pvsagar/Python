# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:23:03 2018

@author: VidyaSagar
"""


import webbrowser


class Movie():
    """ This provides a way to display your movies along with trailers """
    VALID_RATINGS = ["G","PG","PG13","R"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
