from django.contrib import admin
from . import models
from .cutomise_admin import (
    OrganAdmin,
    InfoAdmin,
)

admin.site.register(models.Group)
admin.site.register(models.Category)
admin.site.register(models.Organ, OrganAdmin)
admin.site.register(models.Info, InfoAdmin)
admin.site.register(models.Contact)
admin.site.register(models.Standards)
admin.site.register(models.Product)
admin.site.register(models.News)
admin.site.register(models.Requirements)
admin.site.register(models.Galery)
admin.site.register(models.File)
admin.site.register(models.Tag)
# admin.site.register(models.SlideShow)
admin.site.register(models.SiteSupporter)
admin.site.register(models.AboutUs)
