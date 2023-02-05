import asyncio, logging
from asgiref.sync import sync_to_async
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 
from django.utils.decorators import classonlymethod
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponse
from django.db import models
from django.db.transaction import non_atomic_requests
import json
from copy import deepcopy

###################################################################
#                   bulkImport  helpers start                     #
###################################################################



def bimport_status_skip_insert(dummy_model, model, connection,  search_key, logger):
    
    """
        @dummy_model: (django_ecom_pincode_model) model where temporary data will be stored
        @model: (django_ecom_pincode_model) final model in which data has to be trasferred
        @connection: (django.db connection)
        @search_key: (str) field on which operation @method has to be perfoemed 
        @logger: logger
    """

    #TO_DO: add 0 entry filter

    dummy_db_name = dummy_model._meta.db_table
    model_db_name = model._meta.db_table

    insert_field_list = str(tuple(field.name for field in model._meta.fields if not field.primary_key)).replace("'", "")

    try:
        
        with connection.cursor() as cursor:

            cursor.execute(f'''insert into {model_db_name} {insert_field_list}
                               select {insert_field_list.replace("(", "").replace(")", "")}
                                    from {dummy_db_name} where {search_key} not in
                               (select {search_key} from {model_db_name});''');
        

            result = {"goAhead":True}
                

    except Exception as e:

        logger.exception(f"fake import for bulk date in model {model_db_name} failed", exc_info=True)

        result = {"goAhead":False}


    return result


def bimport_status_common_summary(dummy_model, model, connection, search_key, logger):
    
    """
        @dummy_model: (django_ecom_pincode_model) model where temporary data will be stored
        @model: (django_ecom_pincode_model) final model in which data has to be trasferred
        @connection: (django.db connection)
        @search_key: (str) field on which operation @method has to be perfoemed 
        @logger: logger
    """

    dummy_db_name = dummy_model._meta.db_table
    model_db_name = model._meta.db_table

    try:
        

        with connection.cursor() as cursor:
        
            cursor.execute(f'select id, {search_key} from {dummy_db_name} where {search_key} not in (select {search_key} from {model_db_name});')
            result = {"goAhead":True, "data":([each for each in cursor.fetchall()])}
            

    except Exception as e:

        logger.execption(f"fake import for bulk date in model {model_db_name} failed", exc_info=True)

        result = {"goAhead":False}


    return result



def bimport_status_action(dummy_model, model, entries, connection, cols, logger):
    
    """
        @dummy_model: (django_ecom_pincode_model) model where temporary data will be stored
        @model: (django_ecom_pincode_model) final model in which data has to be trasferred
        @entries: (dict) entries that are to be inserted
        @connection: (django.db connection)
        @cols: (tuple) cols in which order values has to be inserted
        @logger: logger
    """
    dummy_db_name = dummy_model._meta.db_table
    model_db_name = model._meta.db_table

    try:
        

        with connection.cursor() as cursor:
        
            cursor.execute(f"truncate table {dummy_db_name}") 
            cols = str(tuple(cols)).replace("'", "")
            cursor.execute(f"insert into {dummy_db_name} {cols} values {entries}")
            result = {"goAhead":True}
            

    except Exception as e:
        
        logger.execption(f"fake import for bulk date in model {model_db_name} failed", exc_info=True)

        result = {"goAhead":False}


    return result



def prepare_data_for_bulk_import(entries, model, entry_manipultation={}, values=False, logger=None):

    """
        @entries: (list) raw entries that are to be pushed in model
        @model: (django_model) model in consideration
        @entry_manipultation: (dict) mappings model.fields and model.values
        @values: (bool) trigger for raw values
        @logger: logger
        for each field of model a coinsideing manipulation must be passed
        for proper function
    """

    try:

        bulk_entries = [] if not values else ''

        errors = {}

        
        for index, entry in enumerate(entries):

            mapped_data = {}

            for model_field, manipulation in entry_manipultation.items():
                    
                if isinstance(manipulation, str):
                    
                    mapped_data[model_field] = entry[manipulation]

                elif callable(manipulation):

                    mapped_data[model_field] = manipulation(entry)


            m_entry = model(**mapped_data)

            try:

                m_entry.full_clean()

                if values:
                    
                    

                    bulk_entries += f'''({json.dumps(list(mapped_data.values()))[1:-1] + ","
                                    if len(mapped_data.values()) == 1
                                    else json.dumps(list(mapped_data.values()))[1:-1]}), '''


            except Exception as e:

                errors[index] = __bimport_systemError_to_userError__(e.error_dict)



        if values:

            bulk_entries = f"{bulk_entries[:-2]};"


        result = {"goAhead":True, "data":{"entries":bulk_entries, "errors":errors}}
                


    except Exception as e:

        logger.exception(f'data prep for bulk import failed model:{model._meta.db_table} \n {e}', exc_info=True)

        result = {"goAhead":False, "errors":e}

    return result



def __bimport_systemError_to_userError__(error_dict):

    errors = {}

    for key, value in error_dict.items():

        errors[key] = value[0].message

    return errors


###################################################################
#                   bulkImport  helpers stop                      #
###################################################################


#------------------------------------------------------------------#








###################################################################
#                   multiTableModelCreate start                   #
###################################################################




class multiModel(object):

    def __init__(self, model_name, table_name, prototype, app_name, connection) -> None:
        """
            @model_name: name of the new table object
            @table_name: name of the table with which it has to
                         be created in database
            @prototype: model which has to be used as prototype for
                        creating new table 
            @app_name: app for which table has to be created
            @connection: connection to be used

        """

        self.model_name = model_name
        self.table_name = table_name
        self.prototype = prototype
        self.app_name = app_name
        self.connection = connection
        self.name_table_db = f"{self.app_name}_{self.table_name}"

    

    def remove(self):

        if self.__exists__():

            with self.connection.cursor() as cursor:

                cursor.execute(f"drop table {self.name_table_db};")
        

        return 1


    def get(self):

        """
            creates model if it does not exists else return the model  
        """

        return self.__create_model__(create = not self.__exists__())


    def __exists__(self):

        with self.connection.cursor() as cursor:

            cursor.execute("show tables;")
            tables = [each[0] for each in cursor.fetchall()]
        result = False

        if self.name_table_db.lower() in tables:
            
            result = True

        return result


    def __create_model__(self, create = True):


        class Meta:
            pass

        setattr(Meta, "db_table", self.name_table_db)
        fields = {}

        for field in self.prototype._meta.fields:

            fields[field.name] = field.clone()

        attrs = {'__module__':f"{self.app_name}.models", "Meta":Meta}
        self.attrs = attrs
        attrs.update(fields)


        model = type(self.model_name, (models.Model,), attrs)

        
        if create:

        
            with self.connection.schema_editor() as schema_editor:
                in_atomic_block = schema_editor.connection.in_atomic_block
                schema_editor.connection.in_atomic_block = False
                try:
                    schema_editor.create_model(model)
                finally:
                    schema_editor.connection.in_atomic_block = in_atomic_block

                #https://stackoverflow.com/a/69415221/15078316            
                
        return model
    



###################################################################
#                   multiTableModelCreate end                   #
###################################################################





###################################################################
#                   Async Decorators start                        #
###################################################################

def async_return_login(view_function):

    async def check_login(cls, request, *args, **kwargs):

        response = redirect_to_login(request.get_full_path())

        if await sync_to_async(lambda: request.user.is_authenticated)():

            response = await view_function(cls, request, *args, **kwargs)

        return response
    
    return check_login

def async_check_required_permissions(view_function):

    def __permission_all__(required_perms, user_perms):
        
        result = True
        
        for perm in required_perms:
            
            if perm not in user_perms:
            
                result = False

                break



        return result
    
    
    def __permission_any__(required_perms, user_perms):

        result = False

        for perm in required_perms:

            if perm in user_perms:

                result = True

                break

        return result


            

    conversion_function = {"all":__permission_all__,
                           "any":__permission_any__}
    


    async def check_permissions(cls, request, *args, **kwargs):
        
        response = HttpResponse('Insuffcient Permission', status=401)

        user_perms = await sync_to_async(request.user.get_all_permissions)()


        
        for perm_class, perm_list in cls.permissions.items():
            
            perm_run = conversion_function.get(perm_class, False)
            
            if perm_run:

        
                if perm_run(required_perms=perm_list, user_perms=user_perms):
                    
                    response = await view_function(cls, request, *args, **kwargs)


            else:

                raise TypeError(f"{perm_class} type is not defined")

        
        

        return response
    

    return check_permissions



###################################################################
#                   Async Decorators end                          #
###################################################################




#------------------------------------------------------------------#

###################################################################
#                   Async ViewMixins start                        #
###################################################################

class async_cbv(object):


    @classonlymethod
    def as_view(cls, **initkwargs):
        
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view




###################################################################
#                   Async ViewMixins end                          #
###################################################################


#------------------------------------------------------------------#



###################################################################
#                   ViewMixins start                              #
###################################################################


class django_csrf_exempt(object):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):

        return super(django_csrf_exempt, self).dispatch(*args, **kwargs)


###################################################################
#                   ViewMixins end                               #
###################################################################








#------------------------------------------------------------------#



###################################################################
#                   websocketMixins start                         #
###################################################################



async def websocket_connection_barrier(obj):

    allowed = False
    
    if obj.scope["user"].username != "":
        
        allowed = True
        await obj.accept()

    else:

        await obj.close()

    obj.allowed = allowed
    return allowed



###################################################################
#                   websocketMixins start                         #
###################################################################

