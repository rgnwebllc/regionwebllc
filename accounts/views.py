from django.shortcuts import render
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import *
from django.contrib import messages
from django.http import HttpResponseForbidden
from core.decorators import subscription_required

def resize_image(image_file, size=(300, 300)):
    img = Image.open(image_file)
    img = img.convert('RGB')

    # Step 1: Crop to center square
    width, height = img.size
    min_dim = min(width, height)
    left = (width - min_dim) / 2
    top = (height - min_dim) / 2
    right = (width + min_dim) / 2
    bottom = (height + min_dim) / 2
    img = img.crop((left, top, right, bottom))

    # Step 2: Resize to desired dimensions
    img = img.resize(size, Image.Resampling.LANCZOS)

    # Step 3: Save into memory buffer
    buffer = BytesIO()
    img.save(fp=buffer, format='JPEG')
    buffer.seek(0)
    return InMemoryUploadedFile(
        buffer, None, image_file.name, 'image/jpeg', buffer.getbuffer().nbytes, None
    )

def forbidden(request):
    return render(request, 'accounts/forbidden.html', status=403)