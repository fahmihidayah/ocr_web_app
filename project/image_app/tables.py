from . import models
from django_tables2 import Table, TemplateColumn


class ImageDataTable(Table):

    detail = TemplateColumn(template_name='image_app/table/detail.html')
    delete = TemplateColumn(template_name='image_app/table/delete.html')
    retry = TemplateColumn(template_name='image_app/table/retry.html')

    class Meta:
        attrs = {"class": "table table-bordered table-responsive"}
        model = models.Image
        template_name = "django_tables2/bootstrap4.html"
        fields = ['pk', 'title', 'file', 'status', 'created_at', 'updated_at']
