from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('info/<int:info_id>/', categories)
]