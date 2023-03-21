from django_sso.sso_gateway.models import Service
from django.http import HttpResponseForbidden, HttpResponseNotAllowed
import json

class nameBasedBlocking:

    def __init__(self, get_response):
        
        self.get_response = get_response

    def __call__(self, request, *args, **kwds):

        return self.get_response(request)


    def process_view(self, request, view_func, view_args, view_kwargs):
        
        host = request.get_host()
        port_split = host.split(":")
        #first subdomain is considered
        service_search_param = port_split[-1] if len(port_split) > 0 else host.split(".")[0]
        


        if "ApplicationLevel" in request.path:

            if request.method in ["POST", "PUT"]:

                try:
                    
                    json_request = json.loads(request.body)

                except:

                    return HttpResponseForbidden('{"error":"bad token"}')
                
                token_served = json_request.get("token") if request.method == "POST" else json_request.get("token")

                additional_service = Service.objects.filter(base_url__contains = service_search_param)

                if len(additional_service) > 1 or len(additional_service) == 0:

                    raise ProcessLookupError('Service Registration error')
                

                service_token = additional_service[0].token
        
                if service_token != token_served:
                    
                    return HttpResponseForbidden('{"error":"bad token"}')


            else:

                return HttpResponseNotAllowed(["POST", "PUT", "PATCH"],'{"error":"Method not allowed"}')

        request.csrf_processing_done = True

        return None