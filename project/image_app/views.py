from django.shortcuts import render
from django.views import generic
from . import tables, models, forms
from django_tables2 import SingleTableView
from django.shortcuts import redirect
from django.contrib import messages
from . import tasks
import jsonpickle
# Create your views here.

from django.urls import reverse, reverse_lazy


class ImageSingleTableView(SingleTableView):
    template_name = 'image_app/list_image_app.html'
    table_class = tables.ImageDataTable
    paginate_by = 10
    model = models.Image


class ImageCreateView(generic.CreateView):
    template_name = 'image_app/form_image_app.html'
    model = models.Image
    form_class = forms.ImageFileForm
    success_url = reverse_lazy('view_images')

    def get_success_url(self):
        messages.success(self.request, 'Image on Process')
        return super(ImageCreateView, self).get_success_url()


class ImageDetailView(generic.DetailView):
    template_name = 'image_app/detail_image_app.html'
    model = models.Image
    queryset = models.Image.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ImageDetailView, self).get_context_data(**kwargs)
        data: models.Image = context['object']
        context['result_report'] = jsonpickle.decode(data.text)
        return context


class ImageDeleteView(generic.DeleteView):
    template_name = 'image_app/delete_image_app.html'
    model = models.Image
    queryset = models.Image.objects.all()
    success_url = reverse_lazy('view_images')


    def get_context_data(self, **kwargs):
        print("test image")
        return super(ImageDeleteView, self).get_context_data(**kwargs)

    def get_success_url(self):
        messages.success(self.request, 'Image Deleted')
        return super(ImageDeleteView, self).get_success_url()


class RetryProcessView(generic.View):

    def post(self, request, *args, **kwargs):
        id = kwargs['pk']
        tasks.process_by_id(pk=id)
        messages.success(self.request, 'Image on Process')
        return redirect('view_images')