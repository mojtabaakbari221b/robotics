from django.contrib import admin
from . import models
from . import cutomise_admin 



admin.site.register(models.Group)
admin.site.register(models.Category)
admin.site.register(models.Organ, cutomise_admin.OrganAdmin)
admin.site.register(models.Info, cutomise_admin.InfoAdmin)
admin.site.register(models.Contact)
admin.site.register(models.Standards, cutomise_admin.StandardAdmin)
admin.site.register(models.Product, cutomise_admin.ProductAdmin)
admin.site.register(models.News, cutomise_admin.NewsAdmin)
admin.site.register(models.Requirements, cutomise_admin.RequirementsAdmin)
admin.site.register(models.Galery, cutomise_admin.GalleryAdmin)
admin.site.register(models.File)
admin.site.register(models.Tag)
admin.site.register(models.SiteSupporter, cutomise_admin.SiteSupporterAdmin)
admin.site.register(models.AboutUs)
admin.site.register(models.SlideShow, cutomise_admin.SlideShowAdmin)
