from .models import *
from django.db.models.signals import (
    post_save,
    pre_save,
    post_delete,
)
from django.dispatch import receiver
from .models_validators import (
    validate_video_extension,
)

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

@receiver(post_delete, sender=Organ)
@receiver(post_delete, sender=Requirements)
@receiver(post_delete, sender=News)
@receiver(post_delete, sender=Product)
def remove_deleted_promote_entity_from_slideshow(sender, instance, **kwargs):
    type = ContentType.objects.get_for_model(sender)
    slideshow_s = SlideShow.objects.filter(content_type__pk=type.id, object_id=instance.id)
    if instance.is_promote :
        slideshow_s.delete()


@receiver(post_delete, sender=SlideShow)
def remove_promote_from_content(sender, instance, *args,**kwargs):
    content_type = ContentType.objects.get(app_label=instance.content_type.app_label, model=instance.content_type.model)
    content_type = content_type.model_class()
    object = content_type.objects.filter(id=instance.object_id)
    if object.exists() :
        object.update(
            is_promote=False,
        )

@receiver(post_save, sender=Organ)
def add_auto_id(sender, instance, *args,**kwargs):
    if not instance.slug or len(instance.slug) == 0 :
        instance.slug = str(instance.id)
        instance.save()
