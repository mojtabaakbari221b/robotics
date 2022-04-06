from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'slideshow', views.SlideShowViewSet, basename='slideshow')
router.register(r'group', views.GroupViewSet, basename='group')
router.register(r'category', views.CategoryViewSet, basename='category')
router.register(r'organ', views.OrganViewSet, basename='company')
router.register(r'info', views.InfoViewSet, basename='info')
router.register(r'contact', views.ContactViewSet, basename='contact')
router.register(r'standards', views.StandardsViewSet, basename='standards')
router.register(r'product', views.ProductViewSet, basename='product')
router.register(r'tag', views.TagViewSet, basename='tag')
router.register(r'news', views.NewsViewSet, basename='news')
router.register(r'requirements', views.RequirementsViewSet, basename='requirements')
router.register(r'site_supporter', views.SiteSupporterViewSet, basename='site_supporter')
router.register(r'about_us', views.AboutUsViewSet, basename='about_us')
urlpatterns = router.urls
