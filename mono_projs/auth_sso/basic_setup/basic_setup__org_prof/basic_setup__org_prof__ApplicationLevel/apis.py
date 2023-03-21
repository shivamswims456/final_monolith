from django.apps import apps
from .serialize import get_org_user_parser
org_models = apps.get_model('basic_setup__org_prof', 'org_model')
org_users = apps.get_model('basic_setup__org_prof', 'org_users')


def return_org_users(org_id):

    org_model = org_models.objects.get(org_id = org_id) 
    relation_query = org_users.objects.filter(org = org_model)

    return get_org_user_parser(instance=relation_query, many=True).data 