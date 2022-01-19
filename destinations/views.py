from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Destination
from django.urls import reverse_lazy

# Create your views here.
class DestinationListView(ListView):
    template_name = "destinations/destination_list.html"
    model = Destination

class DestinationDetailView(DetailView):
    template_name = 'destinations/destination_detail.html'
    model = Destination

class DestinationCreateView(CreateView):
    template_name = 'destinations/destination_create.html'
    model = Destination
    fields = ['location', 'description', 'traveler', 'rating']


class DestinationUpdateView(UpdateView):
    template_name = 'destinations/destination_update.html'
    model = Destination
    fields = ['description', 'rating']
    success_url = reverse_lazy("destination_list")

class DestinationDeleteView(DeleteView):
    template_name = 'destinations/destination_delete.html'
    model = Destination
    success_url = reverse_lazy("destination_list")
