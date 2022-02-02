from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from django.urls import reverse_lazy

from books.models import Livros

class LivrosCreate(CreateView):
    model = Livros
    fields = '__all__'
   
class LivrosUpdate(UpdateView):
    model = Livros
    fields = ['titulo', 'editora', 'autor', 'resenha'] 

class LivrosDetailView(DetailView):
    model = Livros

class LivrosList(ListView):
    model = Livros   

class LivrosDelete(DeleteView):
    model = Livros
    success_url = reverse_lazy('books:list') 
