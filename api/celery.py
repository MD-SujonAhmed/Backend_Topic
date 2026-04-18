import os
from celery import Celery

# জ্যাঙ্গো সেটিংস ফাইল সেট করা # Django Settings file set kora 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('skillshare_pro')

# জ্যাঙ্গো সেটিংস থেকে কনফিগ নেওয়া
app.config_from_object('django.conf:settings', namespace='CELERY')

# সব অ্যাপের ভেতর থেকে টাস্ক খুঁজে বের করা
app.autodiscover_tasks()