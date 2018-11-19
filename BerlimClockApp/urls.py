from django.urls import path
from rest_framework.urlpatterns import apply_suffix_patterns 

from . import views

urlpatterns = [
    path("", views.GPIOPinView.as_view())
]
