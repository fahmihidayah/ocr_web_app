from . import models
from django import forms
from . import tasks


class ImageForm(forms.ModelForm):

    class Meta:
        model = models.Image
        fields = ['title', 'file', 'text', 'result']


class ImageFileForm(forms.ModelForm):

    def save(self, commit=True):
        object = super(ImageFileForm, self).save(commit=commit)
        if commit:
            tasks.process_by_id(pk=object.pk)
        return object

    class Meta:
        model = models.Image
        fields = ['file']