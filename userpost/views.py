from userpost.models import UserPost
from userpost.serializer import UserPostSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication

# Create your views here.
class UserPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body',)
    #어떤 칼럼을 기반으로 검색을 할건지

    def get_queryset(self):
        #쿼리 셋 filter 
        qs = super().get_queryset()
        #request를 보낸 유저의 글만 필터링
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()

        return qs
    
    def perform_create(self,serializer):
        serializer.save(author=self.request.user)