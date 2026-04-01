from rest_framework import generics, permissions
from .models import User, Blog
from .serializers import UserSerializer, BlogSerializer
from .permissions import IsAuthorOrAdmin

# Modul 1 Register 
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# মডিউল ৩: ব্লগের লিস্ট এবং ক্রিয়েট
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrAdmin]