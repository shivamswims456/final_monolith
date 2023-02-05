from sdks.ecom import utility
from sdks.django import utility as d_uty
from ECOM_pincodes.errors import ERRORS
from ECOM_pincodes.user_messages import MESSAGES
from ECOM_pincodes.models import ECOM_pincodes
from django.db import connection
import logging
from ECOM_pincodes.apps import EcomPincodesConfig



db_logger = logging.getLogger('db')







def vendors_pincode_table(user_name, fake=False):
    """
        @user_name: (str) user for which table has to be made
        @fake: (bool) return fake table

    """
    try:
        
        table_name = f"vendor_version_{user_name}" if not fake else f"vendor_version_{user_name}_fake"

        mm = d_uty.multiModel(model_name="super_vendor_pincode", table_name=table_name,
                              prototype=ECOM_pincodes, app_name=EcomPincodesConfig.name,
                              connection=connection)

        db_logger.debug("create vendor version of Ecom_pincodes table for vendor {user_name}")

        
    except Exception as e:

        db_logger.exception("unable to create vendor version of Ecom_pincodes table for vendor {user_name} \n\
                            {e}", exc_info = True)

    return mm


def generate_bimport_summary( django_ecom_obj ):

    dummy_model = vendors_pincode_table(user_name=django_ecom_obj.user.username, fake=True).get()
    model = vendors_pincode_table(user_name=django_ecom_obj.user.username, fake=False).get()
    result = d_uty.bimport_status_common_summary(dummy_model=dummy_model, model=model,
                                               connection=connection, search_key='item_unique',
                                                logger=db_logger)

    if not result["goAhead"]:

        result = {"goAhead":False, "error":ERRORS["SUMMARY_UNAVAIALBLE"]}


    return result
        


def insert_bimport_skip( django_ecom_obj ):


    dummy_model = vendors_pincode_table(user_name=django_ecom_obj.user.username, fake=True).get()
    model = vendors_pincode_table(user_name=django_ecom_obj.user.username, fake=False).get()
    result = d_uty.bimport_status_skip_insert(dummy_model=dummy_model, model=model,
                                              connection=connection,
                                              search_key='item_unique',
                                              logger=db_logger)

    if not result["goAhead"]:

        result = {"goAhead":False, "error":ERRORS["SUMMARY_UNAVAIALBLE"]}


    return result
        


def insert_ecom_pincodes_from_web_to_database( django_ecom_obj ):

    """
        @super_vendor:str = vendor for which entries are being s\tored 
        @method:str = skip/overwrite
    """

    try:

        db_logger.debug(f"Fetching pincodes for {django_ecom_obj.user.username}")
        #response = utility.fetch_pincodes(django_ecom_obj=django_ecom_obj, log_obj=db_logger)

        response = {"goAhead": True, "data": [{"status": 1, "city_type": "", "pincode": 134007, "active": True,
                                              "state_code": "HR",
                                              "city": "AMBALA", "dccode": "ABA", "route": "PB/PTH/ABA",
                                              "state": "Haryana", "date_of_discontinuance": "", "city_code": "ABA"},
                                              {"status": 1, "city_type": "", "pincode": 134009, "active": True,
                                              "state_code": "HR",
                                              "city": "AMBALA", "dccode": "ABA", "route": "PB/PTH/ABA",
                                              "state": "Haryana", "date_of_discontinuance": "", "city_code": "ABA"},
                                              {"status": 1, "city_type": "", "pincode": 134004, "active": True,
                                              "state_code": "HR",
                                              "city": "AMBALA", "dccode": "ABA", "route": "PB/PTH/ABA",
                                              "state": "Haryana", "date_of_discontinuance": "", "city_code": "ABA"},
                                              {"status": 1, "city_type": "", "pincode": 134003, "active": True, "state_code": "HR", "city": "AMBALA",
                                              "dccode": "ABA", "route": "PB/PTH/ABA", "state": "Haryana", "date_of_discontinuance": "",
                                              "city_code": "ABA"},
                                              {"status": 1, "city_type": "", "pincode": 134002, "active": True, "state_code": "HR", "city": "AMBALA", "dccode": "ABA", "route": "PB/PTH/ABA", "state": "Haryana", "date_of_discontinuance": "", "city_code": "ABA"}]}
        

        if response["goAhead"]:

            manipulations = {'item_unique':lambda entry:f"{entry['pincode']}_{entry['state_code']}_{entry['city_code']}",
                              'status': 'status',
                              'city_type': lambda entry:None if entry['city_type'] == "" else entry['city_type'],
                              'pincode': 'pincode',
                              'active': 'active',
                              'state_code': 'state_code',
                              'city': 'city',
                              'dccode': 'dccode',
                              'route': 'route',
                              'state': 'state',
                              'date_of_discontinuance': lambda entry:None if entry['date_of_discontinuance'] == "" else entry['date_of_discontinuance'],
                              'city_code': 'city_code'}    
            
            
            dummy_model = vendors_pincode_table(user_name=django_ecom_obj.user.username, fake=True).get()
            model = vendors_pincode_table(user_name=django_ecom_obj.user.username, fake=False).get()

            entries = d_uty.prepare_data_for_bulk_import(entries=response["data"],
                                                         model=ECOM_pincodes,
                                                         entry_manipultation=manipulations,
                                                         values=True,
                                                         logger = db_logger)



            if entries["goAhead"]:

                entries = entries["data"]

                result = d_uty.bimport_status_action(dummy_model=dummy_model,
                                            model=model,
                                            entries=entries["entries"],
                                            connection=connection,
                                            cols = tuple(manipulations.keys()),
                                            logger = db_logger)


            

    except Exception as e:

        result = {"goAhead":False}

        db_logger.exception(f"Error while fetching pincodes for {django_ecom_obj.user.username}")

    return result

