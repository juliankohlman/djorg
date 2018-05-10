from django import forms
from .models import Bookmark

class BookmarkForm(forms.ModelForm):
  # Todo add validation
  class Meta:
    model = Bookmark
    fields = ['url', 'name', 'tag', 'description']
