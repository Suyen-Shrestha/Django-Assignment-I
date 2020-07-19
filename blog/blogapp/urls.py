from django.urls import path
from .views import blogsList, blogDetail


urlpatterns = [
    path('list/', blogsList, name='blogs'),
    path('detail/<int:blog_id>', blogDetail, name='blog_detail'),
]