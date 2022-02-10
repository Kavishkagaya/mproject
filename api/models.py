from pyexpat import model
from django.db import models

# Create your models here.
class Subjects(models.Model):
    title = models.CharField(max_length=50)
    imgurl = models.TextField()

class Papers(models.Model):
    title = models.CharField(max_length=50)
    imgurl = models.TextField()
    fileurl = models.TextField()
    subject = models.CharField(max_length=50)