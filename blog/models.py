from django.db import models
from django.utils.timezone import now
from django_quill.fields import QuillField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from location_field.models.plain import PlainLocationField
from django.contrib.admin import display
from .models_validators import (
    validate_media_extension,
)
from common.utilities import (
    ImageFieldForPanelAdmin,
)
from django_jalali.db import models as jmodels

class SlideShow(models.Model, ImageFieldForPanelAdmin):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, editable=False)
    object_id = models.PositiveIntegerField(verbose_name="آیدی محتوا")
    content_object = GenericForeignKey('content_type', 'object_id')
    title = models.TextField(verbose_name="عنوان محتوا")
    type = models.TextField(verbose_name="نوع محتوا")
    media = models.FileField(upload_to='slideshow', blank=True, editable=False)
    is_video = models.BooleanField(default=False, editable=False)
    organ_type = models.CharField(max_length=2 , blank=True, editable=False)
    video_poster = models.ImageField(upload_to='slideshow/poster' , blank=True, editable=False)
    organ_id = models.PositiveBigIntegerField(null=True, editable=False)

    class Meta: 
        verbose_name = "اسلاید شو"
        verbose_name_plural = "مجموعه اسلاید شو"

    def return_image_field(self) :
        if self.is_video :
            return self.video_poster
        return self.media

class File(models.Model):
    file = models.FileField(upload_to='file', verbose_name="فایل")
    describe = models.CharField(max_length=500, null=True , blank=True, verbose_name="توضیح فایل")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id}, {self.describe})'

    class Meta: 
        verbose_name = "فایل"
        verbose_name_plural = "فایل ها"

class Galery(models.Model, ImageFieldForPanelAdmin):
    media = models.FileField(upload_to='gallery/logo', validators=[validate_media_extension], verbose_name="تصویر یا ویدئو")
    video_poster = models.ImageField(upload_to='gallery', verbose_name="پوستر ویدئو", null=True, blank=True, help_text="این فیلد موقعی استفاده میشود که یک ویدئو بارگزاری میکنید")
    describe = models.CharField(max_length=500, null=True , blank=True, verbose_name="توضیح گالری")
    is_video = models.BooleanField(default=False, editable=False, verbose_name="فرمت ویدئو دارد ؟")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id}, {self.describe})'

    class Meta: 
        verbose_name = "گالری"
        verbose_name_plural = "گالری ها"

    def return_image_field(self) :
        if self.is_video :
            return self.video_poster
        return self.media

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
    ceo_management_image = models.ImageField(upload_to='organization/ceo_logo', null=True , blank=True, verbose_name="تصویر مدیر ارگان")
    date = jmodels.jDateTimeField(default = now, verbose_name="تاریخ ثبت شرکت در سایت")
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
    validation_of_knowledge_base = models.BooleanField(default=False, verbose_name="مورد تایید دانش بنیان؟")
    introduction_of_a_company = models.TextField(null=True, blank=True, verbose_name="درباره شرکت")
    number_of_staff = models.PositiveIntegerField(null=True, verbose_name="تعداد کارمندان")
    file = models.FileField(upload_to='info/file', null=True, blank=True, verbose_name="فایل مربوط")
    company_city = models.CharField(max_length=250,null=True, blank=True, verbose_name="شهر محل کار شرکت" )

    established_year = models.PositiveIntegerField(default=1400,null=True, verbose_name="سال تاسیس")

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

class Standards(models.Model, ImageFieldForPanelAdmin):
    title = models.CharField(max_length=128, verbose_name="عنوان")
    image = models.ImageField(upload_to='standard/image', verbose_name="عکس استاندارد")
    text = models.CharField(max_length=500, null=True, blank=True, verbose_name="متن مرتبط به استاندارد")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.title})'

    class Meta: 
        verbose_name = "استاندارد"
        verbose_name_plural = "استانداردها"
    
    def return_image_field(self) :
        return self.image

class Product(models.Model, ImageFieldForPanelAdmin):
    name = models.CharField(max_length=512, verbose_name="نام محصول")
    text = QuillField(verbose_name="متن مرتبط به محصول")
    date = jmodels.jDateTimeField(default = now, verbose_name="تاریخ ثبت محصول در سایت")
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

    def return_image_field(self) :
            return self.media
    
    @display(description='مرتبط به ارگان')
    def get_organ_value(self):
        return self.organ.name

class News(models.Model, ImageFieldForPanelAdmin):
    name = models.CharField(max_length=512, verbose_name="عنوان خبر")
    date_of_submission = jmodels.jDateTimeField(default = now, verbose_name="تاریخ ثبت خبر در سایت")
    text = QuillField(verbose_name="متن خبر")
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
    
    def return_image_field(self) :
        if self.is_video :
            return self.video_poster
        return self.media

class Requirements(models.Model, ImageFieldForPanelAdmin):
    name = models.CharField(max_length=256, verbose_name="عنوان نیازمندی")
    text = QuillField(verbose_name="متن نیازمندی")
    applicant_entity_name = models.CharField(max_length=256, verbose_name="نام سازمان درخواست کننده")
    applicant_entity_logo = models.ImageField(upload_to='requirements/applicant_entity_image', null=True, blank=True, verbose_name="لوگو سازمان درخواست کننده")
    media = models.ImageField(upload_to='requirements/image', null=True, blank=True, verbose_name="عکس مربوط به نیازمندی")
    date_of_submission = jmodels.jDateTimeField(default = now, verbose_name="تاریخ ثبت نیازمندی در سایت")
    deadline = jmodels.jDateTimeField(null=True, blank=True, default = now, verbose_name="تاریخ اتمام نیازمندی")
    file = models.FileField(upload_to='requirements/file', null=True, blank=True, verbose_name="فایل مربوط به نیازمندی")
    is_promote = models.BooleanField(default=False, verbose_name="ویژه است ؟")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.name})'

    class Meta: 
        verbose_name = "نیازمندی"
        verbose_name_plural = "نیازمندی ها"

    def return_image_field(self) :
            return self.media

class SiteSupporter(models.Model, ImageFieldForPanelAdmin):
    name = models.CharField(max_length=512, verbose_name="نام حامی سایت")
    image = models.ImageField(upload_to='supporter/image', verbose_name="عکس حامی سایت")

    def __str__(self):
        return f'{self._meta.verbose_name}({self.id} , {self.name})'

    class Meta: 
        verbose_name = "حامی سایت"
        verbose_name_plural = "حامیان سایت"

    def return_image_field(self) :
            return self.image

class AboutUs(models.Model):
    email = models.EmailField(verbose_name="ایمیل")
    phone_number = models.CharField(max_length=18, verbose_name="شماره تلفن")
    fax = models.TextField(verbose_name="فکس")
    address = models.TextField(verbose_name="آدرس")
    info = QuillField(verbose_name="اطلاعات")
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



