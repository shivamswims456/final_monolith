from django.urls import path, include
from basic_setup.basic_setup__org_prof.basic_setup__org_prof__ApplicationLevel.views import goodMan
app_name = "basic_setup__org_prof__ApplicationLevel"
base_path = "basic_setup/org_prof/ApplicationLevel/"


urlpatterns = [

    path('goodMan', goodMan.as_view(), name='goodMan')
]
#please add only path locations as they are only supported by package
       