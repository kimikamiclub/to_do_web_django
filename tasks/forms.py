from django import forms
from .models import TaskItem


class TaskItemCreateForm(forms.ModelForm):
    class Meta:
        model = TaskItem
        fields = ('title', 'description', 'due_date', 'status', 'category')


class TaskItemUpdateForm(forms.ModelForm):
    class Meta:
        model = TaskItem
        fields = ('title', 'description', 'due_date', 'status', 'category')
