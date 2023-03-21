from .models import dynamic_tables
from uuid import uuid4
from django.db import models
from django.db import connection
from django.db import connections
from django.db.utils import DEFAULT_DB_ALIAS, load_backend






def create_connection(alias=DEFAULT_DB_ALIAS):
    #https://stackoverflow.com/a/56733500/15078316
    db = connections.databases[alias]
    backend = load_backend(db['ENGINE'])
    return backend.DatabaseWrapper(db, alias)


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
                
                for alias in connections.databases.keys():
                    
                    schema_editor.connection = create_connection(alias=alias)
                    
                    in_atomic_block = schema_editor.connection.in_atomic_block
                    
                    schema_editor.connection.in_atomic_block = False
                    try:
                        schema_editor.create_model(model)
                    finally:
                        schema_editor.connection.in_atomic_block = in_atomic_block

                    #https://stackoverflow.com/a/69415221/15078316            

                    schema_editor.connection.close()
                    
        return model
    

class loggedMM(multiModel):

    def __init__(self, model_name, prototype, app_name, table_name = None, connection=connection) -> None:
        
        self.table_name = table_name
        
        if self.table_name == None:
        
            self.table_name =  str(uuid4()).replace("-", "_")
        
        super().__init__(model_name, self.table_name, prototype, app_name, connection)

    
    def get(self):

        result = super().get()
        dynamic_tables(table_name=self.table_name, proto_name=self.prototype.__name__).save()
        return result

    def remove(self):

        result = super().remove()
        dynamic_tables.objects.filter(table_name=self.table_name, proto_name=self.prototype.__name__).delete()
        return result
    


