##adminUser
admin sethu@gmail.com
Frooti@30   

##Packages
django_sso package should be loaded from monolith

##starting a new project

#paste in root **init** file

```
import pymysql, sys
pymysql.install_as_MySQLdb()


#to get connection sdks internally if needed
from pathlib import Path
SUPER_BASE = str(Path(__file__).resolve().parent.parent.parent)
sys.path.append(SUPER_BASE)



#to get dynamic db support for slave replication
from dynamic_tables import init_patch

```

#Add to apps.py signals for dynamic db auto migration

```
from django.db.models.signals import post_migrate
from dynamic_tables.signals import replicated_slaves


class AppConfig(AppConfig):

    #AppConfig class
    def ready(self):

        post_migrate.connect(replicated_slaves, sender=self)


```

#add to settings.py

```
import os, json
SUPER_BASE = Path(__file__).resolve().parent.parent.parent




with open(os.path.join(SUPER_BASE, 'conf', 'servers', 'server.json'), 'r') as f:

    SERVER = json.load(f)




LOGIN_URL = SERVER['auth_sso_login_url']
SSO_ROOT = SERVER['auth_sso_server_address']
SSO_TOKEN = 'to be obtained from sso server'
SESSION_COOKIE_NAME = 'courier'

NOTIFICATION_KEY = 'to be obtained from signal server'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'db_log': {
            'level': 'DEBUG',
            'class': 'django_db_logger.db_log_handler.DatabaseLogHandler'
        },
    },
    'loggers': {
        'db': {
            'handlers': ['db_log'],
            'level': 'DEBUG'
        },
        'django.request': { # logging 500 errors to database
            'handlers': ['db_log'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}




```

#addition settings where database consistency is priority
#add to settings.py

```

from django_replicated.settings import *
DATABASES {
    'default': {
        # ENGINE, HOST, etc.
    },
    'slave1': {
        # ENGINE, HOST, etc.
    },
    'slave2': {
        # ENGINE, HOST, etc.
    },
}
REPLICATED_DATABASE_SLAVES = ['slave1', 'slave2']
DATABASE_ROUTERS = ['django_replicated.router.ReplicationRouter']
REPLICATED_DATABASE_DOWNTIME = 60

```
