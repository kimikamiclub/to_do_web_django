from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TaskItem
from .forms import TaskItemCreateForm, TaskItemUpdateForm


# Create your views here.

class TodoItemListView(ListView):
    model = TaskItem
    template_name = 'task/task_list.html'


class TodoItemCreateView(CreateView):
    model = TaskItem
    template_name = 'task/task_create_form.html'
    form_class = TaskItemCreateForm
    success_url = '/todo/list'


class TodoItemUpdateView(UpdateView):
    model = TaskItem
    template_name = 'task/task_update_form.html'
    form_class = TaskItemUpdateForm
    success_url = '/todo/update'


class TodoItemDeleteView(DeleteView):
    model = TaskItem
    template_name = 'task/task_delete_form.html'
    success_url = "/todo/delete"
