from django.urls import path

from todo.views import TodoViewSet


todo_list = TodoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

todo_random = TodoViewSet.as_view({
    'get': 'random'
})

todo_detail = TodoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', todo_list, name="todo-list"),
    path('random/', todo_random, name="todo-random"),
    path('<int:pk>/', todo_detail, name="todo-detail")
]
