from django.contrib import admin
from .forms import InfoAdminForm

class OrganAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )

    list_display = (
        'id',
        'name',
        'type',
        'ceo_management_name',
        'image_tag',
    )

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

class StandardAdmin(admin.ModelAdmin):
    search_fields = (
        'title',
    )

    list_display = (
        'id',
        'title',
        'text',
        'image_tag',
    )

class SiteSupporterAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )

    list_display = (
        'id',
        'name',
        'image_tag',
    )

class RequirementsAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )

    list_display = (
        'id',
        'name',
        'image_tag',
    )

class GalleryAdmin(admin.ModelAdmin):
    search_fields = (
        'describe',
    )

    list_display = (
        'id',
        'describe',
        'is_video',
        'image_tag',
    )

class NewsAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )

    list_display = (
        'id',
        'name',
        'src',
        'is_video',
        'image_tag',
    )


class SlideShowAdmin(admin.ModelAdmin):
    list_display = [
        'type',
        'object_id',
        'title',
        'image_tag',
    ]

    readonly_fields = [
        'type',
        'object_id',
        'title',
    ]

    exclude = [
        'content_object',
    ]