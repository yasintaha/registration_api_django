from django.db import models

# Create your models here.
class file_model(models.Model):
    file = models.FileField(blank=False,null=False)
    key = models.CharField(max_length=20,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)