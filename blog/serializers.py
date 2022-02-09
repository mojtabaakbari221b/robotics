from rest_framework import serializers
from . import models

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Galery
        fields = '__all__'

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
    gallery = GallerySerializer(many=True)

    class Meta:
        model = models.Organ
        fields = '__all__'

class InfoSerializer(serializers.ModelSerializer):
    organ = OrganSerializer()

    class Meta:
        model = models.Info
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    organ = OrganSerializer()

    class Meta:
        model = models.Contact
        fields = '__all__'

class StandardsSerializer(serializers.ModelSerializer):
    organ = OrganSerializer()

    class Meta:
        model = models.Standards
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    organ = OrganSerializer()
    category = CategorySerializer(many=True)
    gallery = GallerySerializer(many=True)
    standard = StandardsSerializer(many=True)
    
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

class SlideShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SlideShow
        exclude = [
            'id',
            'content_type',
        ]