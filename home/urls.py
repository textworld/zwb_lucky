from django.urls import path, include
from .views import get_make_lucky

urlpatterns = [
    path('make_lucky/', get_make_lucky),
]
