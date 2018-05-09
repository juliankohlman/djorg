from uuid import uuid4
from django.db import models

# Create your models here.
# TODO ADD bookmarked on  column (see Question model from django tutorial)
class Bookmark(models.Model):
  """ Bookmarks model """
  # created_at
  created_at = models.DateTimeField(auto_now_add=True)
  # last modified
  last_modified = models.DateTimeField(auto_now=True)
  # id -- pk
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  # url
  url = models.URLField('URL', unique=True)
  # name
  name = models.CharField(max_length=200)
  # tag/category --> each tag should be capitalized
  tag = models.TextField(blank=True)
  # description/notes
  description = models.TextField(blank=True)