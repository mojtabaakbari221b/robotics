from rest_framework import serializers
from . import models

class jDateSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return str(instance.timestamp())

class StandardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Standards
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'

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
    tags = TagSerializer(many=True)
    files = FileSerializer(many=True)
    category = CategorySerializer(many=True)
    standards = StandardsSerializer(many=True)
    date = jDateSerializer()

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

class ProductSerializer(serializers.ModelSerializer):
    organ = OrganSerializer()
    category = CategorySerializer(many=True)
    gallery = GallerySerializer(many=True)
    standard = StandardsSerializer(many=True)
    tags = TagSerializer(many=True)
    files = FileSerializer(many=True)
    date = jDateSerializer()
    
    class Meta:
        model = models.Product
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True)
    tags = TagSerializer(many=True)
    date_of_submission = jDateSerializer()

    class Meta:
        model = models.News
        fields = '__all__'

class RequirementsSerializer(serializers.ModelSerializer):
    date_of_submission = jDateSerializer()
    deadline = jDateSerializer()

    class Meta:
        model = models.Requirements
        fields = '__all__'

class SiteSupporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SiteSupporter
        fields = '__all__'

class SlideShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SlideShow
        exclude = [
            'id',
            'content_type',
        ]

class AboutUsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.AboutUs
        fields = '__all__'