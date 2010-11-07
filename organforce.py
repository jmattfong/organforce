import cgi
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

import os
from google.appengine.ext.webapp import template

class Greeting(db.Model):
    author = db.UserProperty()
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp.RequestHandler):
    def get(self):
        greetings_query = Greeting.all().order('-date')
        greetings = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
            current_user = users.get_current_user()
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            current_user = ''

        template_values = {
            'greetings': greetings,
            'url': url,
            'url_linktext': url_linktext,
            'current_user': current_user,
            }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))
        
class Apps(webapp.RequestHandler):
	def get(self):
	
		if users.get_current_user():
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Logout'
			current_user = users.get_current_user()
		else:
			url = users.create_login_url(self.request.uri)
			url_linktext = 'Login'
			current_user = ''
            
		template_values = {
			'url': url,
			'url_linktext': url_linktext,
			'current_user': current_user,
			}
		path = os.path.join(os.path.dirname(__file__), 'apps.html')
		self.response.out.write(template.render(path, template_values))
		
class Donate(webapp.RequestHandler):
	def get(self):
		if users.get_current_user():
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Logout'
			current_user = users.get_current_user()
		else:
			url = users.create_login_url(self.request.uri)
			url_linktext = 'Login'
			current_user = ''
            
		template_values = {
			'url': url,
			'url_linktext': url_linktext,
			'current_user': current_user,
			}
		path = os.path.join(os.path.dirname(__file__), 'donate.html')
		self.response.out.write(template.render(path, template_values))
		
class About(webapp.RequestHandler):
	def get(self):
		if users.get_current_user():
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Logout'
			current_user = users.get_current_user()
		else:
			url = users.create_login_url(self.request.uri)
			url_linktext = 'Login'
			current_user = ''
            
		template_values = {
			'url': url,
			'url_linktext': url_linktext,
			'current_user': current_user,
			}
		path = os.path.join(os.path.dirname(__file__), 'about.html')
		self.response.out.write(template.render(path, template_values))
	

class Guestbook(webapp.RequestHandler):
    def post(self):
        greeting = Greeting()

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        greeting.put()
        self.redirect('/')

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/apps', Apps),
                                      ('/donate', Donate),
                                      ('/about', About),
                                      ('/sign', Guestbook)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()