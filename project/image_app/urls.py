from django.urls import path
from . import views

urlpatterns = [
    path('images', views.ImageSingleTableView.as_view(), name='view_images'),
    path('images/create', views.ImageCreateView.as_view(), name='view_create_images'),
    path('images/<int:pk>', views.ImageDetailView.as_view(), name='view_detail_images'),
    path('image/process/<int:pk>', views.RetryProcessView.as_view(), name='view_retry_process'),
]