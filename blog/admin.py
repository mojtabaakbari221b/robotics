from django.contrib import admin
from . import models
from . import cutomise_admin

admin.site.register(models.Group)
admin.site.register(models.Category)
admin.site.register(models.Organ, cutomise_admin.OrganAdmin)
admin.site.register(models.Info)
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
