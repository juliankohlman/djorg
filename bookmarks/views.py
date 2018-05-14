from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Bookmark


class BookmarkForm(forms.ModelForm):
  class Meta:
    model = Bookmark
    fields = ['name', 'url', 'tag', 'description']

def bookmark_list(request, template_name='bookmarks/bookmark_list.html'):
  bookmarks = Bookmark.objects.all()
  data = {}
  data['object_list'] = bookmarks
  return render(request, template_name, data)

def bookmark_create(request, template_name='bookmarks/bookmark_form.html'):
  # or None ??? 
  form = BookmarkForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('bookmarks:bookmark_list')
  return render(request, template_name, {'form': form})

def bookmark_update(request, pk, template_name='bookmarks/bookmark_edit.html'):
  bookmark = get_object_or_404(Bookmark, pk=pk)
  form = BookmarkForm(request.POST or None, instance = bookmark)
  if form.is_valid():
    form.save()
    return redirect('bookmarks:bookmark_list')
  return render(request, template_name, {'form':form})

def bookmark_delete(request, pk, template_name='bookmarks/bookmark_confirm_delete.html'):
  bookmark = get_object_or_404(Bookmark, pk=pk)
  if request.method == 'POST':
    bookmark.delete()
    return redirect('bookmarks:bookmark_list')
  return render(request, template_name, {'object': bookmark})
















# class bookmarks(View):
#   template_name = 'bookmarks/index.html'

#   def get(self, request):
#     # context = {}
#     # context['bookmarks'] = Bookmark.objects.all()
#     # context['personal_bookmarks'] = PersonalBookmark.objects.all()
#     # context['form'] = BookmarkForm()
#     bookmark_list = []
#     form_user = BookmarkForm()
#     bookmarks = Bookmark.objects.all()

#     for bookmark in bookmarks:
#       bookmark_list.append({'Name': bookmark.name, 'Url': bookmark.url})

#     return render(request, self.template_name, {
#       'bookmark_list': bookmark_list,
#       'form_user': form_user
#     })

#   def post(self, request):
#     form_user = BookmarkForm(request.POST)
#     if form_user.is_valid():
#         form_user.save()
#         return HttpResponseRedirect('/bookmarks')


# def index(request):
#   # TODO: business logic, get data, etc...
#   context = {}
#   context['bookmarks'] = Bookmark.objects.all()
#   context['form'] = BookmarkForm()
#   return render(request, 'bookmarks/index.html', context)
