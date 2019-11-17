from django.shortcuts import render, get_object_or_404, redirect
from .models import Workspace, Book, Topic, Entry
from .forms import WorkspaceForm, ChapterForm, BookForm

# Create your views here.
def workspaces(request):
    workspaces = Workspace.objects.all()
    return render(request, "workspaces.html", {"workspaces":workspaces})

def createworkspace(request):
    if request.method == "POST":
        form = WorkspaceForm(request.POST)
        ws = form.save(commit=False)
        ws.publisheradmin = request.user
        ws.save()
        return redirect("workspaces")
        
    form = WorkspaceForm()    
    return render(request, "createworkspace.html", {"form":form})

def createbook(request, id):
    print(request.method)
    if request.method == "POST":
        form = BookForm(request.POST)
        ws = form.save(commit=False)
        ws.workspace = Workspace(pk=id)
        ws.save()
        return redirect("workspaces")
    
    form = BookForm()
    return render(request, "createworkspace.html", {"form":form})

def createchapter(request):
    form = ChapterForm()
    return render(request, "createworkspace.html", {"form":form})

def workspace(request, id):
    if request.method =="POST":
        ws = get_object_or_404(Workspace, pk=id)
        ws.name = request.POST.get('name')
        ws.blurb = request.POST.get('blurb')
        ws.save()
    content = get_object_or_404(Workspace, pk=id)
    wsform = WorkspaceForm(instance=content)
    form = BookForm()
    return render(request, "workspace.html", {"content":content, "form": form, "wsform": wsform})

def book(request, ws, id):
    content = get_object_or_404(Workspace, pk=ws)
    book = get_object_or_404(Book, pk=id)
    return render(request, "book.html", {"content":content, "book":book})

def chapter(request, ws, id, ch):
    if request.method =="POST":
        print("Post")
        chapter = request.form(commit=False)
        chapter.book = get_object_or_404(Book, pk=id)
        chapter.save()
        print(chapter)
    topics = Topic.objects.all()
    return render(request, "chapter.html", {"topics":topics})
