from django import forms
from django.contrib.auth import get_user_model
from django.db.models import fields
from .models import *


class contact(forms.ModelForm):
    class Meta:
        model = contactform
        fields = ("__all__")        