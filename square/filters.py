import django_filters
from .models import MealInfo

class MealInfoFilter(django_filters.FilterSet):
    member_num = django_filters.NumberFilter(field_name='member_num')
    earliest_time = django_filters.DateTimeFilter(field_name='meal_time',lookup_expr='gte')
    latest_time = django_filters.DateTimeFilter(field_name='meal_time',lookup_expr='lte')
    spicy_level = django_filters.NumberFilter(field_name='spicy')
    meal_type = django_filters.NumberFilter(field_name='type')
    min_cost = django_filters.NumberFilter(field_name='cost', lookup_expr='gte')
    max_cost = django_filters.NumberFilter(field_name='cost', lookup_expr='lte')
    class Meta:
        model = MealInfo
        fields = ['grade','member_num','meal_time','spicy','type','cost']