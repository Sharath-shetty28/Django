from django.shortcuts import render, redirect, get_object_or_404
from .models import Note

def home(request):
    notes = Note.objects.all()
    return render(request, 'notes/home.html', {'notes': notes})

def add_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category = request.POST.get('category', '')
        Note.objects.create(title=title, content=content, category=category)
        return redirect('home')
    return render(request, 'notes/add_note.html')

def edit_note(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.category = request.POST.get('category', '')
        note.save()
        return redirect('home')
    return render(request, 'notes/edit_note.html', {'note': note})

def delete_note(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('home')
