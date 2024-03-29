# models.py

from django.db import models
from django.urls import reverse
from django.utils import timezone


class BirdSpecies(models.Model):
    STATUS_CHOICES = [
        ('LC', 'Least Concern'),
        ('NT', 'Near Threatened'),
        ('VU', 'Vulnerable'),
        ('EN', 'Endangered'),
        ('CR', 'Critically Endangered'),
    ]
    My_choice =[
        ('LC', 'Least Concern'),
        ('NT', 'Near Threatened'),
        ('VU', 'Vulnerable'),
        ('EN', 'Endangered'),
        ('CR', 'Critically Endangered'),
    ]
    

    status_code = models.CharField(max_length=2, choices=STATUS_CHOICES,blank=True,null=True)
    common_name = models.CharField(max_length=100, unique=True)
    scientific_name = models.CharField(max_length=100,default='default_value',null=True)
    bird_description = models.TextField(blank=True, null=True,default='default_value')
    current_status = models.CharField(max_length=10,choices= My_choice)

    def __str__(self):
        return self.common_name

class ClassifiedImage(models.Model):
    image = models.ImageField(upload_to='classified_images/')
    predicted_species = models.ForeignKey(BirdSpecies, on_delete=models.CASCADE, null=True)
    classified_at = models.DateTimeField(auto_now_add=True)
    confidence = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.predicted_species.common_name} - {self.classified_at}'

    def get_absolute_url(self):
        return reverse('classified-image-detail', args=[str(self.id)])
