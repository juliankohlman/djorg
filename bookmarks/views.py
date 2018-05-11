from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from .models import Bookmark, PersonalBookmark
from .forms import BookmarkForm


class bookmarks(View):
  template_name = 'bookmarks/index.html'

  def get(self, request):
    # context = {}
    # context['bookmarks'] = Bookmark.objects.all()
    # context['personal_bookmarks'] = PersonalBookmark.objects.all()
    # context['form'] = BookmarkForm()
    bookmark_list = []
    form_user = BookmarkForm()
    bookmarks = Bookmark.objects.all()

    for bookmark in bookmarks:
      bookmark_list.append({'Name': bookmark.name, 'Url': bookmark.url})

    return render(request, self.template_name, {
      'bookmark_list': bookmark_list,
      'form_user': form_user
    })

  def post(self, request):
    form_user = BookmarkForm(request.POST)
    if form_user.is_valid():
        form_user.save()
        return HttpResponseRedirect('/bookmarks')


def index(request):
  # TODO: business logic, get data, etc...
  context = {}
  context['bookmarks'] = Bookmark.objects.all()
  context['form'] = BookmarkForm()
  return render(request, 'bookmarks/index.html', context)
