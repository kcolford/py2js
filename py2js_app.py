import logging
import webapp2

from trans import translate

class Translate(webapp2.RequestHandler):
    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'
        python_string = self.request.get('python_string')
        self.response.write(translate(python_string))

class TestTranslate(webapp2.RequestHandler):
    def get(self):

        f = open('py2js/test_translate.html')
        self.response.write(f.read())

app = webapp2.WSGIApplication([('/py2js/translate/', Translate),
                               ('/py2js/test_translate/', TestTranslate)
                              ],
                              debug=True)
