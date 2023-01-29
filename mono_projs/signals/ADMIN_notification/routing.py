from django.urls import re_path
from ADMIN_notification.socket_consumers import background_process_notification

websocket_urlpatterns = [
    
    re_path(r'signals/notification/$', background_process_notification.as_asgi()),

]