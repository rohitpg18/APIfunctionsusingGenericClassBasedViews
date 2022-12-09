
from rest_framework.pagination import PageNumberPagination

class StudentPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'

class StudentOptionalPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 1000
    page_size_query_param = 'page_size'

    def paginate_queryset(self, queryset, request, view=None):
        page_size = request.GET.get('page_size')
        if not page_size :
            return None
        else:
            return super(StudentOptionalPagination,self).paginate_queryset(queryset, request, view)
