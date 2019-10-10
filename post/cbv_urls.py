from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from post import views

# Default Router 사용 X ==> API ROOT 없음. 

urlpatterns = [
    # 127.0.0.1:8000/post == ListView
    path('cbvPost/', views.PostList.as_view()),  
    # 127.0.0.1:8000/post/<pk> == DetailView
    path('cbvPost/<int:pk>/', views.PostDetail.as_view()), 
]

#
urlpatterns = format_suffix_patterns(urlpatterns)