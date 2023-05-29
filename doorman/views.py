from django.shortcuts import get_object_or_404, render
from django.utils import timezone
# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import AccessEvent, UserProfile

class IndexView(generic.ListView):
    template_name = "doorman/index.html"
    context_object_name = "userprofile_list"
    model = UserProfile
    def get_queryset(self, *args, **kwargs):
        qs = UserProfile.objects.all()
        return qs

class HomePageView(TemplateView):
    template_name = 'doorman/home.html'

#    def home():
#        user_list = UserProfile.object
#        output = ", ".join([n.username for n in user_list])
#        return HttpResponse(output)
    


class UserProfileDetail(DetailView):

    model = UserProfile


class DoorAccessList(ListView):
    model = AccessEvent
    def get_queryset(self, *args, **kwargs):
        num = self.kwargs['pk']
        qs = AccessEvent.objects.all().filter(user_id = num)
        return qs

