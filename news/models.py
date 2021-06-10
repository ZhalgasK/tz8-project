from django.db import models

class News:
    title = models.CharField(max_length=200)
    text = models.TextField
    pusblished_date = models.DateField
    

# Create your models here.
