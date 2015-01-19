'''
!define TEST_SYSTEM {slim} 
!define SLIM_VERSION {0.1}
!path /home/kleer/waferslim-1.0.2
!define COMMAND_PATTERN {python -m waferslim.server -v --syspath %p }

!path /home/kleer/curso_fitnesse

|import|
|user_agent|

|lenguaje en response|
|user_agent|lenguaje?|
|Mozilla/5.0 (Windows NT 6.1; Intel Mac OS X 10.6; rv:7.0.1) Gecko/20100101 Firefox/7.0.1| XHTML1|
|UCWEB/2.0(Symbian; U; S60 V3; en-US; NokiaE71) U2/1.0.0 UCBrowser/8.9.0.277 U2/1.0.0 Mobile|HTML4|
'''

import requests
import re

def map_device(url, user_agent):
  header = {
    'User-Agent': user_agent  
  }
  r = requests.get(url=url, headers=header)
  return r


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

  def is_xhtml1(self):
    return -1 < self.doctype().lower().find('xhtml 1.0')

  def is_languaje(self, languaje):
    return  self.is_wap() if languaje == 'WAP' else \
            self.is_html4() if languaje == 'HTML4' else \
            self.is_html5() if languaje == 'HTML5' else \
            self.is_xhtml1() if languaje == 'XHTML1' else \
            False


class LenguajeEnResponse(object):
    def __init__(self):
      self._ua = ""
        
    def set_user_agent(self, ua):
      self._ua = ua
    
    def lenguaje(self):
      response = map_device(url= "http://www.olx.com.ar", user_agent=self._ua)
      dt = DocType(response.text)
      return ("WAP" * dt.is_wap() +
              "HTML4" * dt.is_languaje("HTML4") +
              "HTML5" * dt.is_languaje("HTML5") +
              "XHTML1" * dt.is_languaje("XHTML1")
      )
