from django.urls import path
from ECOM_pincodes import views

urlpatterns = [

    path('add/skip', views.add_pincodes_skip.as_view(), name='ecom_add_pincodes_skip'),
    path('add/skip/summary', views.add_pincodes_skip_summary.as_view(), name='ecom_add_pincodes_summary_skip'),
    path('add/skip/insert', views.add_pincodes_skip_insert.as_view(), name='ecom_add_pincodes_insert_skip'),

]