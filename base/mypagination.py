from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import PageNumberPagination

class MyLimitOffsetPagination(PageNumberPagination):
    default_limit=5
    page_size = 5
    limit_query_param='limit'
    offset_query_param='offset'
    max_limit=5
