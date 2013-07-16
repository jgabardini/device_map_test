import requests
import re
import csv


CHROME_UA = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36'
URL_MOBILE = 'http://m.your.site/'


class DocType:
	
	def __init__(self, text):
		self.text = text

	def doctype(self):
		dt = re.search('(<!DOCTYPE.*?\>)', self.text, re.MULTILINE | re.IGNORECASE | re.DOTALL)
		return (dt.group(0).
				replace('\n', '').
				replace('\r', '').
				replace('\t', '')
				) if dt else None

	def is_wap(self):
		return -1 < self.doctype().lower().find('mobile')


	def is_html4(self):
		return -1 < self.doctype().lower().find('html 4')


	def is_html5(self):
		return -1 < self.doctype().lower() == '<!doctype html>'

	def is_languaje(self, languaje):
		return	self.is_wap() if languaje == 'WAP' else \
				self.is_html4() if languaje == 'HTML4' else \
				self.is_html5() if languaje == 'HTML5' else \
				False

def map_device(url=URL_MOBILE, user_agent=CHROME_UA):
	header = {
		'User-Agent': user_agent  
	}
	r = requests.get(url=url, headers=header)
	return r

def test_UAs():
	with open('user-agents.csv', 'rb') as uafile:
		uareader = csv.reader(uafile)
		for uarow in uareader:
			if uarow[0] != '#':	
				yield check_ua, uarow[1], uarow[0]

def detect_lang(ua):
	response = map_device(user_agent=ua)
	dt = DocType(response.text)
	return ("WAP" * dt.is_wap() +
			"HTML4" * dt.is_languaje("HTML4") +
			"HTML5" * dt.is_languaje("HTML5")
	)

def check_ua(ua, languaje):
	response = map_device(user_agent=ua)
	dt = DocType(response.text)
	assert dt.is_languaje(languaje)

if __name__ == "__main__":
    for f, ua, languaje in test_UAs():

    	print '%s,"%s"' % (detect_lang(ua), ua)
