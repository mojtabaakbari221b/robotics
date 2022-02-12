from this import d
from rest_framework import viewsets
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from .models import (
    Group,
    Category,
    Info,
    Contact,
    Organ,
    SlideShow,
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
    SlideShowSerializer,
)

class SlideShowViewSet(viewsets.ModelViewSet):
    queryset = SlideShow.objects.all().order_by('-id')[:6]
    serializer_class = SlideShowSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = '?'

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = '?'

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().select_related('group')
    serializer_class = CategorySerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = '?'

class OrganViewSet(viewsets.ModelViewSet):
    queryset = Organ.objects.all().prefetch_related('gallery', 'tags', 'files')
    serializer_class = OrganSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = '?'

class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all().select_related('organ')
    serializer_class = InfoSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = '?'

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().select_related('organ')
    serializer_class = ContactSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = '?'

class StandardsViewSet(viewsets.ModelViewSet):
    queryset = Standards.objects.all().select_related('organ')
    serializer_class = StandardsSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = '?'

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().prefetch_related('category__group' , 'gallery', 'files', 'tags', 'standard').select_related('organ')
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = '?'

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().prefetch_related('files', 'tags')
    serializer_class = NewsSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = '?'

class RequirementsViewSet(viewsets.ModelViewSet):
    queryset = Requirements.objects.all()
    serializer_class = RequirementsSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = '?'


class SiteSupporterViewSet(viewsets.ModelViewSet):
    queryset = SiteSupporter.objects.all()
    serializer_class = SiteSupporterSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = '?'

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = '?'