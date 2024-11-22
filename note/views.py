from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Note

# Create your views here.

def index(request):
  context = {
    'notes_list' : Note.objects.all()
  }
  return render(request, "note/index.html", context)

def add(request):
  return render(request, "note/form.html")

def save(request):
  catat =  Note(
    makul=request.POST['makul'], 
    deskripsi=request.POST['deskripsi'],
    tenggat=request.POST['tenggat']
  )
  catat.save()
  return HttpResponseRedirect(reverse('note.index'))
  
def delete(request, notes_id):
    catat = get_object_or_404(Note, pk=notes_id)
    catat.delete()
    return HttpResponseRedirect(reverse('note.index'))

def edit(request, notes_id):
  catat = get_object_or_404(Note, pk=notes_id)
  tenggat = catat.tenggat.date()
  context = {
      'id' : notes_id,
      'makul' : catat.makul,
      'deskripsi' : catat.deskripsi,
      'tenggat' : tenggat.strftime("%Y-%m-%d")
  }
  return render(request, 'note/form_edit.html', context)

def update(request, notes_id):
  catat = get_object_or_404(Note, pk=notes_id)
  catat.makul = request.POST['makul']
  catat.deskripsi = request.POST['deskripsi']
  catat.tenggat = request.POST['tenggat']
  catat.save()
    
  return HttpResponseRedirect(reverse('note.index'))
