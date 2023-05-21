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
    context_object_name = "latest_AccessEvent_list"
    model = AccessEvent
#    def get_queryset(self):
#        """Return the last five published questions."""
#        return AccessEvent.objects.order_by("-event_date")[:5]

'''
class UserProfileListView(ListView):
    model = UserProfile
    pagenate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
'''


class HomePageView(TemplateView):
    template_name = 'doorman/home.html'

'''
class DetailView(generic.DetailView):
    model = UserProfile
    template_name = "doorman/detail.html"
'''

class UserProfileDetail(DetailView):

    model = UserProfile


class DoorAccessList(ListView):
    model = AccessEvent
    def get_queryset(self, *args, **kwargs):
        num = self.kwargs['pk']
        qs = AccessEvent.objects.all().filter(doorUser_id = num)
        return qs

