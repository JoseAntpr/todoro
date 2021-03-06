from rest_framework import serializers

from tasks.models import Task

class TasksListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ("id", "name", "status")

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('owner', )