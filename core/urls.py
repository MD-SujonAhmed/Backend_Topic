from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # অ্যাডমিন প্যানেল (ডিফল্ট)
    path('admin/', admin.site.urls),
    
    # আপনার তৈরি করা এপিআই এর রুট এখানে কানেক্ট করা হলো
    path('api/', include('api.urls')), 
]