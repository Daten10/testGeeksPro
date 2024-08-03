from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Task


class TaskListAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
                serializer = TaskSerializer(data=request.data)
                if not serializer.is_valid():
                    return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

                title = serializer.validated_data.get('title')
                description = serializer.validated_data.get('description')
                completed = serializer.validated_data.get('completed')
                created = serializer.validated_data.get('created')

                task = Task.objects.create(
                    title=title,
                    description=description,
                    completed=completed,
                    created=created
                )
                return Response(data={'task_id': task.id,
                                      'title': task.title,
                                      'description': task.description,
                                      'completed': task.completed,
                                      'created': task.created}, status=status.HTTP_201_CREATED)


class TaskItemAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'
