# everycheese/cheeses/urls.py
from django.urls import path
from . import views

app_name = "cheeses"

urlpatterns = [
    # URL pattern for CheeseListView
    path(
        route='',
        view=views.CheeseListView.as_view(),
        name='list'
    ),
    # URL pattern for CheeseCreateView
    path(
        route='add/',
        view=views.CheeseCreateView.as_view(),
        name='add'
    ),
    # URL pattern for CheeseDetailView
    path(
        route='<slug:slug>/',
        view=views.CheeseDetailView.as_view(),
        name='detail'
    ),
]
