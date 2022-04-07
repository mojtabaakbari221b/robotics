from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.exceptions import ValidationError

class ExcludeTagFilterBackend(DjangoFilterBackend):
    valid_entity = [
        'product',
        'news',
        'organ',
    ]

    def filter_queryset(self, request, queryset, view):
        queryset = super().filter_queryset(request, queryset, view)
        entity_name = request.GET.get('entity')
        if entity_name :
            if entity_name not in self.valid_entity :
                raise ValidationError
            if entity_name == 'organ' :
                return queryset.exclude(organ=None)
            if entity_name == 'product' :
                return queryset.exclude(product=None)
            if entity_name == 'news' :
                return queryset.exclude(news=None)
        return queryset
