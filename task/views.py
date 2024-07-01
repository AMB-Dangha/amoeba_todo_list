from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.functions import TruncDate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from user.models import User
from .models import Task
from django.urls import reverse_lazy
from .forms import TaskForm
from django.db.models.functions import ExtractWeekDay
from django.utils import timezone


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'

    def get_queryset(self):
        return Task.objects.annotate(
            weekday=ExtractWeekDay('created_at')).exclude(weekday__in=[6, 7]).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dates = Task.objects.annotate(date=TruncDate('created_at')).values('date').distinct()
        context['tasks_by_date'] = {timezone.localdate().today() - timezone.timedelta(days=i): None for i in range(2)}
        tasks_by_date = {date['date']: Task.objects.filter(created_at__date=date['date']) for date in dates}
        context['tasks_by_date'].update(tasks_by_date)

        return context


class TaskListUserView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list_user.html'
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Task.objects.filter(user_id=user_id).annotate(
            weekday=ExtractWeekDay('created_at')).exclude(weekday__in=[6, 7]).order_by('-created_at')

    def get_context_data(self, **kwargs):
        user_id = self.kwargs['user_id']
        context = super().get_context_data(**kwargs)
        dates = Task.objects.filter(user_id=user_id).annotate(date=TruncDate('created_at')).values('date').distinct()
        context['tasks_by_date'] = {timezone.localdate().today() - timezone.timedelta(days=i): None for i in range(2)}
        tasks_by_date = {date['date']: Task.objects.filter(
            user_id=user_id, created_at__date=date['date']) for date in dates}
        context['tasks_by_date'].update(tasks_by_date)
        context['user'] = User.objects.get(id=user_id)
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')