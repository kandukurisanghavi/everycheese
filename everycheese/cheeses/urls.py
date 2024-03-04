from django.urls import path
from .views import CheeseListView, CheeseCreateView, CheeseDetailView, CheeseDeleteView

app_name = "cheeses"

urlpatterns = [
    path(route='', view=CheeseListView.as_view(), name='list'),
    path(route='add/', view=CheeseCreateView.as_view(), name='add'),
    path(route='<slug:slug>/', view=CheeseDetailView.as_view(), name='detail'),
    path(route='<int:pk>/delete/', view=CheeseDeleteView.as_view(), name='delete_cheese'),
]
