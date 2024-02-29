from django.db import models


class Image(models.Model):
    # image_path = models.CharField(max_length=200)
    # pub_date = models.DateTimeField("date published")
    image = models.ImageField(upload_to='images/')
