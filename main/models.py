from django.db import models

# Create your models here.
class Movie(models.Model): # we are creating a table named Movie
    #fields for the Movie table
    name = models.CharField(max_length=350, unique=True)
    director= models.CharField(max_length=350, null=True)
    cast= models.CharField(max_length=1000, null=True)
    description= models.TextField(max_length=5000)
    release_date= models.DateField()
    averageRating = models.FloatField(default=0)
    image = models.URLField(default=None, null=True)


    def __str__(self): #function called string returns whatever you want in the string version in django-admin
        return self.name

    def __unicode__(self):
        return self.name

        #now after creating a table we need to register it to admin.py
        #and after making any changes to database we need to run migrations

class Review(models.Model): # we are creating a table named Movie
    #fields for the Movie table
    name = models.CharField(max_length=350)
    rating = models.FloatField(default=0)
    review = models.TextField()
    date = models.DateField()
    user = models.CharField(max_length=100)


    def __str__(self): #function called string returns whatever you want in the string version in django-admin
        return self.name

    def __unicode__(self):
        return self.name