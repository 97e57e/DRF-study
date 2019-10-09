# 프로젝트 urls.py
# post 앱의 url을 include 해서 계층적으로 관리함.

from django.contrib import admin
from django.urls import path, include
import post.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
]
