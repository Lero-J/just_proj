from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('taskinfo/<int:task_id>', views.task_detail, name='task_detail'),
    path('add', views.add_task, name='add_task'),
    path('mark/<int:task_id>', views.mark_task, name='mark_task'),
    path('delete/<int:task_id>', views.delete_task, name='delete_task'),
]