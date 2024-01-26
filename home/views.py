from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.files.storage import default_storage
from .models import ClassifiedImage, BirdSpecies
from .ml_model import predictClassLabel
from django.http import HttpResponseServerError
import logging
from datetime import datetime

# Create a logger instance
logger = logging.getLogger(__name__)

def abhishek(request):
    return render(request, 'index.html')

def renderHome(request):
    predicted_species = None
    image_url = None

    try:
        if request.method == 'POST':
            submitted_image = request.FILES.get('image')

            if submitted_image:
                # Save the image directly to the 'classified_images/' directory
                image_path = default_storage.save(f'classified_images/{submitted_image.name}', submitted_image)

                # Call your function to predict the class label
                predicted_species_name = predictClassLabel(submitted_image)

                # Fetch or create the BirdSpecies instance based on the predicted species name
                predicted_species, _ = BirdSpecies.objects.get_or_create(common_name=predicted_species_name)

                # Save the classified image to the database
                classified_image = ClassifiedImage.objects.create(
                    image=image_path,
                    predicted_species=predicted_species
                )

                # Generate the correct image URL using the 'url' template tag
                image_url = f'{settings.MEDIA_URL}{image_path}'

                # Redirect to the species_detail page with the predicted_species ID
                return redirect('species_detail', species_id=predicted_species.id)

    except Exception as e:
        # Log the exception or handle it appropriately
        logger.error(f"Error during image processing: {e}", exc_info=True)
        return HttpResponseServerError("Internal Server Error")

    context = {
        'predicted_species': predicted_species,
        'image_url': image_url,
    }
    return render(request, 'home.html', context)

# The rest of your views remain unchanged...


def add_bird_species(request):
    if request.method == 'POST':
        # Get the values from the POST request
        status_code = request.POST.get('status_code')
        common_name = request.POST.get('common_name')
        scientific_name = request.POST.get('scientific_name')
        bird_description = request.POST.get('bird_description')
        current_status = request.POST.get('current_status')

        # Check if status_code is not None before proceeding
        if status_code is not None:
            # Create a BirdSpecies instance
            BirdSpecies.objects.create(
                status_code=status_code,
                common_name=common_name,
                scientific_name=scientific_name,
                bird_description=bird_description,
                current_status=current_status,
            )

    return render(request, 'add_bird_species.html')

def species_detail(request, species_id):
    species = get_object_or_404(BirdSpecies, pk=species_id)
    classified_image = ClassifiedImage.objects.filter(predicted_species=species).first()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
    # Pass the necessary data to the template
    context = {
        'species': species,
        'classified_image': classified_image,
        'image_url': classified_image.image.url if classified_image else None,
        'current_time': current_time,
    }

    return render(request, 'species_detail.html', context)
