from django.db import models
from django.utils import timezone

# Create your models here.

class Countries(models.Model):
  Country_Choices = [
    ('IND', 'INDIA'),
    ('JAP', 'JAPAN'),
    ('AUS', 'Australia'),
    ('ENG', 'England'),
    ('USA', 'United States of America'),
  ]

  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='images/')
  date_added = models.DateTimeField(default=timezone.now)
  country = models.CharField(max_length=3, choices=Country_Choices, default='IND')
  capital = models.CharField(max_length=100)
  description = models.TextField(default='')

  def __str__(self):
    return self.name