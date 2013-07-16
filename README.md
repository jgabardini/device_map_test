To validate whether your site is serving the correct WAP/HTML4/HTML5:

- install python 2.7 and viertualenv 
- Create a file user-agents.csv with the mapping between User Agent and languaje
- change URL_MOBILE in device_map.py
- activate the env: 
source venv/bin/activate
- run test: 
nosetests device_map.py:test_UAs

