To validate whether your site is serving the correct WAP/HTML4/HTML5:

- Create a file user-agents.csv with the mapping between User Agent and languaje
- change URL_MOBILE in device_map.py
- run test: nosetests device_map.py:test_UAs
