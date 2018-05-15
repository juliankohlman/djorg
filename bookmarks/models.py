from django.db import models
from uuid import uuid4
from django.urls import reverse

# Create your models here.
# TODO ADD bookmarked on column (see Question model from django tutorial)
class Bookmark(models.Model):
  """ Bookmarks model """
  id = models.IntegerField(primary_key=True, serialize=True, editable=False)
  created_at = models.DateTimeField(auto_now_add=True)
  description = models.TextField(blank=True)
  last_modified = models.DateTimeField(auto_now=True)
  name = models.CharField(max_length=200)
  tag = models.TextField(blank=True)
  url = models.URLField('URL', unique=True)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('bookmark_edit', kwargs={'pk' : self.pk})
    


