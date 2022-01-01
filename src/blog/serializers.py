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

class OrganSerializer(serializers.ModelSerializer):
    group = GroupSerializer(many=True)
    category = CategorySerializer(many=True)

    class Meta:
        model = models.Organ
        fields = '__all__'

class InfoSerializer(serializers.ModelSerializer):
    company = OrganSerializer()

    class Meta:
        model = models.Info
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    company = OrganSerializer()

    class Meta:
        model = models.Contact
        fields = '__all__'

class StandardsSerializer(serializers.ModelSerializer):
    company = OrganSerializer()

    class Meta:
        model = models.Standards
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    company = OrganSerializer()
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

class SiteSupporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SiteSupporter
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Page
        fields = '__all__'