from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from appone.models import Device
from appone.forms import TestForm
from appone.forms import UserRegistrationForm
from appone.forms import SongForm

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

def thanks_user(request,name):
    return HttpResponse('Thanks {} your registration is successfull'.format(name))


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

def user_register(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']

            if form.cleaned_data['sign_to_news']:
                print('Signed up {} to eh newsletter'.format(form.cleaned_data['email']))

            print(form)

            return HttpResponseRedirect(reverse('thanks_user', args=[name]))

    else:
        form = UserRegistrationForm()
    return render(request, 'appone/user_registration.html', {'form':form})


def song_create(request):
    form = SongForm()
    return render(request, 'appone/song_create.html', {'form': form})

