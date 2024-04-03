from django.urls import path

from todo_list.views import IndexView, TagsListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tags", TagsListView.as_view(), name="tags_list"),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delate/", TaskDeleteView.as_view(), name="task_delete"),

    ]

app_name = "todo_list"
