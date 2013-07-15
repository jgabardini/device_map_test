import unittest

from device_map import map_device, DocType


class MappingTest(unittest.TestCase):
	def test_force_wap(self):
		response = map_device("http://m.olx.com.ar/force/wap")
		dt = DocType(response.text)
		self.assertTrue(dt.is_wap(), "Should be WAP:" + dt.doctype())

	def test_force_html4(self):
		response = map_device("http://m.olx.com.ar/force/html4")
		dt = DocType(response.text)
		self.assertTrue(dt.is_html4(), "Should be HTML4:" + dt.doctype())

	def test_force_html5(self):
		response = map_device("http://m.olx.com.ar/force/html5")
		dt = DocType(response.text)
		self.assertTrue(dt.is_html5(), "Should be HTML5:" + dt.doctype())
