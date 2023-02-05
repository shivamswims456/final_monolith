import requests, json, xmltodict
import logging






def __get_necessary__(kwargs, req_params):

        
    assert all([each in kwargs for each in req_params]), "parameter missing"







def add_creds(django_ecom_obj, data, log_obj) -> dict:
    """
        utiltity function for adding username and password
        @data:data obj to which username password has to be added
        @log_obj: log to which data has to be added


    """
    data.update({"username":django_ecom_obj.ecom_user, "password":django_ecom_obj.ecom_password})

    return data




def awb_cancel(django_ecom_obj, log_obj, **kwargs) -> dict:

    """
        fucntion for awb cancelation
        @awb: awb  number for cancellation

    """

    url = "https://api.ecomexpress.in/apiv2/cancel_awb/"

    data = add_creds(kwargs)

    resp = requests.post(url, data=data)

    if resp.status_code == 200:

        result = {"goAhead":True, "data":resp.json()}

    else:

        result = {"goAhead":False, "data":resp.content}


    return result





    



def ndr_resolution(django_ecom_obj, log_obj, **kwargs) -> dict:


    """
    function for ndr_resolution
    @awb: awb number of ndr
    @comments: comment
    @scheduled_delivery_date: date
    @scheduled_delivery_slot: number
    @instruction: RAD/RTO

    #result data
    """

    url  = "https://api.ecomexpress.in/apiv2/ndr_resolutions/"
    data = add_creds(django_ecom_obj=django_ecom_obj, data={"json_input":json.dumps([kwargs])}, log_obj=log_obj) 

    resp = requests.post(url, data=data)

    if resp.status_code == 200:

        result = {"goAhead":True, "data":resp.json()}

    else:

        result = {"goAhead":False, "data":resp.content}


    return result





def track_order(django_ecom_obj, log_obj, **kwargs) -> dict:

    """
    function for tracking order
    @awb: awb number of package to track  
    #result dict
    """
    
    url = "https://clbeta.ecomexpress.in/track_me/api/mawbd/"

    data = add_creds(django_ecom_obj=django_ecom_obj, data=kwargs, log_obj=log_obj)

    
    resp = requests.post(url, data)

    if resp.status_code == 200:

        result = {"goAhead":True, "data":xmltodict.parse(resp.content)} 

    else:

        result = {"goAhead":False, "data":resp.content}



    return result






def manifest_reverse(django_ecom_obj, log_obj, **kwargs) -> dict:

    """
    reverse manifest api
    @params ["awb_number","order_number","product","consignee","consignee_address1","consignee_address2",
            "consignee_address3","destination_city","pincode","state","mobile","telephone","item_description",
            "pieces","collectable_value","declared_value","actual_weight","volumetric_weight","length","breadth",
            "height","pickup_name","pickup_address_line1","pickup_address_line2","pickup_pincode","pickup_phone",
            "pickup_mobile","return_name","return_address_line1","return_address_line2","return_pincode","return_phone",
            "return_mobile","dg_shipment"]
    
    #result dict
    """

    url = "https://api.ecomexpress.in/apiv2/manifest_awb_rev_v2/"

    __get_necessary__(["awb_number","order_number","product","consignee","consignee_address1","consignee_address2",
                        "consignee_address3","destination_city","pincode","state","mobile","telephone","item_description",
                        "pieces","collectable_value","declared_value","actual_weight","volumetric_weight","length","breadth",
                        "height","pickup_name","pickup_address_line1","pickup_address_line2","pickup_pincode","pickup_phone",
                        "pickup_mobile","return_name","return_address_line1","return_address_line2","return_pincode","return_phone",
                        "return_mobile","dg_shipment"])


    kwargs = {key.upper(): value for key, value in kwargs.items()}
    

    json_data = {'json_input': json.dumps({"ECOMEXPRESS-OBJECTS": {"SHIPMENT": kwargs}})}


    resp = requests.post(url, kwargs)

    if resp.status_code == 200:

        result = {"goAhead":True, "data":resp.json()}

    else:

        result = {"goAhead":False, "data":resp.content}

    
    return result



def manifest_forward(django_ecom_obj, log_obj, **kwargs)->dict:

    """
    forwad manifest api
    @params ["awb_number","order_number","product","consignee","consignee_address1",
            "consignee_address2","consignee_address3","destination_city","pincode",
            "state","mobile","telephone","item_description","pieces","collectable_value",
            "declared_value","actual_weight","volumetric_weight","length","breadth","height",
            "pickup_name","pickup_address_line1","pickup_address_line2","pickup_pincode",
            "pickup_phone","pickup_mobile","return_name","return_address_line1","return_address_line2",
            "return_pincode","return_phone","return_mobile","dg_shipment"]

    #data
    """

    url = "https://api.ecomexpress.in/apiv2/manifest_awb/"

    __get_necessary__(["awb_number","order_number","product","consignee","consignee_address1",
                       "consignee_address2","consignee_address3","destination_city","pincode",
                       "state","mobile","telephone","item_description","pieces","collectable_value",
                       "declared_value","actual_weight","volumetric_weight","length","breadth","height",
                       "pickup_name","pickup_address_line1","pickup_address_line2","pickup_pincode",
                       "pickup_phone","pickup_mobile","return_name","return_address_line1","return_address_line2",
                       "return_pincode","return_phone","return_mobile","dg_shipment"])


    kwargs = {key.upper(): value for key, value in kwargs.items()}


    json_data = {'json_input':json.dumps([kwargs])}

    
    resp = requests.post(url, data=add_creds(django_ecom_obj=django_ecom_obj, data=json_data, log_obj=log_obj))


    if resp.status_code == 200:

        result = {"goAhead":True, "data":resp.json()}

    else:

        result = {"gpAhead":False, "data":resp.content}


    return result    







def generate_awb(django_ecom_obj, log_obj, **kwargs) -> dict:

    """
        for generating awb numbers
        parameters required
        @count: number of awbs to generated < 20000
        @type: type of awbs to be generated[PPD / COD /REV] 
    
        #data:returns list of awbs fetched
    """


    __get_necessary__(["count", "type"])


    url = "https://api.ecomexpress.in/apiv2/fetch_awb/"

    data = add_creds(django_ecom_obj=django_ecom_obj, data=kwargs, log_obj=log_obj)
    resp = requests.post(url, data)

    if resp.status_code == 200:

        result = {"goAhead":True, "data":resp.json()}

    else:

        result = {"goAhead":False, "data":resp.content}


    return result




def fetch_pincodes(django_ecom_obj, log_obj) -> dict:

    """
        for fetching pincode of ecom services
        @django_ecom_obj: django end username password
        @log_obj: for logging 

        #data: returns obj of pincodes
        [{"status": 1, "city_type": "", "pincode": 134007, "active": true, "state_code": "HR",
         "city": "AMBALA", "dccode": "ABA", "route": "PB/PTH/ABA",
          "state": "Haryana", "date_of_discontinuance": "", "city_code": "ABA"}, ...]
    """

    try:
        
        url = "https://api.ecomexpress.in/apiv2/pincodes/"

        auth_data = add_creds(django_ecom_obj=django_ecom_obj, data={}, log_obj=log_obj)

        
        resp = requests.post(url, auth_data)

        if resp.status_code == 200:

            result = {"goAhead":True, "data":resp.json()}


        else:

            result = {"goAhead":False, "data":resp.content}
        

    except Exception as e:

        log_obj.exception(f"ECOM API fetch Error \n {e}", exc_info=True)

    
    return result




