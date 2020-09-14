from django.contrib import admin

# Register your models here.
from appone.models import Employee
from appone.models import Company

admin.site.register(Employee)
admin.site.register(Company)

#python manage.py shell
#python manage.py createsuperuser