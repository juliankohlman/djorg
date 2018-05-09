from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Bookmark

def index(request):
  context = {}
  # TODO: business logic, get data, etc...
  context['bookmarks'] = Bookmark.objects.all()
  return render(request, 'bookmarks/index.html', context)

def bookmark_create(request):
  return render(request, 'bookmarks/create')
  
# Django form class(include model within the index)
class BookmarkCreate(CreateView):
  model = Bookmark
  fields = ['url', 'name', 'tag', 'description']
  initial={'name': 'DevDocs',}
  success_url = reverse_lazy('index')

class BookmarkUpdate(UpdateView):
  model = Bookmark
  fields = ['url', 'name', 'tag', 'description']

class BookmarkDelete(DeleteView):
  model = Bookmark
  success_url = reverse_lazy('bookmarks')
