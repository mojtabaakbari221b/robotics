from functools import wraps
from django.db.models import QuerySet
from rest_framework.response import Response

def filtering(func):

    @wraps(func)
    def inner(self, *args, **kwargs):
        queryset = func(self, *args, **kwargs)
        assert isinstance(queryset, (list, QuerySet)), "apply_pagination expects a List or a QuerySet"

        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        # return queryset
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    return inner