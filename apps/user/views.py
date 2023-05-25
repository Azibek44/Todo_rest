from rest_framework.viewsets import GenericViewSet,mixins

from .models import User
from .serializer import UserSerializer,UserRegisterSerializer

# Create your views here.
class UserAPIViewSet(GenericViewSet,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_serializer_class(self):
            if self.action in ('create', ):
                return UserRegisterSerializer
            return UserSerializer