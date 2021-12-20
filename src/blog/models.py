from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import ArrayField

def compressImage(photo):
    from io import BytesIO
    import sys
    from PIL import Image
    from django.core.files.uploadedfile import InMemoryUploadedFile

    imageTemproary = Image.open(photo)
    outputIoStream = BytesIO()
    imageTemproary.save(outputIoStream , format='JPEG', quality=70)
    outputIoStream.seek(0)
    photo = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % photo.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
    return photo

# relational Models

class Group():
    title = models.CharField(unique=True , max_length=512)

class Category():
    group = models.ForeignKey(Group)
    title = models.CharField(unique=True , max_length=512)

class Company(models.Model):
    name = RichTextField(max_length=256)
    activity_type = RichTextField(max_length=256)
    logo = models.ImageField(upload_to='organization/logo')
    group = models.ManyToManyField(Group)
    ceo_management = RichTextField(max_length=128)
    info = RichTextField(max_length=512)
    tags = ArrayField(models.CharField(max_length=1024))

    def save(self, *args, **kwargs):
        if self.logo :
            self.logo = compressImage(self.logo)
        super(Company, self).save(*args, **kwargs)

class Info(models.Model):
    company = models.ForeignKey(Company)
    address = RichTextField(max_length=1024)
    website = models.URLField(max_length=512)
    established_year = models.DateField()
    validation_of_knowledge_base = models.BooleanField(default=False)
    introduction_of_a_company = RichTextField(max_length=2048)
    number_of_staff = models.PositiveIntegerField(null=True)
    file = models.FieldFile(upload_to='info/file')

class Contact(models.Model):
    company = models.ForeignKey(Company)
    interface_name = models.CharField(max_length=128)
    interface_phone_number = models.CharField(max_length=18)
    tel_channel = models.URLField(max_length=256)
    fax = models.CharField(max_length=18)
    email = models.EmailField(max_length=512)
    phone_number = models.CharField(max_length=18)

class Standards(models.Model):
    company = models.ForeignKey(Company)
    title = RichTextField(max_length=128)
    image = models.ImageField(upload_to='standard/image')
    text = RichTextField(max_length=128)

class Product(models.Model):
    name = RichTextField(max_length=256)
    text = RichTextField(max_length=2056)
    date = models.DateField(default = now)
    image = models.ImageField(upload_to='product/image')
    company = models.ForeignKey(Company)
    category = models.ForeignKey(Category)


# 

class News(models.Model):
    title = RichTextField(max_length=256)
    date_of_submission = models.DateField(default = now)
    text = RichTextField(max_length=2056)
    src = models.URLField(max_length=2056)
    media = models.FieldFile(upload_to='news/media')
    

class Requirements(models.Model):
    title = RichTextField(max_length=256)
    text = RichTextField(max_length=2056)
    applicant_entity_name = RichTextField(max_length=256)
    applicant_entity_logo = models.ImageField(upload_to='requirements/applicant_entity_image')
    image = models.ImageField(upload_to='requirements/image')
    date_of_submission = models.DateField(default = now)
    deadline = models.DateField()