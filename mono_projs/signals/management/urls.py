from django.urls import path
from management import views

urlpatterns = [

    path('background_process_notification', views.background_process_notification_api.as_view(), name='background_process_notification')

]