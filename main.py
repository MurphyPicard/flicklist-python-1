import webapp2
from random import randint

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # # TODO: make a list with at least 5 movie titles
        movies = ["Edge of Tomorrow", "Home Alone", "Bad Santa", "Finding Nemo", "Rat Race"]
        #
        # # TODO: randomly choose one of the movies, and return it
        # movies.random
        return movies[randint(0,4)]

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day!</h1>"
        content += "<p>" + movie + "</p>"
        content += "<h1>The Movie Tomorrw</h1>"
        movie = self.getRandomMovie()
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
