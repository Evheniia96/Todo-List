from django.shortcuts import render
from django.views import generic

from todo_list.models import Task


class IndexView(generic.ListView):
    queryset = Task.objects.prefetch_related("tags")
    template_name = "todo_list/index.html"
