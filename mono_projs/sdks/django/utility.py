from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 



class django_csrf_exempt(object):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):

        return super(django_csrf_exempt, self).dispatch(*args, **kwargs)



async def websocket_connection_barrier(obj):

    allowed = False
    
    if obj.scope["user"].username != "":
        
        allowed = True
        await obj.accept()

    else:

        await obj.close()

    obj.allowed = allowed
    return allowed




def check_claimed_group(request, user, group):

    result = False
    
    if request.user.username == user and group in [_.name for _ in request.user.groups.all()]:

        result = True

    return result