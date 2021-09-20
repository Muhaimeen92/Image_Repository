from .models import Image
from ImageRepository.settings import MEDIA_URL, MEDIA_FOLDER

def handle_uploaded_file(image_files, file_name):
    with open(MEDIA_URL.lstrip("/") + MEDIA_FOLDER + file_name, 'wb+') as destination:
        for chunk in image_files.chunks():
            destination.write(chunk)

def upload_new_image(request, file_name):
    new_image = Image()
    new_image.image = MEDIA_FOLDER + file_name
    new_image.user = request.user
    new_image.file_name = file_name
    new_image.save()