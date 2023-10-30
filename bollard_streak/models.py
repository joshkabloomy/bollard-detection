from django.db import models

class CountryStreak(models.Model):
    countries = models.CharField(max_length=200)
    image_link = models.CharField(max_length=200)
    class Meta: # define what the model name is
        db_table = 'country_table'
