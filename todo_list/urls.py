from django.urls import path

from todo_list.views import IndexView, TagsListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TagTaskListView, \
    TagDeleteView, TagUpdateView, TagCreateView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tags", TagsListView.as_view(), name="tags_list"),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path(
        "tasks/<int:pk>/add/",
        TagTaskListView.as_view(),
        name="task-update-tag"
    ),
    path("tag/create/", TagCreateView.as_view(), name="tag_create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag_update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),

    ]

app_name = "todo_list"
