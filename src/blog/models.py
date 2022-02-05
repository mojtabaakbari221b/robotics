from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import ArrayField
from .models_validators import (
    validate_media_extension,
)

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

class Galery(models.Model):
    media = models.FileField(upload_to='gallery/logo', validators=[validate_media_extension], verbose_name="تصویر یا ویدئو")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id})'

    class Meta: 
        verbose_name = "گالری"
        verbose_name_plural = "گالری ها"

class Group(models.Model):
    title = models.CharField(unique=True, null=False , max_length=512, verbose_name="عنوان")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.title})'

    class Meta: 
        verbose_name = "گروه"
        verbose_name_plural = "گروه ها"

class Category(models.Model):
    group = models.ForeignKey(Group, null=False , on_delete=models.CASCADE, verbose_name="گروه")
    title = models.CharField(unique=True, null=False , max_length=512, verbose_name="عنوان")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.group.title} - {self.title})'

    class Meta: 
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

class Organ(models.Model):
    CO = 'CO'
    ORGAN_CHOICES =(
        ('CO', 'Company'),
        ('LB', 'Labs'),
    )
    name = models.CharField(max_length=256, null=False, verbose_name="نام ارگان")
    logo = models.ImageField(upload_to='organization/logo', null=True , blank=True, verbose_name="لوگو")
    ceo_management_name = models.CharField(max_length=128, verbose_name="نام مدیر ارگان")
    ceo_management_image = models.ImageField(upload_to='organization/ceo_logo', null=False , blank=False, verbose_name="تصویر مدیر ارگان")
    date = models.DateField(default = now, verbose_name="تاریخ ثبت شرکت در سایت")
    info = RichTextField(max_length=512, null=True , blank=True, verbose_name="توضیحی مختصر درباره شرکت")
    activity_type = models.CharField(max_length=256, null=True , blank=True, verbose_name="زمینه فعالیت")
    tags = ArrayField(models.CharField(max_length=1024), null=True , blank=True, verbose_name="تگ ها")
    type = models.CharField(max_length=2, choices=ORGAN_CHOICES, default=CO, verbose_name="نوع شرکت")
    is_promote = models.BooleanField(default=False, verbose_name="یک ارگان ویژه است ؟")
    gallery = models.ManyToManyField(Galery, verbose_name="گالری")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.name})'

    class Meta: 
        verbose_name = "ارگان"
        verbose_name_plural = "ارگان ها"

class Info(models.Model):
    organ = models.ForeignKey(Organ , on_delete=models.CASCADE , related_name="info_company", verbose_name="مرتبط به ارگان")
    address = RichTextField(max_length=1024, null=True, blank=True, verbose_name="آدرس ارگان")
    website = models.URLField(max_length=512, null=True, blank=True, verbose_name="وبسایت")
    established_year = models.DateField(null=True, blank=True, verbose_name="سال تاسیس")
    validation_of_knowledge_base = models.BooleanField(default=False, verbose_name="مورد تایید دانش بنیان؟")
    introduction_of_a_company = RichTextField(max_length=2048, null=True, blank=True, verbose_name="درباره شرکت")
    number_of_staff = models.PositiveIntegerField(null=True, verbose_name="تعداد کارمندان")
    file = models.FileField(upload_to='info/file', null=True, blank=True, verbose_name="فایل مربوط")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.organ.name})'

    class Meta: 
        verbose_name = "اطلاعات ارگان"
        verbose_name_plural = "اطلاعات ارگان ها"

class Contact(models.Model):
    organ = models.ForeignKey(Organ , on_delete=models.CASCADE, verbose_name="مرتبط به ارگان")
    interface_name = models.CharField(max_length=128, null=True, blank=True, verbose_name="نام رابط")
    interface_phone_number = models.CharField(max_length=18, null=True, blank=True, verbose_name="شماره همراه رابط")
    tel_channel = models.URLField(max_length=256, null=True, blank=True, verbose_name="کانال تلگرام")
    fax = models.CharField(max_length=18, null=True, blank=True, verbose_name="فکس")
    email = models.EmailField(max_length=512, null=True, blank=True, verbose_name="ایمیل")
    phone_number = models.CharField(max_length=18, null=True, blank=True, verbose_name="شماره همراه")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.organ.name})'

    class Meta: 
        verbose_name = "تماس با ما"
        verbose_name_plural = "مجموعه تماس با ما"

class Standards(models.Model):
    organ = models.ForeignKey(Organ , on_delete=models.CASCADE, verbose_name="مرتبط به ارگان")
    title = models.CharField(max_length=128, verbose_name="عنوان")
    image = models.ImageField(upload_to='standard/image', verbose_name="عکس استاندارد")
    text = RichTextField(max_length=1024, null=True, blank=True, verbose_name="متن مرتبط به استاندارد")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.organ.name})'

    class Meta: 
        verbose_name = "استاندارها"
        verbose_name_plural = "استاندارهای ارگان ها "

class Product(models.Model):
    name = RichTextField(max_length=512, verbose_name="نام محصول")
    text = RichTextField(max_length=2056, verbose_name="متن مرتبط به محصول")
    date = models.DateField(default = now, verbose_name="تاریخ ثبت محصول در سایت")
    image = models.ImageField(upload_to='product/image', verbose_name="عکس اصلی محصول")
    organ = models.ForeignKey(Organ, on_delete=models.CASCADE, verbose_name="مرتبط به ارگان")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی محصول")
    tags = ArrayField(models.CharField(max_length=1024), null=True, blank=True, verbose_name="تگ های محصول")
    is_promote = models.BooleanField(default=False, verbose_name="ویژه است ؟")
    gallery = models.ManyToManyField(Galery, verbose_name="گالری")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.organ.name} - {self.name})'

    class Meta: 
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

class News(models.Model):
    title = RichTextField(max_length=512, verbose_name="عنوان خبر")
    date_of_submission = models.DateField(default = now, verbose_name="تاریخ ثبت خبر در سایت")
    text = RichTextField(max_length=2056, verbose_name="متن خبر")
    src = models.URLField(max_length=512, null=True, blank=True, verbose_name="لینک منبع خبر")
    media = models.FileField(upload_to='news/media', null=True, blank=True, validators=[validate_media_extension], verbose_name="عکس یا فیلم خبر")
    is_promote = models.BooleanField(default=False, verbose_name="ویژه است ؟")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.title})'

    class Meta: 
        verbose_name = "خبر"
        verbose_name_plural = "اخبار"

class Requirements(models.Model):
    title = RichTextField(max_length=256, verbose_name="عنوان نیازمندی")
    text = RichTextField(max_length=2056, verbose_name="متن نیازمندی")
    applicant_entity_name = RichTextField(max_length=256, verbose_name="نام سازمان درخواست کننده")
    applicant_entity_logo = models.ImageField(upload_to='requirements/applicant_entity_image', null=True, blank=True, verbose_name="لوگو سازمان درخواست کننده")
    image = models.ImageField(upload_to='requirements/image', null=True, blank=True, verbose_name="عکس مربوط به نیازمندی")
    date_of_submission = models.DateField(default = now, verbose_name="تاریخ ثبت نیازمندی در سایت")
    deadline = models.DateField(verbose_name="تاریخ اتمام زمان نیازمندی")
    file = models.FileField(upload_to='requirements/file', null=True, blank=True, verbose_name="فایل مربوط به نیازمندی")
    is_promote = models.BooleanField(default=False, verbose_name="ویژه است ؟")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.title})'

    class Meta: 
        verbose_name = "نیازمندی"
        verbose_name_plural = "نیازمندی ها"

class SiteSupporter(models.Model):
    name = RichTextField(max_length=512, verbose_name="نام حامی سایت")
    text = RichTextField(max_length=2056, null=True, blank=True, verbose_name="متن مربوطه")
    image = models.ImageField(upload_to='supporter/image', verbose_name="عکس حامی سایت")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.name})'

    class Meta: 
        verbose_name = "حامی سایت"
        verbose_name_plural = "حامیان سایت"

class Page(models.Model):
    title = RichTextField(max_length=256, null=True, blank=True, verbose_name="عنوان صفحه")
    text = RichTextField(max_length=4056, verbose_name="متنی که در صفحه قرار میگیرد")
    url = models.CharField(max_length=256, verbose_name="آدرس صفحه چه چیزی باشد ؟")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.title})'

    class Meta: 
        verbose_name = "صفحه شخصی شده"
        verbose_name_plural = "مجموعه صفحات شخصی سازی شده"