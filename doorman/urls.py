from django.urls import path

from .views import IndexView
from .views import HomePageView 
from .views import UserProfileDetail
from .views import DoorAccessList


#from . import views
app_name = "doorman"

urlpatterns = [
    # Landing page 
    path('', IndexView.as_view(), name="index"),
    
    # detail translates to detail.html
    #
    path("<int:pk>/",  IndexView.as_view(), name = "index"),
    
   
    # accessevent-list translates to accessevent_list.html
    #
    path("<int:pk>/dooraccess/", DoorAccessList.as_view(), name = "accessevent-list" ),

    # detail translates to detail.html
    #
    path("<int:pk>/userprofiledetail/", UserProfileDetail.as_view(), name = "detail"), 
]

