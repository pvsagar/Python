# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:25:50 2018

@author: VidyaSagar
"""

import media
import fresh_tomatoes

bahubali = media.Movie("Bahubali",
                       "A story of a Legend",
                       "http://s3.india.com/wp-content/uploads/2017/05/baahubali-2-poster.jpg",
                       "https://www.youtube.com/watch?v=qD-6d8Wo3do")
# print(bahubali.poster_image_url)
# print(bahubali.storyline)
# bahubali.show_trailer()
Deadpool = media.Movie("Deadpool",
                       "A story of a Deadpool",
                       "http://cdn.collider.com/wp-content/uploads/2018/02/deadpool-2-poster.jpg",
                       "https://www.youtube.com/watch?v=ONHBaC-pfsk")

Deadpool2 = media.Movie("Deadpool 2",
                       "A story of Deadpool continues",
                       "http://cdn.collider.com/wp-content/uploads/2018/02/deadpool-2-poster.jpg",
                       "https://www.youtube.com/watch?v=D86RtevtfrA")

movies =[bahubali, Deadpool, Deadpool2]
# fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
