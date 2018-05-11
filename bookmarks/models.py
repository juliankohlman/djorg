from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# TODO ADD bookmarked on  column (see Question model from django tutorial)
class Bookmark(models.Model):
  """ Bookmarks model """
  created_at = models.DateTimeField(auto_now_add=True)
  description = models.TextField(blank=True)
  last_modified = models.DateTimeField(auto_now=True)
  name = models.CharField(max_length=200)
  tag = models.TextField(blank=True)
  url = models.URLField('URL', unique=True)

  def __str__(self):
    return self.name

class PersonalBookmark(Bookmark):
  user = models.ForeignKey(User, on_delete=models.CASCADE)


