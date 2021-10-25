from django.shortcuts import get_object_or_404, render, redirect
from .models import Note
from .forms import NoteForm

# Create your views here.
def index(request):
  note_list = Note.objects.all()
  return render(request, "note/index.html", {'note_list': note_list})

def show(request, pk):
  note = get_object_or_404(Note, pk=pk)
  return render(request, "note/show.html", {'note': note})

def create(request):
  if request.method == "POST":
    form = NoteForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('note_list')
  else:
    form = NoteForm

  return render(request, "note/create.html", {'form': form})

def update(request, pk):
  note = Note.objects.get(pk=pk)
  if request.method == "POST":
    form = NoteForm(request.POST, instance=note)
    if form.is_valid():
      form.save()
      return redirect('note_detail',pk=pk)
  else:
    form = NoteForm(instance = note)

  return render(request, "note/update.html", {'form': form, 'pk': pk})

def delete(request, pk):
  note = get_object_or_404(Note, pk=pk)
  note.delete()
  return redirect('note_list')
