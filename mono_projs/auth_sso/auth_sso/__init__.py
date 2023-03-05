"""
Module intended for providing sso for different 
subordinated services via api struncture in non-native apps
and via add-on app in django

Refrences can be found at
https://pypi.org/project/django-sso/1.1.4/

Project has intentionally not moved to the the latest version
as custom field implemented in newer version was hardcoded in
the installed version and new set of energy would be invested to
the same in new version


#TO-DO: Move Monkey Pacthed django-sso to use 2.0 for native 
custom field support


"""


import pymysql
pymysql.install_as_MySQLdb()
from dynamic_tables import init_patch


