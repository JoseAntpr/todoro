from django import forms

from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["name", "description", "time_estimated", "deadline", "assignee"]