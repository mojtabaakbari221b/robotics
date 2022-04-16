from this import d
from tokenize import group
from rest_framework import viewsets
from url_filter.integrations.drf import DjangoFilterBackend
from .filters import ExcludeTagFilterBackend
from rest_framework.filters import OrderingFilter
from blog.decorator import filtering
from rest_framework.response import Response
from .models import (
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
    AboutUs,
    Tag,
)
from .serializers import (
    CategorySerializer,
    OrganSerializer,
    InfoSerializer,
    ContactSerializer,
    StandardsSerializer,
    ProductSerializer,
    NewsSerializer,
    RequirementsSerializer,
    SiteSupporterSerializer,
    SlideShowSerializer,
    AboutUsSerializer,
    TagSerializer,
)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(group=None).order_by('-id')
    serializer_class = CategorySerializer

    @filtering
    def list(self, request, *args, **kwargs):
        return self.queryset

class SlideShowViewSet(viewsets.ModelViewSet):
    queryset = SlideShow.objects.all().order_by('-id')[:6]
    serializer_class = SlideShowSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = '?'

    @filtering
    def list(self, request, *args, **kwargs):
        # serializer = self.serializer_class(self.queryset, many=True)
        # return serializer.data
        return self.queryset

class OrganViewSet(viewsets.ModelViewSet):
    queryset = Organ.objects.prefetch_related('gallery','standards', 'tags', 'files', 'category').all()
    serializer_class = OrganSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = '?'
    lookup_field = 'slug'

class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all().prefetch_related('organ__gallery', 'organ__tags', 'organ__files', 'organ__category', 'organ__standards')
    serializer_class = InfoSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = '?'

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().prefetch_related('organ__gallery', 'organ__tags', 'organ__files', 'organ__category', 'organ__standards')
    serializer_class = ContactSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = '?'

class StandardsViewSet(viewsets.ModelViewSet):
    queryset = Standards.objects.all()
    serializer_class = StandardsSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = '?'

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.\
        prefetch_related('category' , 'gallery', 'files', 'tags', 'standard','organ__gallery', 'organ__tags', 'organ__files', 'organ__category', 'organ__standards')\
            .all()
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

class AboutUsViewSet(viewsets.ViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

    def list(self, request):
       serializer = self.serializer_class(self.queryset.last(), many=False)
       return Response(data=serializer.data)

class TagViewSet(viewsets.ViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [
        ExcludeTagFilterBackend,
        OrderingFilter,
    ]
    filter_fields = '__all__'
    ordering_fields = '__all__'
    ordering = '?'

    def get_serializer(self, queryset, many=True):
        return self.serializer_class(queryset, many=many)

    @filtering
    def list(self, request, *args, **kwargs):
        return self.queryset
