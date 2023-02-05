from django.contrib.auth import get_user_model
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.conf import settings

from sdks.ecom.utility import fetch_pincodes
from sdks.django.utility import async_cbv, mono_sync_to_async
from sdks.django.utility import check_claimed_group
from sdks.signals.signals import send_bpn_signal

from ECOM_users.models import ECOM_super_vendors
from ECOM_pincodes.helpers import insert_ecom_pincdes_from_web_to_database as pin_web_database

from asgiref.sync import sync_to_async

import asyncio
import logging, time 
# Create your views here.


db_logger = logging.getLogger('db')








def __add_pincode_sync_logic__(request, vendor):

    try:

        
        if med_group(request=request, user=vendor, group="ecom_super_vendor"):
            um = get_user_model()
            uo = um.objects.filter(username=request.user.username)

            if uo.exists():
                
                django_ecom_obj = ECOM_super_vendors.objects.filter(user=uo[0])

                if django_ecom_obj.exists():
                    
                    result = django_ecom_obj[0]
                    #monkey patching 
                    #https://stackoverflow.com/a/64813978/15078316
                    str(result)
                    
    except Exception as e:

        print(e)

    

    return result






class add_pincodes(async_cbv, View):            


    async def get(self, request, vendor):

        uv = sync_to_async(__add_pincode_sync_logic__, thread_sensitive=False)
        uv = await uv(request=request, vendor=vendor)
        
        print(uv)        
        if uv:

            loop = asyncio.get_event_loop()
            add_pincodes_web_db = sync_to_async(pin_web_database, thread_sensitive=False)
            add_pincodes_web_db_task = await loop.create_task(add_pincodes_web_db(vendor))
            
            try:

                add_pincodes_web_db_result = add_pincodes_web_db_task.result()
                #user level message has been passed from function 


                if add_pincodes_web_db_result["goAhead"]:
                    
                    send_bpn_signal_async = loop.create_task(send_bpn_signal)
                    send_bpn_signal_async_result = send_bpn_signal_async(key=settings.NOTIFICATION_KEY, user=vendor, message=add_pincodes_web_db_result)

                    try:

                        send_bpn_signal_async_result.result()

                    except Exception as e:

                        db_logger.error(f'ECOM bpn signal failed for {vendor} \n {e}', exc_info=True)



            except Exception as e:
                
                db_logger.exception(f'ECOM pincode addition failed for {vendor} \n {e}', exc_info=True)
                



            
        return JsonResponse({"goAhead":True, "message":"Task scheduled"}) 


"""



class add_pincodes(LoginRequiredMixin, View):

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view



    async def get(self, request, vendor):

        #add_pincode_async_logic = add_pincode_sync_logic(request=request, vendor=vendor)


        
        if user_verified is not False:

            #print(fetch_pincodes(django_ecom_obj=django_ecom_obj, log_obj={}))
            loop = asyncio.get_event_loop()
            async_function = sync_to_async(wait, thread_sensitive=False)
            loop.create_task(async_function)


        return HttpResponse("Non-blocking HTTP request (via sync_to_async)")

 """