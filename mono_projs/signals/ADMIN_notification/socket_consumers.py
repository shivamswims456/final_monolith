import json
from asgiref.sync import sync_to_async
from ADMIN_notification.models import individual_layer_stack as ils 
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from sdks.django.utility import websocket_connection_barrier
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
#channels = users

um = get_user_model()


class background_process_notification(AsyncJsonWebsocketConsumer):

    def save_group(self):
        

        self_group = str(self.scope['user'].username) #1234567890 = "1234567890"
        ils(user = self.scope['user'], channel_group = self_group).save()



    async def connect(self):

        allowed = await websocket_connection_barrier(self)
          
        if allowed:

            
            await database_sync_to_async(self.save_group)() 
            #user_instance, user_private_group = username
            await self.channel_layer.group_add(str(self.scope['user'].username), self.channel_name)
        



    async def send_signal(self, event):
        
        await self.send_json({
            "event": event
        })


        

    async def receive_json(self, content, **kwargs):

        del content["key"]         
        
        await self.channel_layer.group_send(content.get("user"), {
                    "type": "send_signal",
                    "data":content
                })





    async def disconnect(self, code):


        if self.allowed:
        
            await self.channel_layer.group_discard(str(self.scope["user"].username), self.channel_name)

