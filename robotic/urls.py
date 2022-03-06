"""robotic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.contrib.sitemaps import views as sitemaps_views
from sitemaps import sitemap

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/blog/', include('blog.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

# sitemap configuration

sitemaps = {
    'static': sitemap.StaticViewSitemap,
    'organ': sitemap.OrganSitemap,
    'product': sitemap.ProductSitemap,
    'news': sitemap.NewsSitemap,
    'requirement': sitemap.RequiremetnsSitemap,
}


urlpatterns += [
    path('sitemap.xml/', sitemaps_views.sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
]

from .settings import DEBUG
if DEBUG :
    from .settings import MEDIA_URL, MEDIA_ROOT
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

# swagger

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path

schema_view = get_schema_view(
   openapi.Info(
      title="robomech API",
      default_version='v1.0',
      description="design and developed by Hirkano",
      terms_of_service="https://www.hirkano.ir/",
   ),
   public=True,
   permission_classes=[
       permissions.IsAuthenticated,
       permissions.IsAdminUser,
    ],
)

urlpatterns += [
   re_path(r'^api/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^api/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]