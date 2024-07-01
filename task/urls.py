from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView, TaskListUserView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<str:user_id>/', TaskListUserView.as_view(), name='task_list_user'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name='task_edit'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('detail/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
]