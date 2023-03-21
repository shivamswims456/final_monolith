from rest_framework.parsers import JSONParser
from rest_framework import serializers
from django.apps import apps
from django.contrib.auth import get_user_model
parser = JSONParser()



class _user__get_org_user_parser(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = "__all__"
        
    

class get_org_user_parser(serializers.ModelSerializer):

    users = _user__get_org_user_parser(many=True, read_only=True)

    class Meta:

        fields = "__all__"
        model = apps.get_model('basic_setup__org_prof', 'org_users')




