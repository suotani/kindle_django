from django import forms
from django.forms import ModelForm, CharField
from .models import Note

class NoteForm(ModelForm):
  def __init__(self, *args, **kwargs):
    super(NoteForm, self).__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs["class"] = "form-control"

  class Meta:
    model = Note
    fields = ['title', 'score', 'text']