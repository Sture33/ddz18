from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, DetailView, UpdateView, DeleteView, ListView, CreateView

from app18.forms import CreateBook, CreateAuthor
from app18.models import Book, Author


# Create your views here.
class StartPage(TemplateView):
    template_name = 'index.html'

class BookList(ListView):
    template_name = 'book_list.html'
    model = Book
    context_object_name = 'book_list'
class AuthorList(ListView):
    template_name = 'author_list.html'
    model = Author
    context_object_name = 'author_list'

class BookCreate(CreateView):
    template_name = 'create_book.html'
    model = Book
    fields = ['title', 'author', 'genre', 'raiting']
    success_url = reverse_lazy('book_list')
class AuthorCreate(CreateView):
    template_name = 'create_author.html'
    model = Author
    fields = ['name', 'surname']
    success_url = reverse_lazy('author_list')

class BookDetail(DetailView):
    template_name = 'book_detail.html'
    model = Book
    context_object_name = 'book'
class AuthorDetail(DetailView):
    template_name = 'author_detail.html'
    model = Author
    context_object_name = 'author'

class BookUpdate(UpdateView):
    template_name = 'book_update.html'
    model = Book
    fields = ['title', 'author', 'genre', 'raiting']
    success_url = reverse_lazy('book_list')
class AuthorUpdate(UpdateView):
    template_name = 'author_update.html'
    model = Author
    fields = ['name', 'surname']
    success_url = reverse_lazy('author_list')

class BookDelete(DeleteView):
    template_name = 'book_delete.html'
    model = Book
    success_url = reverse_lazy('book_list')
class AuthorDelete(DeleteView):
    template_name = 'author_delete.html'
    model = Author
    success_url = reverse_lazy('author_list')