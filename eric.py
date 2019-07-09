import urllib2
import requests
from bs4 import BeautifulSoup

def getEricAuth():
	login_url = "http://scumbag-control/auth.asp"
	target_url = "http://scumbag-control/title_app.asp"

	login_params = {'login' : 'administrator', 'password' : 'belkin', 'action_login.x' : '1', 'action_login.y' : '1'}

	s = requests.Session()
	s.post(url = login_url, data = login_params)
	r = s.get(url = target_url)

	soup = BeautifulSoup(r.text, features="lxml")

	applet_id =  soup.find('param', attrs={'name' : 'APPLET_ID'}).get('value');
	return applet_id
