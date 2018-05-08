from uuid import uuid4
from django.db import models

# Create your models here.
class Bookmark(models.Model):
  """ Bookmarks model """
  # id -- pk
  id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  # url
  url = models.URLField('URL', unique=True)
  # name
  name = models.CharField(max_length=200)
  # tag 

  # description/notes
  description = models.TextField(blank=True)