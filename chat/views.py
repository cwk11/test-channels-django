from django.shortcuts import render
from health_check.backends import BaseHealthCheckBackend
from health_check.exceptions import ServiceUnavailable

# Create your views here.
def index(request):
    return render(request, 'chat/index.html')

def room(request,room_name):
    return render(request, 'chat/room.html', {
        'room_name': 'ltu'
    })


class MyHealthCheckBackend(BaseHealthCheckBackend):
    critical_service = False

    def check_status(self):
        pass
        raise ServiceUnavailable("error!")
    def identifier(self):
        return self.__class__.__name__
