from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from tasks.models import Task
from tasks.serializer import TasksSerializer, TasksListSerializer




class TaskViewSet(ModelViewSet):
    """
    Lists (GET) and Creates (POST) Tasks
    """
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        return TasksListSerializer if self.action == "list" else TasksSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
