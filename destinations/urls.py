from django.urls import path
from django.views.generic.edit import CreateView 
from .views import DestinationDeleteView, DestinationDetailView, DestinationListView, DestinationCreateView, DestinationUpdateView

urlpatterns = [
    path('', DestinationListView.as_view(), name='destination_list'),
    path("<int:pk>/", DestinationDetailView.as_view(), name='destination_detail'),
    path("create/", DestinationCreateView.as_view(), name="destination_create"),
    path('<int:pk>/update/', DestinationUpdateView.as_view(), name='destination_update'),
    path('<int:pk>/delete/', DestinationDeleteView.as_view(), name='destination_delete'),
]