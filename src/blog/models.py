from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import ArrayField

def compressImage(photo, name):
    import os
    from io import BytesIO
    import sys
    from PIL import Image
    from django.core.files.uploadedfile import InMemoryUploadedFile
    imageTemproary = Image.open(photo)
    imageTemproary = imageTemproary.convert('RGB')
    outputIoStream = BytesIO()
    if os.path.isfile(photo.path):
        os.remove(photo.path)
    if imageTemproary.width > 900 :
        ratio = 900 / imageTemproary.width
        imageTemproary = imageTemproary.resize( (int(imageTemproary.width * ratio) ,int(imageTemproary.height * ratio)) ) 
    imageTemproary.save(outputIoStream , format='JPEG', quality=70)
    outputIoStream.seek(0)
    photo.name = name[0:80]
    photo = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % photo.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
    return photo

class Group(models.Model):
    title = models.CharField(unique=True, null=False , max_length=512)

    def __str__(self):
        return f'{__class__.__name__}({self.id} , {self.title})'

class Category(models.Model):
    group = models.ForeignKey(Group, null=False , on_delete=models.CASCADE)
    title = models.CharField(unique=True, null=False , max_length=512)

    def __str__(self):
        return f'{__class__.__name__}({self.id} , {self.group.title} - {self.title})'

class Organ(models.Model):
    CO = 'CO'
    ORGAN_CHOICES =(
        ('CO', 'Company'),
        ('LB', 'Labs'),
    )
    name = RichTextField(max_length=256, null=False)
    logo = models.ImageField(upload_to='organization/logo', null=True , blank=True)
    ceo_management_name = RichTextField(max_length=128)
    ceo_management_image = models.ImageField(upload_to='organization/ceo_logo', null=False , blank=False)
    date = models.DateField(default = now)
    info = RichTextField(max_length=512, null=True , blank=True)
    activity_type = RichTextField(max_length=256, null=True , blank=True)
    tags = ArrayField(models.CharField(max_length=1024), null=True , blank=True)
    type = models.CharField(max_length=2, choices=ORGAN_CHOICES, default=CO)
    is_promote = models.BooleanField(default=False)

    def __str__(self):
        return f'{__class__.__name__}({self.id} , {self.name})'

class Info(models.Model):
    organ = models.ForeignKey(Organ , on_delete=models.CASCADE , related_name="info_company")
    address = RichTextField(max_length=1024, null=True, blank=True)
    website = models.URLField(max_length=512, null=True, blank=True)
    established_year = models.DateField(null=True, blank=True)
    validation_of_knowledge_base = models.BooleanField(default=False)
    introduction_of_a_company = RichTextField(max_length=2048, null=True, blank=True)
    number_of_staff = models.PositiveIntegerField(null=True)
    file = models.FileField(upload_to='info/file', null=True, blank=True)

    def __str__(self):
        return f'{__class__.__name__}({self.id} , {self.organ.name})'

class Contact(models.Model):
    organ = models.ForeignKey(Organ , on_delete=models.CASCADE)
    interface_name = models.CharField(max_length=128, null=True, blank=True)
    interface_phone_number = models.CharField(max_length=18, null=True, blank=True)
    tel_channel = models.URLField(max_length=256, null=True, blank=True)
    fax = models.CharField(max_length=18, null=True, blank=True)
    email = models.EmailField(max_length=512, null=True, blank=True)
    phone_number = models.CharField(max_length=18, null=True, blank=True)

    def __str__(self):
        return f'{__class__.__name__}({self.id} , {self.organ.name})'

class Standards(models.Model):
    organ = models.ForeignKey(Organ , on_delete=models.CASCADE)
    title = RichTextField(max_length=128)
    image = models.ImageField(upload_to='standard/image')
    text = RichTextField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f'{__class__.__name__}({self.id} , {self.organ.name})'

class Product(models.Model):
    name = RichTextField(max_length=256)
    text = RichTextField(max_length=2056)
    date = models.DateField(default = now)
    image = models.ImageField(upload_to='product/image')
    organ = models.ForeignKey(Organ, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    tags = ArrayField(models.CharField(max_length=1024), null=True, blank=True)
    is_promote = models.BooleanField(default=False)

    def __str__(self):
        return f'{__class__.__name__}({self.id} , {self.organ.name} - {self.name})'


class News(models.Model):
    title = RichTextField(max_length=256)
    date_of_submission = models.DateField(default = now)
    text = RichTextField(max_length=2056)
    src = models.URLField(max_length=2056)
    image = models.ImageField(upload_to='news/image', height_field=None, width_field=None, null=True, blank=True)
    media = models.FileField(upload_to='news/video', null=True, blank=True)
    is_promote = models.BooleanField(default=False)

    def __str__(self):
        return f'{__class__.__name__}({self.id} , {self.title})'
    

class Requirements(models.Model):
    title = RichTextField(max_length=256)
    text = RichTextField(max_length=2056)
    applicant_entity_name = RichTextField(max_length=256)
    applicant_entity_logo = models.ImageField(upload_to='requirements/applicant_entity_image', null=True, blank=True)
    image = models.ImageField(upload_to='requirements/image', null=True, blank=True)
    date_of_submission = models.DateField(default = now)
    deadline = models.DateField()
    file = models.FileField(upload_to='requirements/file', null=True, blank=True)
    is_promote = models.BooleanField(default=False)

    def __str__(self):
        return f'{__class__.__name__}({self.id} , {self.title})'

class SiteSupporter(models.Model):
    name = RichTextField(max_length=256)
    text = RichTextField(max_length=2056, null=True, blank=True)
    image = models.ImageField(upload_to='supporter/image')

class Page(models.Model):
    title = RichTextField(max_length=256, null=True, blank=True)
    text = RichTextField(max_length=4056)
    url = models.CharField(max_length=256)

# ********************* # TODO # ********************* #

# gallery for organ ?
# gallery for product ?.
