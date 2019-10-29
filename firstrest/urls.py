# 프로젝트 urls.py
# post 앱의 url을 include 해서 계층적으로 관리함.

from django.contrib import admin
from django.urls import path, include
import post.urls
import post.cbv_urls
import userpost.urls
from rest_framework import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('', include('post.cbv_urls')),
    path('userpost/', include('userpost.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
