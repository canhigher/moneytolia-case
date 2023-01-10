from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action

from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(methods=['GET'], detail=False, name="Get random todo")
    def random(self, request, *args, **kwargs):
        instance = Todo.objects.order_by('?').first()
        serializer = TodoSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
