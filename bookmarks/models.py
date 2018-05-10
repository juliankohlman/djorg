from uuid import uuid4
# from django.forms import ModelForm
from django.db import models

# Create your models here.
# TODO ADD bookmarked on  column (see Question model from django tutorial)
class Bookmark(models.Model):
  """ Bookmarks model """
  # id -- pk
  # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  # created_at
  created_at = models.DateTimeField(auto_now_add=True)
  # description/notes
  description = models.TextField(blank=True)
  # last modified
  last_modified = models.DateTimeField(auto_now=True)
  # name
  name = models.CharField(max_length=200)
  # tag/category --> each tag should be capitalized
  tag = models.TextField(blank=True)
  # url
  url = models.URLField('URL', unique=True)

# Bookmark ModelForm
# class BookmarkForm(ModelForm):
#   # Todo add validation
#   class Meta:
#     model = Bookmark
#     fields = ['url', 'name', 'tag', 'description']

