from django.urls import path
from .views import Index, IndexCreateView, IndexUpdateView, IndexDeleteView

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("task/create/", IndexCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/update/", IndexUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delete/", IndexDeleteView.as_view(), name="task_delete")
]

app_name = "todolist_project"
