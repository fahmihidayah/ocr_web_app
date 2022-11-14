from django.db import models

# Create your models here.

class Image(models.Model):
    file: models.ImageField = models.ImageField(upload_to='images')

    title: models.CharField = models.CharField(max_length=100, null=True, default='')

    text: models.TextField = models.TextField(max_length=2000, null=True, default='')

    result: models.CharField = models.CharField(max_length=3000, null=True, default='')

    status: models.IntegerField = models.IntegerField(default=0)

    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True, editable=False)

    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title