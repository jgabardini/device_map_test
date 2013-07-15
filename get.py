
import requests

# http://www.useragentstring.com/pages/useragentstring.php
# http://user-agent-string.info/list-of-ua
UA = [
	# Chrome
	'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36',
	'NOKIAN82 UCWEB',
]

def devise_map(user_agent):
	header = {
		'User-Agent': user_agent  
	}
	r = requests.get('http://m.olx.com.ar/', headers=header)

	print '-' * 10
	print r.headers
	print r.history


for ua in UA:
	devise_map(ua)
