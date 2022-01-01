from rest_framework import viewsets
from url_filter.integrations.drf import DjangoFilterBackend
from .models import (
    Group,
    Category,
    Info,
    Contact,
    Organ,
    Standards,
    Product,
    News,
    Requirements,
    SiteSupporter,
    Page,
)
from .serializers import (
    GroupSerializer,
    CategorySerializer,
    OrganSerializer,
    InfoSerializer,
    ContactSerializer,
    StandardsSerializer,
    ProductSerializer,
    NewsSerializer,
    RequirementsSerializer,
    SiteSupporterSerializer,
    PageSerializer,
)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filter_fields = '__all__'

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().prefetch_related('group')
    serializer_class = CategorySerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filter_fields = '__all__'

class OrganViewSet(viewsets.ModelViewSet):
    queryset = Organ.objects.all().prefetch_related('gallery')
    serializer_class = OrganSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filter_fields = '__all__'

class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all().select_related('organ')
    serializer_class = InfoSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filter_fields = '__all__'

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().select_related('organ')
    serializer_class = ContactSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filter_fields = '__all__'

class StandardsViewSet(viewsets.ModelViewSet):
    queryset = Standards.objects.all().select_related('organ')
    serializer_class = StandardsSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filter_fields = '__all__'

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().prefetch_related('category__group' , 'gallery').select_related('organ')
    serializer_class = ProductSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filter_fields = '__all__'

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filter_fields = '__all__'

class RequirementsViewSet(viewsets.ModelViewSet):
    queryset = Requirements.objects.all()
    serializer_class = RequirementsSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filter_fields = '__all__'


class SiteSupporterViewSet(viewsets.ModelViewSet):
    queryset = SiteSupporter.objects.all()
    serializer_class = SiteSupporterSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filter_fields = '__all__'

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filter_fields = '__all__'