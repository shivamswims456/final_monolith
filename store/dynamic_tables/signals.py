from copy import deepcopy
from collections import defaultdict
from django.db.migrations.recorder import MigrationRecorder
from django.conf import settings
from django.core.management import call_command
from django.db import connection


def replicated_slaves(*args, **kwargs):
    
    from dynamic_tables.models import dynamic_tables    
    
    
    for each in kwargs["plan"]:
        
        #replacements_copies = {proto:set(replacements)}
        replacements_copies = defaultdict(set)

        latest_migration = MigrationRecorder.Migration.objects.order_by('-applied')[0]
            
        for ops in each[0].operations:
            #iterating through operations of a single migration

            proto = getattr(ops, "model_name", False)
            dynatabs = dynamic_tables.objects.filter(proto_name=proto)
            replacements = set([_dt.table_name for _dt in dynatabs])
            replacements_copies[f'{latest_migration.app}_{proto}'] = replacements_copies[f'{latest_migration.app}_{proto}'].union(replacements)


        if len(dynatabs) > 0:
            
            sql = call_command('sqlmigrate', latest_migration.app, latest_migration.name,  '--database', 'default')
            #sql = migration in raw sql

            replicas = ['default'] + settings.REPLICATED_DATABASE_SLAVES
            
            for replica in replicas:
                    
                with connection[replica].cursor() as cursor:

                    for to_replaced, replacement_List in replacements_copies.items():
                        #to_replaced  {latest_migration.app}_{proto} combination
                        #replacement_List slave instances to be migrated

                        for replacement in replacement_List:

                            rsql = sql.replace(to_replaced, f'{latest_migration.app}_{replacement}')
                            #rsql = replaced sql   
                            for statement in [_ for _ in rsql.split(";") if not _.startswith("--") and ";" in _]:
                                #rsql.split(";") splitting statements
                                #_.startswith("--") check not comment
                                #";" in _ empty statement protection
                                cursor.execute(statement)
                                
