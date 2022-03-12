def compressImage(list_of_photo, size=1000):
    from PIL import Image
    for photo in list_of_photo :
        if photo :
            image = Image.open(photo.path)
            if image.width > size :
                ratio = size / image.width
                image = image.resize( (int(image.width * ratio) ,int(image.height * ratio)) ) 
            image.save(photo.path , quality=70, optimize=True)

class ImageFieldForPanelAdmin():
    default_image_url = "https://www.yiwubazaar.com/resources/assets/images/default-product.jpg"
    
    def return_image_url(self, image_field):
        from robotic.settings import HOST_AND_DOMAIN
        if image_field.name is None or len(image_field.name) == 0 :
            return self.default_image_url # default image
        else :
            return f"{HOST_AND_DOMAIN}/media/{image_field}"

    def image_tag(self):
        from django.utils.html import mark_safe
        image_field = self.return_image_field()
        image_url = self.return_image_url(image_field)
        return mark_safe(f'<img src="{image_url}" width="150" height="150" />')
    image_tag.short_description = 'تصویر'
    image_tag.allow_tags = True