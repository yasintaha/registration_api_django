from django.db import models

# Create your models here.
class Register_model(models.Model):
    Fname = models.CharField(max_length=243)
    lname = models.CharField(max_length=243)
    email = models.EmailField(max_length=243,unique=True)
    Address = models.CharField(max_length=243)
    