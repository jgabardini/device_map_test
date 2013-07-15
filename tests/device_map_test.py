import unittest

from device_map import DocType

WAP_TEXT  = \
	"""<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE html PUBLIC "-//WAPFORUM//DTD XHTML Mobile 1.2//EN"
	"http://www.openmobilealliance.org/tech/DTD/xhtml-mobile12.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
	  <head>
	    <title>Hello world</title>
	  </head>
	  <body>
	    <p>Hello <a href="http://example.org/">world</a>.</p>
	  </body>
	</html>
	"""

HTML4_TEXT  = \
"""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
    <title>OLX Mobile</title>
<link href='/css/dummy-1373311203.css' type='text/css' rel="stylesheet" />
<link rel="shortcut icon" href="http://static03.olx-st.com/images/favicon.ico" type="image/x-icon" />
<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0; user-scalable: no" />
</head>
  <body>
    <p>Hello <a href="http://example.org/">world</a>.</p>
  </body>
</html>
"""

HTML5_TEXT  = \
"""<!doctype html>
<html>
<head>
    <title>OLX Mobile</title>
<link href='/css/dummy-1373311203.css' type='text/css' rel="stylesheet" />
<link rel="shortcut icon" href="http://static03.olx-st.com/images/favicon.ico" type="image/x-icon" />
<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0; user-scalable: no" />
</head>
  <body>
    <p>Hello <a href="http://example.org/">world</a>.</p>
  </body>
</html>
"""

class DeviceMap_DocType(unittest.TestCase):
	def test_for_wap(self):
		dt = DocType(WAP_TEXT)
		wap_doctype = (
			'<!DOCTYPE html PUBLIC "-//WAPFORUM//DTD XHTML Mobile 1.2//EN"'+
			'"http://www.openmobilealliance.org/tech/DTD/xhtml-mobile12.dtd">'
		)
		self.assertEquals(wap_doctype, dt.doctype())

	def test_for_wap(self):
		dt = DocType(WAP_TEXT)
		self.assertTrue(dt.is_wap(), "Not a WAP:" + dt.doctype())

	def test_for_html4(self):
		dt = DocType(HTML4_TEXT)
		self.assertTrue(dt.is_html4(), "Not a HTML4:" + dt.doctype())

	def test_for_html5(self):
		dt = DocType(HTML5_TEXT)
		self.assertTrue(dt.is_html5(), "Not a HTML5:" + dt.doctype())

	def test_is_languaje_wap(self):
		dt = DocType(WAP_TEXT)
		self.assertTrue(dt.is_languaje('WAP'), "Not a WAP:" + dt.doctype())
	
	def test_is_languaje_html4(self):
		dt = DocType(HTML4_TEXT)
		self.assertTrue(dt.is_languaje('HTML4'), "Not a HTML4:" + dt.doctype())
	
	def test_is_languaje_html5(self):
		dt = DocType(HTML5_TEXT)
		self.assertTrue(dt.is_languaje('HTML5'), "Not a HTML5:" + dt.doctype())
	
	def test_is_languaje_unknown(self):
		dt = DocType(HTML5_TEXT)
		self.assertTrue(dt.is_languaje('unknown'), "Lenguaje unknown should be false:" + dt.doctype())

