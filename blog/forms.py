from .models import (
    Info,
)
from django_jalali.admin.widgets import AdminjDateWidget, AdminSplitjDateTime
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminTimeWidget


class InfoAdminForm(ModelForm):
    class Meta:
        model = Info
        widgets = {
            'established_year': AdminjDateWidget(),
        }
        exclude = '__all__'