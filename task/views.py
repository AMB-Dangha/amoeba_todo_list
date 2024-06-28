from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy
from .forms import TaskForm


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'

    def get_queryset(self):
        return Task.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_tasks'] = context.get('object_list')
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