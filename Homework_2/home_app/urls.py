from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('task_1/', views.task_1, name="task_1"),
    path('task_2/', views.task_2, name="task_2"),
    path('task_3/', views.task_3, name="task_3"),
]
