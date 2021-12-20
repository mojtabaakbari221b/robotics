def image_validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [
        '.jpg',
        '.png' ,
        '.jpeg' ,
        '.jfif' ,
        '.webp' ,
    ]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def file_validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [
        '.zip',
        '.rar' ,
        '.pdf' ,
    ]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')