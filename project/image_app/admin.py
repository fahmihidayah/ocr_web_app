from django.contrib import admin
from . import models, forms
# Register your models here.


@admin.register(models.Image)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'file', 'created_at', 'updated_at']
    search_fields = ['title', 'file']
    form = forms.ImageForm
    
