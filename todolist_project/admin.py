from django.contrib import admin

from todolist_project.models import Tag, Task


admin.site.register(Task)
admin.site.register(Tag)
