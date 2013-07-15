import requests
import re

# http://www.useragentstring.com/pages/useragentstring.php
# http://user-agent-string.info/list-of-ua
UA = [
	# Chrome
	'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36',
	'NOKIAN82 UCWEB',
]

CHROME_UA = UA[0]
URL_MOBILE = 'http://m.olx.com.ar/'


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


def map_device(url=URL_MOBILE, user_agent=CHROME_UA):
	header = {
		'User-Agent': user_agent  
	}
	r = requests.get(url=url, headers=header)
 	
		# print '-' * 10
		# print r.headers
		# print r.history
	return r


