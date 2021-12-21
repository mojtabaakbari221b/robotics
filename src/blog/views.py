from rest_framework import viewsets
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

class group_view_set(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class category_view_set(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class company_view_set(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class info_view_set(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

class contact_view_set(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class standards_view_set(viewsets.ModelViewSet):
    queryset = Standards.objects.all()
    serializer_class = StandardsSerializer

class product_view_set(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class news_view_set(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class requirements_view_set(viewsets.ModelViewSet):
    queryset = Requirements.objects.all()
    serializer_class = RequirementsSerializer