from rest_framework import serializers
from ..models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'author', 'description', 'is_completed', 'created_at', 'modified_at')
        read_only = ('id', 'created_at', 'modified_at')

