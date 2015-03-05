import webapp2

form = """
    <form method="post" action="/testform">
      <input name="q">
      <input type="submit">
    </form>
"""
class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write('Hello Udacity!')
        self.response.out.write(form)


class TestHandler(webapp2.RequestHandler):
    def post(self):
        # self.response.write('Hello Udacity!')
        q = self.request.get("q")
        self.response.out.write(q)

        # self.response.headers['Content-Type'] = 'text/plain'
        # self.response.write(self.request)


app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/testform',TestHandler)],
                               debug=True)
