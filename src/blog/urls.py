from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
]


router = DefaultRouter()
router.register(r'group', views.GroupViewSet, basename='group')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'category', views.CategoryViewSet, basename='category')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'organ', views.OrganViewSet, basename='company')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'info', views.InfoViewSet, basename='info')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'contact', views.ContactViewSet, basename='contact')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'standards', views.StandardsViewSet, basename='standards')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'product', views.ProductViewSet, basename='product')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'news', views.NewsViewSet, basename='news')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'requirements', views.RequirementsViewSet, basename='requirements')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'site_supporter', views.SiteSupporter, basename='requirements')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'page', views.Page, basename='requirements')
urlpatterns += router.urls