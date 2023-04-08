from django.urls import path,include
from . import views
from .views import HelloView


urlpatterns = [
    path('',HelloView.as_view(),name="Hello"), #to get all paths
    path('ram/',view=views.RAMView.as_view(),name="Ram-details"), # to get ram details
    path('sys/',view=views.SysView.as_view(),name="Sys-details"), # to get system details
    path('process/',view=views.ProcessView.as_view(),name="Process-details"), # to get process details
]   
