from django.shortcuts import render
from django.views import generic

from todo_list.models import Task, Tag


class IndexView(generic.ListView):
    queryset = Task.objects.prefetch_related("tags")
    template_name = "todo_list/index.html"


class TagsListView(generic.ListView):
    model = Tag
    template_name = "todo_list/tags_list.html"
