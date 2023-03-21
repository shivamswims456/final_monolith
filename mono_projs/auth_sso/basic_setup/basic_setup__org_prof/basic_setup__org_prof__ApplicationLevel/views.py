from django.views import View
from django.http import HttpResponse, JsonResponse
from django.apps import apps

class get_org_user(View):

    """
        intended to return all the org the user is affliated to 
        on post request
    """
    


    def post(self, request):

        


        return HttpResponse('')





class goodMan(View):

    """
        view intended for getting org 
        #statrt here 
    """

    def post(self, request):

        from .apis import return_org_users

        return JsonResponse(return_org_users(2116232369), safe=False)