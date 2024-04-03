from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from todo_list.models import Task, Tag


class IndexView(generic.ListView):
    # queryset = Task.objects.prefetch_related("tags")
    model = Task
    template_name = "todo_list/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:index")


class TaskUpdateView(generic.UpdateView):

    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:index")


class TaskDeleteView(generic.DeleteView):

    model = Task
    success_url = reverse_lazy("todo_list:index")


class TagsListView(generic.ListView):
    model = Tag
    template_name = "todo_list/tags_list.html"


class TagTaskListView(generic.ListView):

    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:index")

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        task.is_done = not task.is_done
        task.save()
        return HttpResponseRedirect(
            reverse("todo_list:index"))


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:index")


class TagUpdateView(generic.UpdateView):

    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:index")


class TagDeleteView(generic.DeleteView):

    model = Tag
    success_url = reverse_lazy("todo_list:index")

