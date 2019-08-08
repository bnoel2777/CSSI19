
import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h1>Hello, Ben!</h1>')
class AboutPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h3>this is about the page</h3>')
class newspage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h1>This is my new page</h1>')



routes =   [('/', MainPage),('/news', newspage)]
app = webapp2.WSGIApplication(routes, debug=True)
  
                                                                                                                   