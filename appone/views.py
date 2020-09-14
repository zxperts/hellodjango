from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from appone.models import Device
from appone.forms import TestForm

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


def thanks(request):
    return HttpResponse('Thanks your form has been processed')


def get_form_data(request):

    if request.method == 'POST':
        print('In POST processing')

        form = TestForm(request.POST)
        if form.is_valid():
            print('name:', form.cleaned_data['name'])
            print('email:', form.cleaned_data['email'])
            print('yes_no:', form.cleaned_data['yes_no'])
            print('city:', form.cleaned_data['city'])

            return HttpResponseRedirect(reverse('thanks'))

    else:
        form = TestForm()
    return render(request, 'appone/form.html', {'form': form})



