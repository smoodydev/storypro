from django.shortcuts import render, get_object_or_404
from .models import Workspace, Book
from .forms import WorkspaceForm, ChapterForm, BookForm

# Create your views here.
def workspaces(request):
    workspaces = Workspace.objects.all()
    return render(request, "workspaces.html", {"workspaces":workspaces})

def createworkspace(request):
    form = WorkspaceForm()
    return render(request, "createworkspace.html", {"form":form})

def createbook(request):
    form = BookForm()
    return render(request, "createworkspace.html", {"form":form})

def createchapter(request):
    form = ChapterForm()
    return render(request, "createworkspace.html", {"form":form})

def workspace(request, id):
    content = get_object_or_404(Workspace, pk=id)
    books = Book.objects.filter(workspace=content.id)
    return render(request, "workspace.html", {"content":content, "books":books})
