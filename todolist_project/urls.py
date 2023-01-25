from django.urls import path
from .views import (Index,
                    IndexCreateView,
                    IndexUpdateView,
                    IndexDeleteView,
                    TagsListView,
                    TagsCreateView,
                    TagsUpdateView,
                    TagsDeleteView)

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("task/create/", IndexCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/update/", IndexUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delete/", IndexDeleteView.as_view(), name="task_delete"),
    path("tags/", TagsListView.as_view(), name="tag_list"),
    path("tags/create/", TagsCreateView.as_view(), name="tag_create"),
    path("tags/<int:pk>/update/", TagsUpdateView.as_view(), name="tag_update"),
    path("tags/<int:pk>/delete/", TagsDeleteView.as_view(), name="tag_delete"),
]

app_name = "todolist_project"
