from django.db import models



class Information(models.Model):
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    address = models.TextField()


