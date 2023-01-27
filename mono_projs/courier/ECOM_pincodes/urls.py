from django.urls import path
from ECOM_pincodes import views

urlpatterns = [

    path('add', views.add_pincodes.as_view(), name='ecom_add_pincodes')

]