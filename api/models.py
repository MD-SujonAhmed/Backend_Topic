from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('author', 'Author'),
        ('subscriber', 'Subscriber'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='subscriber')
    

class Blog(models.Model): # Module 3: CRUD API
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_thumbnails/', null=True, blank=True) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,db_index=True)