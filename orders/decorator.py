from functools import wraps
from django.http import HttpResponseForbidden

def customer_permission_required(func):
    @wraps(func)
    def wrap(request, *args, **kwargs):
        if not request.user.is_customer:
            return HttpResponseForbidden("You don't have permission to view this resource.")
        return func(request, *args, **kwargs)
    return wrap