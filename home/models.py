from django.db import models

# Create your models here.
class Member(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=2000)
    def __str__(self):
        return self.name