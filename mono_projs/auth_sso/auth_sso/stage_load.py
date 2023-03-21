from django.conf import settings
from n_app_factory.actions import load_package

stages = {"DEV":{"package":['basic_setup'],
                 "exclude_nested":[],
                 "models_denied":{}} 
         }


conf = stages[settings.CICD_STAGE]

#print(load_package(conf["package"], conf["exclude_nested"]))
url_packages, apps_to_be_loaded, app_names = load_package(conf["package"], conf["exclude_nested"])
settings.MODELS_DENIED.update(conf["models_denied"])
settings.INSTALLED_APPS += apps_to_be_loaded
settings.APP_NAMES += app_names
