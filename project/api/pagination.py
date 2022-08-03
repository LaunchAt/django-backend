from rest_framework.pagination import CursorPagination as BaseCursorPagination


class CursorPagination(BaseCursorPagination):
    max_page_size = 100
    ordering = '-created_at'
    page_size_query_param = 'page_size'
