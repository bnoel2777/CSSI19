
import webapp2
import jinja2
import os

# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        t = the_jinja_env.get_template('templates/welcome.html')

        self.response.write(t.render())

class AboutPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h3>this is about the page</h3>')
class newspage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h1>This is my new page</h1>')
class Resultpage(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h3>result page</h3>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ')



class FavPage(webapp2.RequestHandler):
    def get(self):
        t = the_jinja_env.get_template('templates/welcome.html')
        favs = {"title":"My Favorite Websites","item1":"Google","item2":"Youtube","item3":"Twitter","item4":"Facebook"}
        self.response.write(t.render())
  
routes =   [('/', MainPage),
            ('/about', AboutPage)
            ('/news', Newspage)
            ('/result', Resultpage)]
app = webapp2.WSGIApplication(routes, debug=True)


  
                                                                                                                   