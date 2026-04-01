from django.urls import path
from .views import RegisterView, BlogListCreateView, BlogDetailView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Module 1: Authentication (JWT)
    # এই ইউআরএল দিয়ে ইউজার রেজিস্ট্রেশন করবে
    path('register/', RegisterView.as_view(), name='register'),
    
    # এই ইউআরএল এ ইউজারনেম/পাসওয়ার্ড দিলে টোকেন পাওয়া যাবে (Login)
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # টোকেন এক্সপায়ার হয়ে গেলে নতুন টোকেন নেওয়ার জন্য
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Module 3: REST API (Blog CRUD)
    # সব ব্লগের লিস্ট দেখা এবং নতুন ব্লগ তৈরি করা (POST)
    path('blogs/', BlogListCreateView.as_view(), name='blog-list'),
    
    # নির্দিষ্ট একটি ব্লগ দেখা, আপডেট করা বা ডিলিট করা
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
]