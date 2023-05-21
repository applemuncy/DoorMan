from django.urls import path

from .views import IndexView
from .views import HomePageView 
from .views import UserProfileDetail
from .views import DoorAccessList
app_name = "doorman"

urlpatterns = [
    
    path('', HomePageView.as_view(), name='home'),
    
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

