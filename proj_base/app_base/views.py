from django.http import HttpResponse
from django.shortcuts import render
import waffle

# Create your views here.
#  Create your views here.
def index(request):
    from django.conf import settings

    print(settings.CONFIG_LOAD) # custom variable
    if waffle.flag_is_active(request, 'IS_ACTIVE_CUSTOM_MSG'):
        """Behavior if flag is active."""
        msg_flag = "FLAG Active"
    else:
        """Behavior if flag is inactive."""
        msg_flag = "FLAG Inactive"

    if waffle.switch_is_active('IS_ACTIVE_CUSTOM_SWITCH'):
        msg_switch = "SWITCH active"
    else:
        msg_switch = "SWITCH inactive"

    return HttpResponse(f"Bienvenidos al app base| {msg_flag} | {msg_switch}")