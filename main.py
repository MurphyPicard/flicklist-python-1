import webapp2
import cgi

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>FlickList</title>
</head>
<body>
    <h1>FlickList</h1>
"""

page_footer = """
</body>
</html>
# """

terrible_movies = ["Gigli"]

def getCurrentWatchlist():
    return ["Star Wars", "Star Trek", "Star Fox"]


class Index(webapp2.RequestHandler):

    def get(self):

        edit_header = "<h3>Edit My Watchlist</h3>"

        add_form = """
        <form action="/add" method="post">
            <label>
                I want to add
                <input type="text" name="new-movie"/>
                to my watchlist.
            </label>
            <input type="submit" value="Add It"/>
        </form>
        """

        crossoff_options = ""
        for movie in getCurrentWatchlist():
            crossoff_options += '<option value="{0}">{0}</option>'.format(movie)

        cross_off_form = """
        <form action="/cross-off" method="post">
            <label>
                I want to cross-off
                <select name="crossed-off-movie" />
                    {0}
                </select>
                from my watchlist.
            </label>
            <input type="submit" value="cross-off" />
        </form>
        """.format(crossoff_options)

        content = page_header + edit_header + add_form + cross_off_form + page_footer
        self.response.write(content)


class AddMovie(webapp2.RequestHandler):

    def post(self):
        # look inside the request to figure out what the user typed
        new_movie = self.request.get("new-movie")

        # build response content
        new_movie_element = "<strong>" + new_movie + "</strong>"
        sentence = new_movie_element + " has been added to your Watchlist!"

        content = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(content)

class CrossOffMovie(webapp2.RequestHandler):

    def post(self):
        old_movie = self.request.get("crossed-off-movie")

        if crossed_off_movie not in getCurrentWatchlist():
            error = "{0} is not in your watchlist so you can't cross it off".format("crossed_off_movie")
            error_escaped = cgi.escape(error, quote=True)
            # redirect to homepage, and include error as a query parameter in the URL
            self.redirect("/?error=" + error_escaped)

        old_movie_element = "<strikethrough>" + old_movie + "</strikethrough>"
        old_movie_confirmation = old_movie_element + "has been deleted from the watchlist"
        content = page_header + "<p>" + old_movie_confirmation + "</p>" + page_footer
        self.response.write(content)
# Create a new RequestHandler class called CrossOffMovie, to receive and
# handle the request from your 'cross-off' form. The user should see a message like:
# "Star Wars has been crossed off your watchlist".

app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/cross-off', CrossOffMovie)
], debug=True)
