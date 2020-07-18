from django.urls import path
from .views import blogsList


urlpatterns = [
    path('list/', blogsList, name='blogs'),
]