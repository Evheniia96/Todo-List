from django.urls import path

from todo_list.views import IndexView, TagsListView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tags", TagsListView.as_view(), name="tags_list"),
    ]

app_name = "todo_list"
