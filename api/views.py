from rest_framework import generics, permissions
from .models import User, Blog
from .serializers import UserSerializer, BlogSerializer
from .permissions import IsAuthorOrAdmin
from .tasks import send_welcome_email_task

# Modul 1 Register 
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self,serializer):
        user=serializer.save()
        send_welcome_email_task.delay(user.email)

class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.select_related('author').all() 

    serializer_class = BlogSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.select_related('author').only(
    'title', 
    'author__username', 
    'created_at'
)
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrAdmin]