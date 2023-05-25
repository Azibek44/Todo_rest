from rest_framework.viewsets import GenericViewSet,mixins
from rest_framework import generics
from rest_framework import filters
from .permision import TodoPermission
from apps.todo.models import Todo
from apps.todo.serializer import TodoSerializer
from rest_framework.response import Response
# Create your views here.
class TodoAPIViewSet(GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = TodoPermission
    
class TodoALLDEL(generics.DesrtoyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permision_class = TodoPermission
    
    
    
    def delete(self,request,*args, **kwargs):
        todo = Todo.objects.filter(user = request.user)
        todo = [i for i in todo.delete()]
        
        
        return Response({"delete":"Все таски удалены "})