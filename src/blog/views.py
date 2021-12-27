from rest_framework import viewsets
from url_filter.integrations.drf import DjangoFilterBackend
from .models import (
Group,
Category,
Company,
Info,
Contact,
Standards,
Product,
News,
Requirements,
)
from .serializers import (
GroupSerializer,
CategorySerializer,
CompanySerializer,
InfoSerializer,
ContactSerializer,
StandardsSerializer,
ProductSerializer,
NewsSerializer,
RequirementsSerializer,
)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [
            DjangoFilterBackend,
    ]
    filter_fields = '__all__'

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [
            DjangoFilterBackend,
    ]
    filter_fields = '__all__'

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [
            DjangoFilterBackend,
    ]
    filter_fields = '__all__'

class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    filter_backends = [
            DjangoFilterBackend,
    ]
    filter_fields = '__all__'

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [
            DjangoFilterBackend,
    ]
    filter_fields = '__all__'

class StandardsViewSet(viewsets.ModelViewSet):
    queryset = Standards.objects.all()
    serializer_class = StandardsSerializer
    filter_backends = [
            DjangoFilterBackend,
    ]
    filter_fields = '__all__'

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
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