from django.urls import path
from .views import task_1, task_2, task_3, task_4, task_5

urlpatterns = [
    path('', task_1, name = "task_1"),
    path('task_2/', task_2, name = "task_2"),
    path('task_3/', task_3, name = "task_3"),
    path('task_4/', task_4, name = "task_4"),
    path('task_5/', task_5, name = "task_5"),
]