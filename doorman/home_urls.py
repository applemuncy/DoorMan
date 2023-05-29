from django.urls import path

from .views import HomePageView 


#from . import views

urlpatterns = [
    # Landing page 
    path('', HomePageView.as_view(), name="home"),
    
]

