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

class ProductAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )

    list_display = (
        'id',
        'name',
        'get_organ_value',
        'image_tag',
    )


class SlideShowAdmin(admin.ModelAdmin):
    list_display = [
        'type',
        'object_id',
        'title',
    ]

    readonly_fields = [
        'type',
        'object_id',
        'title',
    ]

    exclude = [
        'content_object',
    ]