from django.conf.urls import url
from .views import workspaces, createworkspace, createbook, createchapter, workspace, book, chapter

urlpatterns = [
    url(r'^$', workspaces, name="workspaces"),
    url(r'^createworkspace', createworkspace, name="createworkspace"),
    url(r'^createbook', createbook, name="createbook"),
    url(r'^createchapter', createchapter, name="createchapter"),
    url(r'^workspace/(\d+)/$', workspace, name="workspace"),
    url(r'^workspace/(\d+)/(\d+)/$', book, name="book"),
    url(r'^chapter', chapter, name="chapter"),


]