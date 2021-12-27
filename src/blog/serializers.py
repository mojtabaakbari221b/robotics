from rest_framework import serializers
from . import models

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = models.Category
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    group = GroupSerializer(many=True)

    class Meta:
        model = models.Company
        fields = '__all__'

class InfoSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = models.Info
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = models.Contact
        fields = '__all__'

class StandardsSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = models.Standards
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    category = CategorySerializer(many=True)

    class Meta:
        model = models.Product
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = '__all__'

class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Requirements
        fields = '__all__'