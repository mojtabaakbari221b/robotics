from django.contrib import admin
from .forms import InfoAdminForm

class OrganAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )

    list_display = (
        'name',
        'type',
        'ceo_management_name',
        'image_tag',
    )

    # fields = '__all__'
    readonly_fields = ['image_tag']

class InfoAdmin(admin.ModelAdmin):
    form = InfoAdminForm

    # pass