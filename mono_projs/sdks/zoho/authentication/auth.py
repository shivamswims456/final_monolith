""" 
    module for logging in zoho account through customer proxy 

"""


import requests


SESSION = requests.Session()





def login(django_zoho_obj, zoho_log_obj)->None:

    