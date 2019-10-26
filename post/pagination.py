from rest_framework.pagination import PageNumberPagination

#커스텀 페이지네이션
class MyPagination(PageNumberPagination):
    page_size = 5