from django.urls import path,include
from .views import HelloView


urlpatterns = [
    path('',HelloView.as_view(),name="Hello"), #to get all paths
]
