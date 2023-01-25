from django.urls import path
from valuate import views


urlpatterns = [

    path("valuate", views.demo.as_view(), name='demo')
    
]
