from django import forms
from .models import Workspace, Book, Chapter

class WorkspaceForm(forms.ModelForm):
    class Meta:
        model = Workspace
        fields = ('name', 'blurb')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'blurb')

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ('chap_num', 'title', 'content')

