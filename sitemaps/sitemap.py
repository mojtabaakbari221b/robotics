from django.contrib.sitemaps import Sitemap
from blog.views import *

organ_types_url = {
        "CO" : "company",
        "SC" : "providers",
        "LB" : "library",
    }

class StaticViewSitemap(Sitemap):
    static_pages = [
        "",
        "news",
        "requirement",
        "company",
        "providers",
        "library",
        "requirement",
    ]

    priority = 1.0
    changefreq = "daily"

    def items(self):
        return self.static_pages

    def location(self, item):
        return f"/{item}"
    

class OrganSitemap(Sitemap):
    queryset = OrganViewSet.queryset.order_by('-id')[0:10]
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return self.queryset
    
    def location(self, obj):
        return f"/{organ_types_url.get(obj.type)}/{obj.id}"

class ProductSitemap(Sitemap):
    queryset = ProductViewSet.queryset.order_by('-id')[0:10]
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return self.queryset
    
    def location(self, obj):
        return f"/{organ_types_url.get(obj.organ.type)}/{obj.organ.id}/product/{obj.id}"

class NewsSitemap(Sitemap):
    queryset = NewsViewSet.queryset.order_by('-id')[0:10]
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return self.queryset
    
    def location(self, obj):
        return f"/news/{obj.id}"

class RequiremetnsSitemap(Sitemap):
    queryset = RequirementsViewSet.queryset.order_by('-id')[0:10]
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return self.queryset
    
    def location(self, obj):
        return f"/requirement/{obj.id}"

