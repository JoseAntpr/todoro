from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from tasks.models import Task
from tasks.serializer import TasksSerializer, TasksListSerializer




class TasksApi(ListCreateAPIView):
    """
    Lists (GET) and Creates (POST) Tasks
    """
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        return TasksListSerializer if self.request.method == "GET" else TasksSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskDetailApi(RetrieveUpdateDestroyAPIView):
    """
    Retrives(GET), Updates (PUT) and Destroy (DELETE) a given Task
    """

    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    permission_classes = (IsAuthenticated,)