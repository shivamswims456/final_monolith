import asyncio
from sdks.django.utility import async_cbv, async_return_login, async_check_required_permissions
from ECOM_users.models import ECOM_super_vendors
from ECOM_pincodes.errors import ERRORS as pin_errors
from ECOM_pincodes.user_messages import MESSAGES as pin_messages
from ECOM_pincodes.helpers import insert_ecom_pincodes_from_web_to_database as pin_web_db, generate_bimport_summary, insert_bimport_skip
from asgiref.sync import sync_to_async
from django.views import View
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model
from sdks.django.async_background import create_background_task as cbt

um = get_user_model()


def wait(ecom):

    print(ecom.ecom_password, "wait")

    import time

    for each in range(5):

        print(each)
        time.sleep(1)

    return 1









class add_pincodes_skip_insert(async_cbv, View):

    permissions = {"all":['ECOM_pincodes.ECOM_pincodes_bulk_add']}

    def sync_get(self, request):

        response = HttpResponse('You are not a super vendor', status=401)

        vendor = ECOM_super_vendors.objects.filter(user=um.objects.get(username=request.user.username))

        result = vendor.exists()

        if result:

            result = vendor.first()

            result.__str__()
            
        return result


    @async_return_login    #shadow async version of login_required
    @async_check_required_permissions
    async def get(self, request):

        async_get = await sync_to_async(self.sync_get)(request)

        response = HttpResponse(pin_errors["NO_SUPER_VENDOR"], status = 400)

        if async_get is not False:

            response = JsonResponse(await sync_to_async(insert_bimport_skip)(async_get))


        return response




class add_pincodes_skip_summary(async_cbv, View):

    permissions = {"all":['ECOM_pincodes.ECOM_pincodes_bulk_add']}

    def sync_get(self, request):

        response = HttpResponse('You are not a super vendor', status=401)

        vendor = ECOM_super_vendors.objects.filter(user=um.objects.get(username=request.user.username))

        result = vendor.exists()

        if result:

            result = vendor.first()

            result.__str__()
            
        return result


    @async_return_login    #shadow async version of login_required
    @async_check_required_permissions
    async def get(self, request):

        async_get = await sync_to_async(self.sync_get)(request)

        response = HttpResponse(pin_errors["NO_SUPER_VENDOR"], status = 400)

        if async_get is not False:

            response = JsonResponse(await sync_to_async(generate_bimport_summary)(async_get))


        return response

class add_pincodes_skip(async_cbv, View):


    permissions = {"all":['ECOM_pincodes.ECOM_pincodes_bulk_add']}

    def sync_get(self, request):

        response = HttpResponse('You are not a super vendor', status=401)

        vendor = ECOM_super_vendors.objects.filter(user=um.objects.get(username=request.user.username))

        result = vendor.exists()

        if result:

            result = vendor.first()

            result.__str__()
            
        return result
        
        
        
    @async_return_login    #shadow async version of login_required
    @async_check_required_permissions
    async def get(self, request):

        async_get = await sync_to_async(self.sync_get)(request)

        response = HttpResponse(pin_errors["NO_SUPER_VENDOR"], status = 400)

        if async_get is not False:
                
            asyncio.create_task(cbt(pin_web_db,
                                    lambda*args:print(args[0].result()),
                                    {"django_ecom_obj":async_get})) 
            
            response = HttpResponse(pin_messages["pin_imported_started"])

        return response

