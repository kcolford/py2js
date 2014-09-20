import logging
import webapp2

out = """Hi there!

%s

"""
class Echo(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write(out % (self.request))

app = webapp2.WSGIApplication([('/py2js/.*', Echo)],
                              debug=True)
