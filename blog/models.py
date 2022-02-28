from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from location_field.models.plain import PlainLocationField
from .models_validators import (
    validate_media_extension,
    validate_video_extension,
)
from django.db.models.signals import (
    post_save,
    m2m_changed,
    pre_save,
)
from django.dispatch import receiver
from django.utils.html import mark_safe
from robotic.settings import HOST_AND_DOMAIN

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

class ImageFieldForPanelAdmin():

    default_image_url = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQMAAADCCAMAAAB6zFdcAAAAYFBMVEXa2tpVVVXd3d1OTk5SUlJwcHC1tbVLS0uOjo7h4eGcnJxWVlbU1NRaWlphYWGnp6fHx8e8vLxra2umpqa5ubnOzs51dXWvr6+WlpaGhobDw8OAgIBkZGR7e3uQkJBERETECcahAAACeUlEQVR4nO3b6W6qQBiAYWaxw7gdxAXc2vu/y4qIgIKpQo7x433+lUaTeYPDDGIQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGQffo3WN5jV7Go/74dw/nJXrsbH8+tYFRvZnQgAY0kNDAuE4kNLDp6quDxVxAA5P4LmsjP7cCGvzrtMajwTAb3G4NhtdAB7skWVdfMLgGOhqdroY2rBwaWgMd2fOA3aY8NrgGG5uviFz5mqE1WBeLaxtfhzywBnrliu3B7HpwaA12RQM7l/xZ0Kv9gyTzy3xgQsmfBR27sHU4epmfCNauBZ8HOnHKpa3j8Wl2C9KoRfkSeQ2Cw2lEbtx+Juy28SitLhTFNfD5ye6W7RG897UJQ1yDYHaZ85L6kB5Mk9Ia+LRYBP181SbKRfu7SGswVVd2URnU1O5bv0wT1sBvKzea3a48PUJj4mlLBFkN9Lp6r91OouJ45LKV4bo5grAGe6uqEYqFUL5btGbXGEFUg3I3cN0UnCPoL3NpkjSNU1QDP7LqNsJ5Eig2Cc1rJ0kNKhvjMsJpJvTj8rgL7z8OkhoE8e1pkP1vdLouVv52x7vlkqAG2WapgTlua2nur5GSGkyaEmQz4e0cEdUjyGng//w9vLWr2nDlNJjO/pggWyjUrpFiGujomccxajdZBtpAua3A+0hPNlBuc708SGrQsDp4wByKLZSgBmr2nMnssoUS0+B0YXhe/i6CGryMBlIaJL6Tg4AG9vgddvCdrzA/u4Hq+NC+ktCgFzSgAQ0+u0H60+2p/ZoPbRB1eWb/1qf+uK9P7x4MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPwHvzkNNPrHNmiDAAAAAElFTkSuQmCC"
    
    def return_image_url(self, image_field):
        if image_field.name is None or len(image_field.name) == 0 :
            return self.default_image_url # default image
        else :
            return f"{HOST_AND_DOMAIN}/media/{image_field}"

    def image_tag(self):
        image_field = self.return_image_field()
        image_url = self.return_image_url(image_field)
        return mark_safe(f'<img src="{image_url}" width="150" height="150" />')
    image_tag.short_description = 'تصویر'
    image_tag.allow_tags = True

class SlideShow(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    title = models.TextField()
    type = models.TextField()
    media = models.FileField(upload_to='slideshow', blank=True)
    is_video = models.BooleanField(default=False)
    organ_type = models.CharField(max_length=2 , blank=True)
    video_poster = models.ImageField(upload_to='slideshow/poster' , blank=True)
    organ_id = models.PositiveBigIntegerField(null=True)

class File(models.Model):
    file = models.FileField(upload_to='file', verbose_name="فایل")
    describe = models.CharField(max_length=500, null=True , blank=True, verbose_name="توضیح فایل")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id}, {self.describe})'

    class Meta: 
        verbose_name = "فایل"
        verbose_name_plural = "فایل ها"

class Galery(models.Model):
    media = models.FileField(upload_to='gallery/logo', validators=[validate_media_extension], verbose_name="تصویر یا ویدئو")
    video_poster = models.ImageField(upload_to='gallery', verbose_name="پوستر ویدئو", null=True, blank=True, help_text="این فیلد موقعی استفاده میشود که یک ویدئو بارگزاری میکنید")
    describe = models.CharField(max_length=500, null=True , blank=True, verbose_name="توضیح گالری")
    is_video = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id}, {self.describe})'

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

class Tag(models.Model):
    title = models.CharField(max_length=4096, null=False, blank=True, verbose_name="عنوان تگ")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id}, {self.title})'

    class Meta: 
        verbose_name = "تگ"
        verbose_name_plural = "تگ ها"

class Category(models.Model):
    group = models.ForeignKey(Group, null=False , on_delete=models.CASCADE, verbose_name="گروه")
    title = models.CharField(unique=True, null=False , max_length=512, verbose_name="عنوان")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.group.title} - {self.title})'

    class Meta: 
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

class Organ(models.Model, ImageFieldForPanelAdmin):
    CO = 'CO'
    ORGAN_CHOICES =(
        ('CO', 'Company'),
        ('LB', 'Labs'),
        ('SC', 'Services')
    )
    banner = models.ImageField(upload_to='organization/banner', null=True , blank=True, verbose_name="بنر" )
    name = models.CharField(max_length=256, null=False, verbose_name="نام ارگان")
    media = models.ImageField(upload_to='organization/logo', null=True , blank=True, verbose_name="لوگو")
    ceo_management_name = models.CharField(max_length=128, verbose_name="نام مدیر ارگان")
    ceo_management_image = models.ImageField(upload_to='organization/ceo_logo', null=False , blank=False, verbose_name="تصویر مدیر ارگان")
    date = models.DateTimeField(default = now, verbose_name="تاریخ ثبت شرکت در سایت")
    info = models.CharField(max_length=512, null=True , blank=True, verbose_name="توضیحی مختصر درباره شرکت")
    activity_type = models.CharField(max_length=256, null=True , blank=True, verbose_name="زمینه فعالیت")
    tags = models.ManyToManyField(Tag, verbose_name="تگ ها", blank=True)
    type = models.CharField(max_length=2, choices=ORGAN_CHOICES, default=CO, verbose_name="نوع شرکت")
    is_promote = models.BooleanField(default=False, verbose_name="یک ارگان ویژه است ؟")
    gallery = models.ManyToManyField(Galery, verbose_name="گالری", blank=True)
    files = models.ManyToManyField(File, verbose_name="فایل ها", blank=True)
    category = models.ManyToManyField(Category,editable=False, blank=True, verbose_name="دسته بندی ها")
    standards = models.ManyToManyField('Standards', blank=True, related_name='organ_standards', verbose_name="استاندارد ها")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.name})'

    def return_image_field(self) :
        return self.media


    class Meta: 
        verbose_name = "ارگان"
        verbose_name_plural = "ارگان ها"


class Info(models.Model):
    organ = models.ForeignKey(Organ , on_delete=models.CASCADE , related_name="info_company", verbose_name="مرتبط به ارگان")
    address = models.TextField(null=True, blank=True, verbose_name="آدرس ارگان")
    website = models.URLField(max_length=512, null=True, blank=True, verbose_name="وبسایت")
    established_year = models.DateTimeField(null=True, blank=True, verbose_name="سال تاسیس")
    validation_of_knowledge_base = models.BooleanField(default=False, verbose_name="مورد تایید دانش بنیان؟")
    introduction_of_a_company = models.TextField(null=True, blank=True, verbose_name="درباره شرکت")
    number_of_staff = models.PositiveIntegerField(null=True, verbose_name="تعداد کارمندان")
    file = models.FileField(upload_to='info/file', null=True, blank=True, verbose_name="فایل مربوط")
    company_city = models.CharField(max_length=250,null=True, blank=True, verbose_name="شهر محل کار شرکت" )

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
    phone_number = models.TextField(null=True, blank=True, verbose_name="شماره همراه")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.organ.name})'

    class Meta: 
        verbose_name = "تماس با ما"
        verbose_name_plural = "مجموعه تماس با ما"

class Standards(models.Model):
    title = models.CharField(max_length=128, verbose_name="عنوان")
    image = models.ImageField(upload_to='standard/image', verbose_name="عکس استاندارد")
    text = models.CharField(max_length=500, null=True, blank=True, verbose_name="متن مرتبط به استاندارد")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.title})'

    class Meta: 
        verbose_name = "استاندارد"
        verbose_name_plural = "استانداردها"

class Product(models.Model):
    name = models.CharField(max_length=512, verbose_name="نام محصول")
    text = RichTextField(verbose_name="متن مرتبط به محصول")
    date = models.DateTimeField(default = now, verbose_name="تاریخ ثبت محصول در سایت")
    media = models.ImageField(upload_to='product/image', verbose_name="عکس اصلی محصول")
    organ = models.ForeignKey(Organ, on_delete=models.CASCADE, verbose_name="مرتبط به ارگان")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی محصول")
    tags = models.ManyToManyField(Tag, verbose_name="تگ ها", blank=True)
    is_promote = models.BooleanField(default=False, verbose_name="ویژه است ؟")
    gallery = models.ManyToManyField(Galery, verbose_name="گالری", blank=True)
    files = models.ManyToManyField(File, verbose_name="فایل ها", blank=True)
    standard = models.ManyToManyField(Standards, verbose_name="استاندارد ها", blank=True)

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.organ.name} - {self.name})'

    class Meta: 
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

class News(models.Model):
    name = models.CharField(max_length=512, verbose_name="عنوان خبر")
    date_of_submission = models.DateTimeField(default = now, verbose_name="تاریخ ثبت خبر در سایت")
    text = RichTextField(verbose_name="متن خبر")
    src = models.URLField(max_length=512, null=True, blank=True, verbose_name="لینک منبع خبر")
    media = models.FileField(upload_to='news/media', null=True, blank=True, validators=[validate_media_extension], verbose_name="عکس یا فیلم خبر")
    is_promote = models.BooleanField(default=False, verbose_name="ویژه است ؟")
    files = models.ManyToManyField(File, verbose_name="فایل ها", blank=True)
    tags = models.ManyToManyField(Tag, verbose_name="تگ ها", blank=True)
    is_video = models.BooleanField(default=False, editable=False)
    video_poster = models.ImageField(upload_to='gallery', verbose_name="پوستر ویدئو", null=True, blank=True, help_text="این فیلد موقعی استفاده میشود که یک ویدئو بارگزاری میکنید")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.name})'

    class Meta: 
        verbose_name = "خبر"
        verbose_name_plural = "اخبار"

class Requirements(models.Model):
    name = models.CharField(max_length=256, verbose_name="عنوان نیازمندی")
    text = RichTextField(verbose_name="متن نیازمندی")
    applicant_entity_name = models.CharField(max_length=256, verbose_name="نام سازمان درخواست کننده")
    applicant_entity_logo = models.ImageField(upload_to='requirements/applicant_entity_image', null=True, blank=True, verbose_name="لوگو سازمان درخواست کننده")
    media = models.ImageField(upload_to='requirements/image', null=True, blank=True, verbose_name="عکس مربوط به نیازمندی")
    date_of_submission = models.DateTimeField(default = now, verbose_name="تاریخ ثبت نیازمندی در سایت")
    deadline = models.DateTimeField(verbose_name="تاریخ اتمام زمان نیازمندی")
    file = models.FileField(upload_to='requirements/file', null=True, blank=True, verbose_name="فایل مربوط به نیازمندی")
    is_promote = models.BooleanField(default=False, verbose_name="ویژه است ؟")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.name})'

    class Meta: 
        verbose_name = "نیازمندی"
        verbose_name_plural = "نیازمندی ها"

class SiteSupporter(models.Model):
    name = models.CharField(max_length=512, verbose_name="نام حامی سایت")
    image = models.ImageField(upload_to='supporter/image', verbose_name="عکس حامی سایت")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.name})'

    class Meta: 
        verbose_name = "حامی سایت"
        verbose_name_plural = "حامیان سایت"

class AboutUs(models.Model):
    email = models.EmailField(verbose_name="ایمیل")
    phone_number = models.CharField(max_length=18, verbose_name="شماره تلفن")
    fax = models.TextField(verbose_name="فکس")
    address = models.TextField(verbose_name="آدرس")
    info = RichTextField(verbose_name="اطلاعات")
    location = PlainLocationField(based_fields=['city'], zoom=13, verbose_name="مکان")
    telegram_channel = models.URLField(blank=True)
    whatsapp_channel = models.URLField(blank=True)
    twitter_channel = models.URLField(blank=True)
    instagram_channel = models.URLField(blank=True)
    bale_channel = models.URLField(blank=True)
    eata_channel = models.URLField(blank=True)

    class Meta: 
        verbose_name = "صفحه درباره ما"
        verbose_name_plural = "درباره ما"

@receiver(m2m_changed, sender=Product.category.through)
def add_Category_to_organ(sender, instance, *args,**kwargs):
    products = Product.objects.filter(organ=instance.organ).values('id')
    categories = Category.objects.filter(product__in=products).distinct()
    instance.organ.category.set(categories)

@receiver(pre_save, sender=News)
@receiver(pre_save, sender=Galery)
def edit_is_video_filed_in_instance_before_save(sender, instance, **kwargs):
    if instance.media != "" and instance.media is not None :
        try :
            validate_video_extension(instance.media)
            instance.is_video = True
        except :
            instance.is_video = False

@receiver(post_save, sender=Requirements)
@receiver(post_save, sender=News)
@receiver(post_save, sender=Product)
@receiver(post_save, sender=Organ)
def add_promoter_to_slideshow(sender, instance, **kwargs):
    type = ContentType.objects.get_for_model(sender)
    slideshow_s = SlideShow.objects.filter(content_type__pk=type.id, object_id=instance.id)
    if instance.is_promote :
        slideshow_object = SlideShow.objects.get_or_create(
            content_type=type,
            object_id=instance.id
        )[0]
        slideshow_object.title = instance.name
        slideshow_object.media = instance.media
        slideshow_object.type = instance._meta.verbose_name
        if sender == News :
            slideshow_object.is_video = instance.is_video
            slideshow_object.video_poster = instance.video_poster
        if sender == Organ :
            slideshow_object.organ_type = instance.type
            slideshow_object.media = instance.banner
        if sender == Product :
            slideshow_object.organ_id = instance.organ.id
            slideshow_object.organ_type = instance.organ.type
        slideshow_object.save()
    elif slideshow_s.exists():
        slideshow_s.delete()

