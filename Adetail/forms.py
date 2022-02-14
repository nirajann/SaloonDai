from django import forms
from django.contrib.auth import get_user_model
from django.db.models import fields
from .models import *


class details(forms.ModelForm):
    class Meta:
        model = data_field
        fields = ("__all__")


class h_details(forms.ModelForm):
    class Meta:
        model = history_data
        fields = ("__all__")