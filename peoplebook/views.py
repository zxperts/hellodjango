from django.shortcuts import render
from django.template import loader
from peoplebook.peoples import  people

from django.http import HttpResponse
# Create your views here.

def users(request):
    template =loader.get_template('peoplebook/index.html')
    return HttpResponse(template.render({}, request))



def users_details(request,display='small'):
    return None


def users_list(request,display='small'):
    context={'users': people,
             }
    return render(request,'peoplebook/users_list.html',context)