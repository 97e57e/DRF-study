from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

#django rest framewokr - > router - > url

router = DefaultRouter()
router.register('', views.UserPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]