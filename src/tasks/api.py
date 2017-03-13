from rest_framework.generics import ListCreateAPIView

from rest_framework.response import Response

from tasks.models import Task
from tasks.serializer import TasksSerializer


class TasksApi(ListCreateAPIView):
    """
    Lists (GET) and Creates (POST) Tasks
    """
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
