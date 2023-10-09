from django import forms
from django.core import validators
from .models import Users


class NewUserForm(forms.ModelForm):
    # custom validators would go here if you want them
    class Meta:
        model = Users
        fields = '__all__'


