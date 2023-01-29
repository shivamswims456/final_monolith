from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from sdks.ecom.utility import fetch_pincodes
from sdks.django.utility import check_claimed_group
from ECOM_users.models import ECOM_super_vendors
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
# Create your views here.



class add_pincodes(LoginRequiredMixin, View):

    def get(self, request, vendor):

        if check_claimed_group(request=request, user=vendor, group="ecom_super_vendor"):

            um = get_user_model()
            uo = um.objects.filter(username=request.user.username)

            if uo.exists():

                django_ecom_obj = ECOM_super_vendors.objects.filter(user=uo[0])

                if django_ecom_obj.exists():
                    
                    django_ecom_obj = django_ecom_obj[0]
                    
                    print(fetch_pincodes(django_ecom_obj=django_ecom_obj, log_obj={}))
    
        

        return JsonResponse({"goAhead":True})

