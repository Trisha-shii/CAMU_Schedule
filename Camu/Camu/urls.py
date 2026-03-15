from django.contrib import admin
from django.urls import path
from MyCamu.views import schedule_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schedule/', schedule_view), # Access this at http://127.0.0.1:8000/schedule/
]