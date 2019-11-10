from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Workspace(models.Model):
    publisheradmin = models.ForeignKey(User)
    name = models.CharField(max_length=140, blank=False)
    blurb = models.TextField(max_length=140, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    workspace = models.ForeignKey(Workspace, related_name="books")
    title = models.CharField(max_length=200, blank=False)
    blurb = models.TextField(max_length=140, blank=True)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    book = models.ForeignKey(Book, related_name="chapters")
    chap_num = models.IntegerField(blank=True)
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        string = ""
        if self.chap_num:
            string = string+str(self.chap_num)
        if self.title:
            string = string+self.title
        if string != "":
            return string
        else:
            return "Un-Named Chapter in "+ self.book

class Topic(models.Model):
    workspace = models.ForeignKey(Workspace, related_name="topic")
    shorthand = models.CharField(max_length=3, blank=True)
    name = models.CharField(max_length=140, blank=False)
    blurb = models.TextField(max_length=140, blank=True)

    def __str__(self):
        return self.name

class Entry(models.Model):
    topic = models.ForeignKey(Workspace, related_name="entries")
    name = models.CharField(max_length=140, blank=False)
    blurb = models.TextField(max_length=140, blank=True)

    def __str__(self):
        return self.name