from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from .models import Bookmark
from .forms import BookmarkForm
# from django.urls import reverse_lazy
class bookmarks(View):
  template_name = 'bookmarks/index.html'

  def get(self, request):
    bookmark_list = []
    form_user = BookmarkForm()
    bookmarks = Bookmark.objects.all()

    for bookmark in bookmarks:
      bookmark_list.append({'Name': bookmark.name, 'Url': bookmark.url})

    return render(request, self.template_name, {
      'title': 'Bookmark List',
      'bookmark_list': bookmark_list,
      'form_user': form_user
    })
  
  def post(self, request):
    form_user = BookmarkForm(request.POST)
    if form_user.is_valid():
        form_user.save()
        return HttpResponseRedirect('/bookmarks')



def index(request):
  # if request.method == 'GET':
  #   form = BookmarkForm()
  context = {}
  # TODO: business logic, get data, etc...
  context['bookmarks'] = Bookmark.objects.all()
  return render(request, 'bookmarks/index.html', context)
