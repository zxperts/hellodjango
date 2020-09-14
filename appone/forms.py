from django import forms
from django.forms import CheckboxSelectMultiple


class TestForm(forms.Form):
    CITIES_CHOICES = (
        (0, 'Paris'),
        (1, 'Toulouse'),
        (2, 'Lyon'),
    )

    name = forms.CharField(label='Your name', max_length=50)
    email = forms.EmailField(label='Your email', max_length=50, required=False)
    yes_no = forms.BooleanField(label='Either Yes or No')
    city = forms.ChoiceField(label='Your city', choices=CITIES_CHOICES)

class UserRegistrationForm(forms.Form):

    PLAN_CHOICES = (
        ('basic', 'Basic Plan'),
        ('premium', 'Premium Plan'),
        ('deluxe', 'Deluxe Plan'),

    )

    ADDITIONAL_0PTIONS_CHOICES = (
        ('storage', 'Extra Storage +1eGB'),
        ('support', 'Support On-Site 24/7'),
        ('account', 'Additional account'),

    )
    name=forms.CharField(label='Your name', max_length=50)
    email=forms.EmailField(label='Your mail', max_length=50)
    sign_to_news=forms.BooleanField(label='Sign up to the news letter', required=False)
    plan=forms.ChoiceField(label='Your plan', choices=PLAN_CHOICES)
    additional_options = forms.MultipleChoiceField(label='Additional options',
                                                   required=False,
                                                   widget=CheckboxSelectMultiple,
                                                   choices=ADDITIONAL_0PTIONS_CHOICES)

