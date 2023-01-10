from django.contrib import admin
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
    path('admin/', admin.site.urls),
    path('todo/', todo_list, name="todo-list"),
    path('todo/random/', todo_random, name="todo-random"),
    path('todo/<int:pk>', todo_detail, name="todo-detail")
]
