from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
]


router = DefaultRouter()
router.register(r'group', views.group_view_set, basename='group')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'category', views.category_view_set, basename='category')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'company', views.company_view_set, basename='company')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'info', views.info_view_set, basename='info')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'contact', views.contact_view_set, basename='contact')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'standards', views.standards_view_set, basename='standards')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'product', views.product_view_set, basename='product')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'news', views.news_view_set, basename='news')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'requirements', views.requirements_view_set, basename='requirements')
urlpatterns += router.urls