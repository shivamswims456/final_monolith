from django.shortcuts import render
from django.views import View
from management.models import application_setup
from channels.layers import get_channel_layer
from sdks.django.utility import django_csrf_exempt
from django.http import JsonResponse
from asgiref.sync import async_to_sync
import json
# Create your views here.

channel_layer = get_channel_layer()

class background_process_notification_api(django_csrf_exempt, View ):

    
    def get(self, request):

        return JsonResponse({1:"good"})

    
    def post(self, request):

        result = {"goAhead":False}
        request_body = json.loads(request.body.decode('utf-8'))
        

        if all([ _ in request_body for _ in ['key', 'user', 'message']])\
            and application_setup.objects.filter(application_key=request_body.get('key'),\
                                                 enabled=True).exists():
            
            del request_body["key"]


            async_to_sync(channel_layer.group_send)(request_body.get("user"), {
                    "type": "send_signal",
                    "data":request_body
                })


            result = {"goAhead":True}

        return JsonResponse(result)