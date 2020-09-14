from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from appone.models import Device

def hello(request):
    return HttpResponse("Hello Django! appone application")


def device_add(request, os, model):
    device= Device(os=os, model=model)
    device.save()
    return HttpResponse("Created device {}".format(device))

def device_detail(request, id):
    try:
        device = Device.objects.get(id=id)
    except Device.DoesNotExist:
        return HttpResponse(status=404)

    return HttpResponse(device)

def devices_filter(request, os):
    devices_names = []
    for d in Device.objects.filter(os=os):
        devices_names.append(d.__str__())

    body='<br/>'.join(devices_names)
    return HttpResponse(body)



