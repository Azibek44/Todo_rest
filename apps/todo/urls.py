from rest_framework.routers import DefaultRouter

from django.urls import path

from apps.todo.views import TodoAPIViewSet

router = DefaultRouter()
router.register('todo',TodoAPIViewSet,basename='todo_api')

urlpatterns = [
    
]

urlpatterns += router.urls