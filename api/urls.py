from django.urls import path,include
from . import views
from .views import HelloView


urlpatterns = [
    path('',HelloView.as_view(),name="Hello"), #to get all paths
    path('ram/',view=views.RAMView.as_view(),name="Ram-details"), # to get ram details

]   
