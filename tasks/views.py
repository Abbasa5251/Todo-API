from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .api.serializers import TaskSerializer

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    
    tasks = Task.objects.filter().exclude(is_deleted=True)
    serializer = TaskSerializer(tasks, many=True)
    return Response({"result": serializer.data})