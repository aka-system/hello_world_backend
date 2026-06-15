from django.urls import path
from .views import HelloWorldView

urlpatterns = [
    path('objects/', HelloWorldView.as_view())
]