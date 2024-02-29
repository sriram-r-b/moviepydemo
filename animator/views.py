from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Welcome to animator")
from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm

def upload_images(request):
    if request.method == 'POST':
        images = []  # List to store images

        # Process initial image
        initial_form = ImageForm(request.POST, request.FILES)
        if initial_form.is_valid():
            image = initial_form.cleaned_data['image']
            images.append(Image(image=image))

        # Handle additional images (up to 5)
        for i in range(1, 5):
            additional_field_name = f'image_{i}'
            if additional_field_name in request.FILES:
                additional_form = ImageForm({'image': request.FILES[additional_field_name]})
                if additional_form.is_valid():
                    image = additional_form.cleaned_data['image']
                    images.append(Image(image=image))
                else:
                    # Handle invalid additional image form (optional)
                    pass

        # Save all valid images
        if images:
            Image.objects.bulk_create(images)
            return redirect('success_url')  # Redirect to success page

    else:
        initial_form = ImageForm()

    context = {'initial_form': initial_form}
    return render(request, 'upload_form.html', context)
