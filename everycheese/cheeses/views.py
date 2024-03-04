from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Cheese

class CheeseListView(ListView):
    model = Cheese

class CheeseDetailView(DetailView):
    model = Cheese

class CheeseCreateView(LoginRequiredMixin, CreateView):
    model = Cheese
    fields = [
        'name',
        'description',
        'firmness',
        'country_of_origin',
    ]

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class CheeseDeleteView(LoginRequiredMixin, DeleteView):
    model = Cheese
    success_url = reverse_lazy('cheeses:list')  
    template_name = 'cheeses/cheese_confirm_delete.html' 

    def get_object(self, queryset=None):
        cheese_id = self.kwargs.get('pk')
        return get_object_or_404(Cheese, pk=cheese_id)
