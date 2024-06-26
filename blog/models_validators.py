valid_extensions = {
    # "zip" : [
    #     ".rar",
    #     ".zip",
    #     ".tar",
    # ] ,
    "video" : [
        ".mp4",
        ".mkv",
        ".mpeg",
        ".mpg",
        ".mov",
    ] ,
    "img" : [
        ".jpg",
        ".png",
        ".jpeg",
        ".jfif",
        ".webp",
        ".apng",
        ".avif",
        ".gif",
        ".pjpeg",
        ".pjp",
        ".svg",
        ".webp",
        ".tif",
        ".tiff",
        ".bmp"
    ] ,
    # "pdf" :[
    #     ".pdf",
    # ] ,
}

# def validate_img_extension(value):
#     import os
#     from django.core.exceptions import ValidationError
#     ext = os.path.splitext(value.name)[1]
#     if not ext.lower() in valid_extensions["img"]:
#         raise ValidationError(f'unsupported file extension. should be one of {valid_extensions["img"]}')

# def validate_video_extension(value):
#     import os
#     from django.core.exceptions import ValidationError
#     ext = os.path.splitext(value.name)[1]
#     if not ext.lower() in valid_extensions["video"]:
#         raise ValidationError(f'unsupported file extension. should be one of {valid_extensions["video"]}')

# def validate_zip_extension(value):
#     import os
#     from django.core.exceptions import ValidationError
#     ext = os.path.splitext(value.name)[1]
#     if not ext.lower() in valid_extensions["zip"]:
#         raise ValidationError('Unsupported file extension.')

# def validate_pdf_extension(value):
#     import os
#     from django.core.exceptions import ValidationError
#     ext = os.path.splitext(value.name)[1]
#     if not ext.lower() in valid_extensions["pdf"]:
#         raise ValidationError('Unsupported file extension.')

def validate_video_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    if ext.lower() not in valid_extensions["video"] :
        raise ValidationError(f'unsupported file extension.\
            your file extension should one of {valid_extensions["video"]}')

def validate_media_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    if not ext.lower() in valid_extensions["img"] and ext.lower() not in valid_extensions["video"] :
        raise ValidationError(f'unsupported file extension.\
            your file extension should one of {valid_extensions["img"]}\
            or {valid_extensions["video"]}')
            
def validate_tag(value):
    import re
    from django.core.exceptions import ValidationError
    if re.match("^[\sA-Za-z0-9_-]*$", value):
        return True
    else :
        raise ValidationError('string only contains letters, numbers, underscores, dash and spaces')

def validate_slug(value):
    import re
    from django.core.exceptions import ValidationError
    if re.match("^[A-Za-z0-9_-]*$", value):
        return True
    else :
        raise ValidationError('string only contains letters, numbers, underscores and dash')