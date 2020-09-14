from django.db import models

# Create your models here.


class Device(models.Model):
    OS_ANDROID = 'android'
    OS_IOS = 'ios'

    OS_CHOICES = (
        (OS_ANDROID, 'android'),
        (OS_IOS, 'ios')
    )

    FORM_FACTOR_PHONE = 'phone'
    FORM_FACTOR_TABLET = 'tablet'

    FORM_FACTOR_CHOISCES =(
        (FORM_FACTOR_PHONE, 'phone'),
        (FORM_FACTOR_TABLET, 'tablet')
    )

    os = models.CharField(max_length=20, choices=OS_CHOICES, default=OS_ANDROID)
    form_factor = models.CharField(max_length=20, choices=FORM_FACTOR_CHOISCES, default=FORM_FACTOR_PHONE)
    model=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    description=models.TextField(blank=True)
    enabled=models.BooleanField(default=True)

    def __str__(self):
        return '{pk} - {os} {form_factor} {model} {created_at} {enabled} {description}'.format(
            pk=self.pk,
            os=self.get_os_display(),
            form_factor=self.get_os_display(),
            model=self.model,
            created_at=self.created_at,
            enabled=self.enabled,
            description=self.description
        )
class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{} {}'.format(self.pk,self.name)

class Departement(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{} {}'.format(self.pk,self.name)

class Employee(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey('Company',on_delete=models.CASCADE)
    departement = models.ForeignKey('Departement',on_delete=models.CASCADE)
    age = models.IntegerField()
    name = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return '{id} {name}, company={company}, department={departement}, age={age}, salary={salary}'.format(
            id=self.pk,
            name=self.name,
            company=self.company,
            departement=self.departement,
            age=self.age,
            salary=self.salary,
        )